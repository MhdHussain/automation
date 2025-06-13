import pandas as pd
import pyodbc

try:
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        + "Server=(localdb)\\MSSQLLocalDB;"
        + "Database=AdventureWorks2017;"
        + "Trusted_Connection=yes;"
    )
    print("Connected")
    cursor = connection.cursor()

    with open("queries.sql") as f:
        queries_content = f.read()

    queries = queries_content.split(";")
    dataframes = []

    for query in queries:
        query = query.strip()
        if not query:
            continue
        cursor.execute(query)
        if cursor.description:
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            df = pd.DataFrame.from_records(rows, columns=columns)
            dataframes.append(df)

    with pd.ExcelWriter("results.xlsx") as writer:
        startrow = 0
        for df in dataframes:
            df.to_excel(writer, sheet_name="Data", startrow=startrow, index=False)
            startrow += len(df) + 2

except pyodbc.Error as e:
    print("Unable to connect to the database", e)
