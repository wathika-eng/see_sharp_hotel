# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set environment variable to ensure that Python output is displayed immediately
ENV PYTHONUNBUFFERED=1

# Set the working directory to where settings.py can be found
WORKDIR /Restaurant_management_system

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the entire current directory to the container
COPY . .

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=Restaurant_management_system.settings
ENV PYTHONPATH=/Restaurant_management_system

# Collect static files (for production)
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Expose port 8000 for the application
EXPOSE 8000

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

##                TESTS                  ###
# HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
# CMD curl --fail http://localhost:8000/ || exit 1
