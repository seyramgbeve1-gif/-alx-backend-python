#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
import csv
import uuid

# Connect to MySQL server (not yet to a specific database)
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=King02432sley70seyram&$
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


# Create database if it doesn’t exist
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")


# Connect directly to the ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password",  # 🔁 same password
            database="ALX_prodev"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None


# Create table if not exists
def create_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(10,2) NOT NULL,
            INDEX (user_id)
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")


# Insert data into the table from CSV
def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = float(row['age'])
                
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))
        
        connection.commit()
        print(f"Data from {csv_file} inserted successfully.")
        cursor.close()
    except Error as e:
        print(f"Error inserting data: {e}")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
