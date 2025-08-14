#!/usr/bin/env python3
import sqlite3
from contextlib import closing
from datetime import datetime, date
import csv
import os
from typing import Optional, Iterable, Tuple

DB_PATH = os.path.join(os.path.dirname(__file__), "inventory.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

# ---------------------------
# Database Utilities
# ---------------------------
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Read schema from schema.sql and execute it."""
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = f.read()
    with closing(get_conn()) as conn, conn:
        conn.executescript(schema)

# ---------------------------
# CRUD and Reports
# (The rest of your functions from the original Python code remain here)
# ---------------------------

# ... [Place all the add_supplier, list_suppliers, add_product, update_product, 
# delete_product, list_products, record_sale, low_stock_report,
# sales_report_between, monthly_sales_report, export_rows_to_csv, CLI menus, main loop] ...

if __name__ == "__main__":
    init_db()
    main()
