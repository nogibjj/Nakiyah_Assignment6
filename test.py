import subprocess


def test_extract():
    """Tests the extractData function."""
    try:
        result = subprocess.run(
            ["python3", "main.py", "extract"],
            capture_output=True,
            text=True,
            check=True,
        )
        print("Extract Output:")
        print(result.stdout)  # Print output for verification
    except subprocess.CalledProcessError as e:
        print("Extract stdout:", e.stdout)
        print("Extract stderr:", e.stderr)
        raise


def test_load():
    """Tests the loadData function."""
    try:
        result = subprocess.run(
            ["python3", "main.py", "load"],
            capture_output=True,
            text=True,
            check=True,
        )
        print("Load Output:")
        print(result.stdout)  # Print output for verification
    except subprocess.CalledProcessError as e:
        print("Load stdout:", e.stdout)
        print("Load stderr:", e.stderr)
        raise


def test_general_query():
    query = """
        SELECT employee.Job_Role, 
               AVG(employee.Years_of_Experience) AS avg_years_of_experience, 
               AVG(mentalhealth.Hours_Worked_Per_Week) AS avg_hours_worked_per_week
        FROM nd191_assignment6.nd191_employee_data employee
        JOIN nd191_assignment6.nd191_mentalhealth_data mentalhealth 
        ON employee.Employee_ID = mentalhealth.Employee_ID
        GROUP BY employee.Job_Role
        ORDER BY Job_Role DESC
        LIMIT 5;
    """
    try:
        result = subprocess.run(
            ["python3", "main.py", "query", query],
            capture_output=True,
            text=True,
            check=True,
        )
        print("General Query Output:")
        print(result.stdout)  # Print output for verification
    except subprocess.CalledProcessError as e:
        print("Query stdout:", e.stdout)
        print("Query stderr:", e.stderr)
        raise


if __name__ == "__main__":
    test_extract()  # To test extract functionality
    test_load()  # To test load functionality
    test_general_query()  # To test query functionality
