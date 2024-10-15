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
    # Check if the key messages indicating success are in the stdout
    assert "Data has been saved into two CSV files" in result.stdout
    assert "Employee table created successfully" in result.stdout
    assert "All employee data inserted successfully" in result.stdout
    assert "Mental health table created successfully" in result.stdout
    assert "All mental health data inserted successfully" in result.stdout

if __name__ == "__main__":
    testExtract()
    testTransformLoad()
