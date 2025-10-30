#!/usr/bin/python3
stream_users = __import__('0-stream_users').stream_users

print("Streaming users from database...\n")

for user in stream_users():
    print(user)
