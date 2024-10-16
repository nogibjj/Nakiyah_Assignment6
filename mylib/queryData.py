import os
from databricks import sql
from dotenv import load_dotenv


# Define a global variable for the log file
LOG_FILE = "query_log.md"


def logQuery(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def queryData(query):

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    cursor.close()
    logQuery(f"{query}", result)