import sys
import argparse
from mylib.extractDataNew import extractData
from mylib.loadDataNew import loadData

def handle_arguments(args):
    """Handle command-line arguments and execute the corresponding function."""
    parser = argparse.ArgumentParser(description="ETL and Query Logging CLI Tool")
    
    parser.add_argument("action", 
                        choices=["extract", "load"], 
                        help="Specify the action to perform")
    
    if args and args[0] == "log_query":
        parser.add_argument("query", 
                            help="SQL query to be logged")
    
    return parser.parse_args(args)

def main():
    """Handle CLI commands."""
    args = handle_arguments(sys.argv[1:])
    
    if args.action == "extract":
        print("Extracting data...")
        extractData()
    elif args.action == "load":
        print("Loading data to Databricks...")
        loadData()
    else:
        print(f"Unknown action: {args.action}")

if __name__ == "__main__":
    main()
