import sys
import argparse
from mylib.extractData import extractData
from mylib.loadData import loadData
from mylib.queryData import query


def handle_arguments(args):
    parser = argparse.ArgumentParser(description="ETL and Query Logging CLI Tool")

    parser.add_argument(
        "action",
        choices=["extract", "load", "query"],
        help="Specify the action to perform",
    )

    # Temporarily parse known arguments to check the action
    partial_args = parser.parse_args(args[:1])  # Parse only the 'action'

    # Add a query argument if the action is 'query'
    if partial_args.action == "query":
        parser.add_argument(
            "query", nargs=argparse.REMAINDER, help="SQL query to be executed"
        )

    return parser.parse_args(args)  # Fully parse the arguments


def main():
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extractData()
    elif args.action == "load":
        print("Loading data to Databricks...")
        loadData()
    elif args.action == "query":
        if not args.query:
            print("Error: A query is required for the 'query' action.")
            sys.exit(1)  # Exit the program if no query is provided
        else:
            # Join the SQL query list back into a string
            query_string = " ".join(args.query)
            print(f"Executing query: {query_string}")
            query(query_string)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
