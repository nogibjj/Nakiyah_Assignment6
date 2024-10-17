import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

## Transforms and Loads employee and mental health data into the specified Databricks database
def loadData(employee_dataset="Data/EmployeeData.csv", mentalhealth_dataset="Data/MentalHealthData.csv"):

    database_name = "nd191_assignment6"
    employee_table = "nd191_employee_data"
    mentalhealth_table = "nd191_mentalhealth_data"
    
    # Load datasets
    df_employee = pd.read_csv(employee_dataset)
    df_mentalhealth = pd.read_csv(mentalhealth_dataset)

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    
    with sql.connect(server_hostname=server_h,
                     http_path=http_path,
                     access_token=access_token) as connection:
        cursor = connection.cursor()
        
        # Create and use the database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        cursor.execute(f"USE {database_name}")
        
        # Drop the employee table if it exists
        cursor.execute(f"DROP TABLE IF EXISTS {employee_table}")
        
        # Create employee data table
        cursor.execute(
            f"""
            CREATE TABLE {employee_table} (
                Employee_ID STRING PRIMARY KEY, 
                Age INTEGER,                                
                Job_Role STRING,                              
                Industry STRING,                              
                Years_of_Experience INTEGER,                
                Work_Location STRING                         
            )
            """
        )

        print("Employee table created successfully.")

        # Check if DataFrame is empty
        if df_employee.empty:
            print("Employee DataFrame is empty.")
            return "Data loading aborted."

        print(f"Inserting {df_employee.shape[0]} rows into {employee_table}.")

        # Insert employee data using executemany for batch insertion
        insert_employee_query = f"INSERT INTO {employee_table} VALUES (?, ?, ?, ?, ?, ?)"
        for index, row in df_employee.iterrows():
            try:
                cursor.execute(insert_employee_query, tuple(row))
            except Exception as e:
                print(f"Error inserting row {index}: {e}")

        print("All employee data inserted successfully.")

        # Drop the mental health table if it exists
        cursor.execute(f"DROP TABLE IF EXISTS {mentalhealth_table}")

        # Create mental health data table
        cursor.execute(
            f"""
            CREATE TABLE {mentalhealth_table} (
                Employee_ID STRING PRIMARY KEY, 
                Hours_Worked_Per_Week INTEGER,             
                Mental_Health_Condition STRING,               
                Access_to_Mental_Health_Resources BOOLEAN
            )
            """
        )

        print("Mental health table created successfully.")

        # Insert mental health data
        if not df_mentalhealth.empty:
            print(f"Inserting {df_mentalhealth.shape[0]} rows into {mentalhealth_table}.")
            insert_mentalhealth_query = f"INSERT INTO {mentalhealth_table} VALUES (?, ?, ?, ?)"
            for index, row in df_mentalhealth.iterrows():
                try:
                    cursor.execute(insert_mentalhealth_query, tuple(row))
                except Exception as e:
                    print(f"Error inserting row {index}: {e}")

            print("All mental health data inserted successfully.")
    return "Data loaded successfully"

