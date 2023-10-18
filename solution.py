import sqlite3
import pandas as pd

database_file = '{path of the database.db}'

try:
    connection = sqlite3.connect(database_file)
    sql_query = "SELECT c.customer_id as Customer, c.age as Age, i.item_id as Item, SUM(o.quantity) AS Quantity FROM customers c JOIN sales s ON c.customer_id = s.customer_id JOIN orders o ON s.sales_id = o.sales_id JOIN items i ON o.item_id = i.item_id GROUP BY c.customer_id, i.item_id ORDER BY c.customer_id, i.item_id;"
		
    df = pd.read_sql_query(sql_query, connection)

    df = df[df['Age'] >= 18 ]
    df = df[df['Age'] <= 35 ]
    df = df[df['Quantity'] > 0 ]
    df = df[df['Quantity'].round() == df['Quantity']]
	
    if not df.empty:
        print("Final Output:")
        print(df)
    else:
        print("No rows match the filter criteria.")

    connection.close()

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
