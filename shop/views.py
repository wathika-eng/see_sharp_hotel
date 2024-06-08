from django_daraja.mpesa.core import MpesaClient
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import Product, Contact, Orders, OrderUpdate
from django.contrib.auth.models import User
from django.contrib import messages
from math import ceil
from django.contrib.auth import authenticate, login, logout
import json
from django.views.decorators.csrf import csrf_exempt
import os
import json
import datetime
from django.core.mail import EmailMessage
import africastalking


# Initialize SDK
username = os.environ[
    "username"
]  # use 'sandbox' for development in the test environment
api_key = os.environ[
    "api_key"
]  # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


def index(request):
    allProds = []
    category_prods = Product.objects.values("category", "id")
    cats = {item["category"] for item in category_prods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    products = {"allProds": allProds}
    return render(request, "shop/index.html", products)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    thankyou = False
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thankyou = True
        return render(request, "shop/contact.html", {"thankyou": thankyou})
    return render(request, "shop/contact.html", {"thankyou": thankyou})


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get("orderId", "")
        email = request.POST.get("email", "")
        name = request.POST.get("name", "")
        password = request.POST.get("password")
        user = authenticate(username=name, password=password)
        if user is not None:
            try:
                order = Orders.objects.filter(order_id=orderId, email=email)
                if len(order) > 0:
                    update = OrderUpdate.objects.filter(order_id=orderId)
                    updates = []
                    for item in update:
                        updates.append(
                            {"text": item.update_desc, "time": item.timestamp}
                        )
                        response = json.dumps(
                            {
                                "status": "success",
                                "updates": updates,
                                "itemsJson": order[0].items_json,
                            },
                            default=str,
                        )
                    return HttpResponse(response)
                else:
                    return HttpResponse('{"status":"no_item"}')
            except Exception as e:
                return HttpResponse('{"status":"error"}')
        else:
            return HttpResponse('{"status":"Invalid"}')
    return render(request, "shop/tracker.html")


def orderView(request):
    if request.user.is_authenticated:
        current_user = request.user
        orderHistory = Orders.objects.filter(userId=current_user.id)
        if len(orderHistory) == 0:
            messages.info(request, "You have not ordered.")
            return render(request, "shop/orderView.html")
        return render(request, "shop/orderView.html", {"orderHistory": orderHistory})
    return render(request, "shop/orderView.html")


def searchMatch(query, item):
    if (
        query in item.desc.lower()
        or query in item.product_name.lower()
        or query in item.category.lower()
        or query in item.desc
        or query in item.product_name
        or query in item.category
        or query in item.desc.upper()
        or query in item.product_name.upper()
        or query in item.category.upper()
    ):
        return True
    else:
        return False


def search(request):
    query = request.GET.get("search")
    allProds = []
    category_products = Product.objects.values("category", "id")
    cats = {item["category"] for item in category_products}
    for cat in cats:
        filtered_prods = Product.objects.filter(category=cat)
        prod = [item for item in filtered_prods if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    products = {"allProds": allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 3:
        products = {
            "msg": "No item available. Please make sure to enter relevant search query"
        }
    return render(request, "shop/search.html", products)


# @login_required
def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get("itemsJson", "")
        user_id = request.POST.get("user_id", "")
        name = request.POST.get("name", "")
        amount = request.POST.get("amount", "")
        email = request.POST.get("email", "")
        # address = request.POST.get("address1", "")
        city = request.POST.get("city", "")
        estate = request.POST.get("estate", "")
        apartment = request.POST.get("apartment", "")
        phone = request.POST.get("phone", "")
        order = Orders(
            items_json=items_json,
            userId=user_id,
            name=name,
            email=email,
            # address=address,
            city=city,
            estate=estate,
            apartment=apartment,
            phone=phone,
            amount=amount,
        )
        order.save()
        update = OrderUpdate(
            order_id=order.order_id, update_desc="The Order has been Placed"
        )
        update.save()
        thank = True
        id = order.order_id
        now = datetime.datetime.now()
        estimated_delivery_time = now + datetime.timedelta(hours=1)
        formatted_estimated_time = estimated_delivery_time.strftime("%Y-%m-%d %H:%M:%S")

        rider_details = "Rider John, +254712345678"  # Replace with actual rider details
        customer_care = "+254712345678"  # Replace with actual customer care number

        # Send SMS
        message = f"""Thank you {name} for your order!
                        Order Details: {items_json}
                        Order ID: {id}
                        Estimated Delivery Time: {formatted_estimated_time}
                        Rider Details: {rider_details}
                        Customer Care: {customer_care}
                        Total Amount: {amount}
                        Delivery is free!
                        Thank you for choosing Seesharp Hotel!"""
        try:
            # response = sms.send(message, [phone])
            # print(response)
            pass
        except Exception as e:
            pass
            # print(f"Error sending SMS: {e}")
        finally:
            email = EmailMessage(
                "Order Confirmation",
                message,
                "testkuku23@gmail.com",  # Sender's email address
                [email],  # List of recipient email addresses
            )
            email.send()
            print(f"Email sent successfully to {email}")
        if "onlinePay" in request.POST:
            try:
                cl = MpesaClient()
                account_reference = "seesharp Hotel"
                transaction_desc = f"Your order for {amount}"
                callback_url = "https://api.darajambili.com/express-payment"
                response = cl.stk_push(
                    phone,
                    int(amount),
                    account_reference,
                    transaction_desc,
                    callback_url,
                )
                return render(
                    request, "shop/checkout.html", {"thank": response, "id": id}
                )
            except Exception as e:
                # Log the error and send it to the frontend
                print(f"Error initiating M-Pesa STK Push: {e}")
                return JsonResponse({"error": str(e)}, status=400)
        elif "cashOnDelivery" in request.POST:
            return render(request, "shop/checkout.html", {"thank": thank, "id": id})
    return render(request, "shop/checkout.html")


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    # print(product)
    return render(request, "shop/prodView.html", {"product": product[0]})


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            messages.warning(request, "Invalid credentials! Please try again")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponse("404- Not found")


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST["username"]
        f_name = request.POST["f_name"]
        l_name = request.POST["l_name"]
        email = request.POST["email1"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        # check for errorneous input
        if password1 != password:
            messages.warning(request, " Passwords do not match")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        try:
            user = User.objects.get(username=username)
            messages.warning(
                request, " Username Already taken. Try with different Username."
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        except User.DoesNotExist:
            # Create the user
            myuser = User.objects.create_user(
                username=username, email=email, password=password
            )
            myuser.first_name = f_name
            myuser.last_name = l_name
            myuser.phone = phone
            myuser.save()
            messages.success(request, " Your Account has been successfully created")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponse("404 - Not found")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def error_404_view(request, exception):
    return redirect("shop/index.html")


# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == "CHECKSUMHASH":
#             checksum = form[i]

#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict["RESPCODE"] == "01":
#             print("order successful")
#         else:
#             print("order was not successful because" + response_dict["RESPMSG"])
#     return render(request, "shop/paymentstatus.html", {"response": response_dict})


def redirect_to_hotel(request):
    return redirect("shop/index.html")
