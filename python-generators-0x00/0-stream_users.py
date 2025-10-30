#!/usr/bin/python3
"""
0-stream_users.py
Provides a generator that yields rows from the user_data table one at a time.
"""

from seed import connect_to_prodev

def stream_users():
    """
    Connect to ALX_prodev and yield rows from user_data one-by-one as dicts.
    Uses a single loop (while True + fetchone) and ensures resources are closed.
    """
    connection = connect_to_prodev()
    if connection is None:
        return  # nothing to yield if we couldn't connect

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM user_data")
        # single loop: fetch rows one by one and yield them
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row
    finally:
        # This will run when generator is exhausted or when the generator is closed
        try:
            cursor.close()
        except Exception:
            pass
        try:
            connection.close()
        except Exception:
            pass
