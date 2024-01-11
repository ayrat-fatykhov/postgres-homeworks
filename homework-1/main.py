"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

employees_path = "../homework-1/north_data/employees_data.csv"
customers_path = "../homework-1/north_data/customers_data.csv"
order_path = "../homework-1/north_data/orders_data.csv"


def instantiate_from_csv(csv_path):
    with open(csv_path, encoding="utf-8") as file:
        data = csv.DictReader(file)
        # print(data)
        items = list(data)
        # print(items)
        return items


if __name__ == '__main__':
    with psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='skypropython29'
    ) as conn:
        with conn.cursor() as cur:
            elements = instantiate_from_csv(employees_path)
            for element in elements:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                            (
                                element["employee_id"],
                                element["first_name"],
                                element["last_name"],
                                element["title"],
                                element["birth_date"],
                                element["notes"]
                            )
                            )
                cur.execute("SELECT * FROM customers")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

        with conn.cursor() as cur:
            elements = instantiate_from_csv(customers_path)
            for element in elements:
                cur.execute("INSERT INTO customers_v2 VALUES (%s, %s, %s)",
                            (
                                element["customer_id"],
                                element["company_name"],
                                element["contact_name"]
                                 )
                            )
                cur.execute("SELECT * FROM customers")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

        with conn.cursor() as cur:
            elements = instantiate_from_csv(order_path)
            for element in elements:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                            (
                                element["order_id"],
                                element["customer_id"],
                                element["employee_id"],
                                element["order_date"],
                                element["ship_city"]
                            )
                            )
                cur.execute("SELECT * FROM customers")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    conn.close()
