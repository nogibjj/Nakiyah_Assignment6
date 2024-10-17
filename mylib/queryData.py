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
        
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            logQuery(query, str(e))
            raise  # Re-raise the exception after logging
        finally:
            cursor.close()
        logQuery(f"{query}", result)

sqlCommand = """SELECT 
            employee.Job_Role,
            AVG(employee.Years_of_Experience) AS avg_years_of_experience,
            AVG(mentalhealth.Hours_Worked_Per_Week) AS avg_hours_worked_per_week
        FROM 
            nd191_assignment6.nd191_employee_data employee
        JOIN 
            nd191_assignment6.nd191_mentalhealth_data mentalhealth ON employee.Employee_ID = mentalhealth.Employee_ID
        GROUP BY employee.Job_Role
        ORDER BY Job_Role DESC
        LIMIT 10"""
    
queryData(sqlCommand)
        # cursor.execute(query)
        # result = cursor.fetchall()

