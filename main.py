import sys
import argparse
from mylib.extractData import extractData
from mylib.loadData import loadData
from mylib.queryData import queryData


def handle_arguments(args):
    """Handle command-line arguments and execute the corresponding function."""
    parser = argparse.ArgumentParser(description="ETL and Query Logging CLI Tool")

    parser.add_argument(
        "action",
        choices=["extract", "load", "general_query"],
        help="Specify the action to perform",
    )

    parser.add_argument(
        "query", nargs="?", help="SQL query to be executed", default=None
    )
    return parser.parse_args(args)


def main():

    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extractData()
    elif args.action == "load":
        print("Loading data to Databricks...")
        loadData()
    elif args.action == "general_query":
        print("Creating a general query...")
        queryData(args.query)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
