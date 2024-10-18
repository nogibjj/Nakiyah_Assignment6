

```sql

        SELECT employee.Job_Role, 
               AVG(employee.Years_of_Experience) AS avg_years_of_experience, 
               AVG(mentalhealth.Hours_Worked_Per_Week) AS avg_hours_worked_per_week
        FROM nd191_assignment6.nd191_employee_data employee
        JOIN nd191_assignment6.nd191_mentalhealth_data mentalhealth 
        ON employee.Employee_ID = mentalhealth.Employee_ID
        GROUP BY employee.Job_Role
        ORDER BY Job_Role DESC
        LIMIT 5;
    
```

```response from databricks
[Row(Job_Role='Software Engineer', avg_years_of_experience=17.8, avg_hours_worked_per_week=42.333333333333336), Row(Job_Role='Sales', avg_years_of_experience=19.3125, avg_hours_worked_per_week=41.0), Row(Job_Role='Project Manager', avg_years_of_experience=19.72222222222222, avg_hours_worked_per_week=39.05555555555556), Row(Job_Role='Marketing', avg_years_of_experience=18.916666666666668, avg_hours_worked_per_week=31.25), Row(Job_Role='HR', avg_years_of_experience=15.0, avg_hours_worked_per_week=39.7)]
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
        LIMIT 5;
    
```

```response from databricks
[Row(Job_Role='Software Engineer', avg_years_of_experience=17.8, avg_hours_worked_per_week=42.333333333333336), Row(Job_Role='Sales', avg_years_of_experience=19.3125, avg_hours_worked_per_week=41.0), Row(Job_Role='Project Manager', avg_years_of_experience=19.72222222222222, avg_hours_worked_per_week=39.05555555555556), Row(Job_Role='Marketing', avg_years_of_experience=18.916666666666668, avg_hours_worked_per_week=31.25), Row(Job_Role='HR', avg_years_of_experience=15.0, avg_hours_worked_per_week=39.7)]
```

