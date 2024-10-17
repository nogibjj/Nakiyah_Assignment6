install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py
	
lint:
	ruff check *.py

test:
	python3 -m pytest -vv --nbval -cov=mylib -cov=main test*.py
	
all: install format lint test

generate_and_push:
	# Create the markdown file 
	python test.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	python main.py extract

transform_load: 
	python main.py load

query:
	python main.py general_query """SELECT 
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