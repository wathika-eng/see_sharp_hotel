-- Create table for Product model
CREATE TABLE
    Product (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(50) NOT NULL,
        category VARCHAR(50) NOT NULL DEFAULT '',
        subcategory VARCHAR(50) NOT NULL DEFAULT '',
        price INTEGER NOT NULL DEFAULT 0,
        description VARCHAR(200) NOT NULL,
        pub_date DATE NOT NULL,
        image VARCHAR(100) NOT NULL DEFAULT 'shop/images'
    );

-- Create table for Contact model
CREATE TABLE
    Contact (
        msg_id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(70) NOT NULL DEFAULT '',
        phone VARCHAR(70) NOT NULL DEFAULT '',
        description VARCHAR(500) NOT NULL DEFAULT '',
        timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

-- Create table for Orders model
CREATE TABLE
    Orders (
        order_id SERIAL PRIMARY KEY,
        items_json VARCHAR(5000) NOT NULL,
        userId INTEGER NOT NULL DEFAULT 0,
        amount INTEGER NOT NULL DEFAULT 0,
        name VARCHAR(90) NOT NULL,
        email VARCHAR(111) NOT NULL,
        city VARCHAR(111) NOT NULL,
        estate VARCHAR(111) NOT NULL,
        apartment VARCHAR(111) NOT NULL,
        phone VARCHAR(111) NOT NULL DEFAULT '',
        timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

-- Create table for OrderUpdate model
CREATE TABLE
    OrderUpdate (
        update_id SERIAL PRIMARY KEY,
        order_id INTEGER NOT NULL DEFAULT 0,
        update_desc VARCHAR(5000) NOT NULL,
        timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );