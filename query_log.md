```sql
SELECT employee.Job_Role, AVG(employee.Years_of_Experience) AS avg_years_of_experience, AVG(mentalhealth.Hours_Worked_Per_Week) AS avg_hours_worked_per_week FROM nd191_assignment6.nd191_employee_data employee JOIN nd191_assignment6.nd191_mentalhealth_data mentalhealth ON employee.Employee_ID = mentalhealth.Employee_ID GROUP BY employee.Job_Role ORDER BY Job_Role DESC LIMIT 10;
```

```response from databricks
[Row(Job_Role='Software Engineer', avg_years_of_experience=21.0, avg_hours_worked_per_week=39.0), Row(Job_Role='Sales', avg_years_of_experience=29.0, avg_hours_worked_per_week=41.666666666666664), Row(Job_Role='HR', avg_years_of_experience=20.5, avg_hours_worked_per_week=52.0), Row(Job_Role='Data Scientist', avg_years_of_experience=6.0, avg_hours_worked_per_week=43.333333333333336)]
```

```sql

        SELECT employee.Job_Role, 
               AVG(employee.Years_of_Experience) AS avg_years_of_experience, 
               AVG(mentalhealth.Hours_Worked_Per_Week) AS avg_hours_worked_per_week
        FROM nd191_assignment6.nd191_employee_data employee
        JOIN nd191_assignment6.nd191_mentalhealth_data mentalhealth 
        ON employee.Employee_ID = mentalhealth.Employee_ID
        GROUP BY employee.Job_Role
        ORDER BY Job_Role DESC
        LIMIT 10;
    
```

```response from databricks
[Row(Job_Role='Software Engineer', avg_years_of_experience=21.0, avg_hours_worked_per_week=39.0), Row(Job_Role='Sales', avg_years_of_experience=29.0, avg_hours_worked_per_week=41.666666666666664), Row(Job_Role='HR', avg_years_of_experience=20.5, avg_hours_worked_per_week=52.0), Row(Job_Role='Data Scientist', avg_years_of_experience=6.0, avg_hours_worked_per_week=43.333333333333336)]
```

```sql

        SELECT employee.Job_Role, 
               AVG(employee.Years_of_Experience) AS avg_years_of_experience, 
               AVG(mentalhealth.Hours_Worked_Per_Week) AS avg_hours_worked_per_week
        FROM nd191_assignment6.nd191_employee_data employee
        JOIN nd191_assignment6.nd191_mentalhealth_data mentalhealth 
        ON employee.Employee_ID = mentalhealth.Employee_ID
        GROUP BY employee.Job_Role
        ORDER BY Job_Role DESC
        LIMIT 10;
    
```

```response from databricks
[Row(Job_Role='Software Engineer', avg_years_of_experience=21.0, avg_hours_worked_per_week=39.0), Row(Job_Role='Sales', avg_years_of_experience=29.0, avg_hours_worked_per_week=41.666666666666664), Row(Job_Role='HR', avg_years_of_experience=20.5, avg_hours_worked_per_week=52.0), Row(Job_Role='Data Scientist', avg_years_of_experience=6.0, avg_hours_worked_per_week=43.333333333333336)]
```

