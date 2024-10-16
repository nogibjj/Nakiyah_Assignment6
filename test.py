"""
Unit tests for extractData, loadData, and logQuery functions
"""
import subprocess


def testExtract():
    """Tests the extractData function"""
    result = subprocess.run(
        ["python3", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Data has been saved into two CSV files" in result.stdout


def testTransformLoad():
    """Tests the loadData function"""
    result = subprocess.run(
        ["python3", "main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Employee table created successfully" in result.stdout
    assert "All employee data inserted successfully" in result.stdout
    assert "Mental health table created successfully" in result.stdout
    assert "All mental health data inserted successfully" in result.stdout


def test_generalQuery():
    """tests general_query"""
    result = subprocess.run(
        [
            "python3",
            "main.py",
            "general_query",
            """SELECT 
                employee.Job_Role,
                AVG(employee.Years_of_Experience) AS avg_years_of_experience,
                AVG(mentalhealth.Hours_Worked_Per_Week) AS avg_hours_worked_per_week
            FROM 
                nd191_employee_data employee
            JOIN 
                nd191_mentalhealth_data mentalhealth ON employee.Employee_ID = mentalhealth.Eployee_ID
            GROUP BY employee.Job_Role
            ORDER BY Job_Role DESC
            LIMIT 10""",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0



if __name__ == "__main__":
    testExtract()
    testTransformLoad()
