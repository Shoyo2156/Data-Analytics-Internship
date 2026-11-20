
import sqlite3

DB_PATH = "bluestock_mf.db"
SQL_PATH = "sql/queries.sql"

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Read SQL file
with open(SQL_PATH, "r", encoding="utf-8") as file:
    sql_content = file.read()

# Split queries using semicolon
queries = [
    query.strip()
    for query in sql_content.split(";")
    if query.strip()
]

print("Total queries found:", len(queries))

# Execute each query
for i, query in enumerate(queries, start=1):
    print("\n" + "=" * 60)
    print(f"QUERY {i}")
    print("=" * 60)

    try:
        cursor = conn.execute(query)

        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        print(columns)

        for row in rows[:10]:
            print(row)

        print("Total rows returned:", len(rows))

    except Exception as error:
        print("ERROR:", error)

conn.close()

print("\nAll queries processed!")
