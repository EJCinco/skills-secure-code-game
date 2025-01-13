'''
Please note:

The first file that you should run in this level is tests.py for database creation, with all tests passing.
Remember that running the hack.py will change the state of the database, causing some tests inside tests.py
to fail.

If you like to return to the initial state of the database, please delete the database (level-4.db) and run 
the tests.py again to recreate it.
'''

import sqlite3
import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    DB_CRUD_ops().get_stock_info(request.args["input"])
    DB_CRUD_ops().get_stock_price(request.args["input"])
    DB_CRUD_ops().update_stock_price(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class Connect:
    """Handles database connection."""
    def create_connection(self, path):
        try:
            return sqlite3.connect(path)
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
            return None

class Create:
    """Initializes the database if it does not exist."""
    def __init__(self):
        con = Connect()
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, 'level-4.db')
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()

            # Check if the stocks table exists; if not, create it
            cur.execute("""
                CREATE TABLE IF NOT EXISTS stocks (
                    date TEXT,
                    symbol TEXT,
                    price REAL
                )
            """)

            # Insert dummy data if the table is empty
            if not cur.execute("SELECT 1 FROM stocks LIMIT 1").fetchone():
                cur.execute("INSERT INTO stocks (date, symbol, price) VALUES ('2022-01-06', 'MSFT', 300.00)")
                db_con.commit()

        except sqlite3.Error as e:
            print(f"ERROR: {e}")
        finally:
            if db_con:
                db_con.close()

class DB_CRUD_ops:
    """Performs CRUD operations on the database."""
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'level-4.db')
        Create()  # Ensure the database is initialized

    def get_stock_info(self, stock_symbol):
        """Fetches all stock information for a given symbol."""
        con = Connect().create_connection(self.db_path)
        try:
            res = "[METHOD EXECUTED] get_stock_info\n"
            query = "SELECT * FROM stocks WHERE symbol = ?"
            res += f"[QUERY] {query.replace('?', repr(stock_symbol))}\n"

            cur = con.cursor()
            cur.execute(query, (stock_symbol,))
            for row in cur.fetchall():
                res += f"[RESULT] {row}\n"
            return res

        except sqlite3.Error as e:
            return f"ERROR: {e}"
        finally:
            if con:
                con.close()

    def get_stock_price(self, stock_symbol):
        """Fetches the price of a given stock symbol."""
        con = Connect().create_connection(self.db_path)
        try:
            res = "[METHOD EXECUTED] get_stock_price\n"
            query = "SELECT price FROM stocks WHERE symbol = ?"
            res += f"[QUERY] {query.replace('?', repr(stock_symbol))}\n"

            cur = con.cursor()
            cur.execute(query, (stock_symbol,))
            for row in cur.fetchall():
                res += f"[RESULT] {row}\n"
            return res

        except sqlite3.Error as e:
            return f"ERROR: {e}"
        finally:
            if con:
                con.close()

    def update_stock_price(self, stock_symbol, price):
        """Updates the price of a stock."""
        if not isinstance(price, (float, int)):
            return "ERROR: Stock price must be a number."

        con = Connect().create_connection(self.db_path)
        try:
            res = "[METHOD EXECUTED] update_stock_price\n"
            query = "UPDATE stocks SET price = ? WHERE symbol = ?"
            res += f"[QUERY] {query.replace('?', repr(price)).replace('?', repr(stock_symbol))}\n"

            cur = con.cursor()
            cur.execute(query, (price, stock_symbol))
            con.commit()
            return res

        except sqlite3.Error as e:
            return f"ERROR: {e}"
        finally:
            if con:
                con.close()




