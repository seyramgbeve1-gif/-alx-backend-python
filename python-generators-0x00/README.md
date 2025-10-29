# Python Generators - Getting Started

## Objective
Create a generator that streams rows from an SQL database one by one.

This project sets up a MySQL database, creates a table, and seeds it with sample data for later generator use.

---

## Files
| File | Description |
|------|--------------|
| `seed.py` | Python script to connect, create database, create table, and insert data from CSV |
| `0-main.py` | Test script to verify setup |
| `user_data.csv` | CSV file with sample user data |

---

## Database Schema
**Database:** `ALX_prodev`  
**Table:** `user_data`

| Field | Type | Attributes |
|--------|------|-------------|
| `user_id` | CHAR(36) | Primary Key, Indexed |
| `name` | VARCHAR(255) | NOT NULL |
| `email` | VARCHAR(255) | NOT NULL |
| `age` | DECIMAL(10,2) | NOT NULL |

---

## Setup Instructions

1. Install MySQL and Python dependencies:
   ```bash
   sudo apt install mysql-server
   pip install mysql-connector-python
