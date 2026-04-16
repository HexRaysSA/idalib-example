import argparse

from ida_domain.database import Database, IdaCommandOptions


def main():
    parser = argparse.ArgumentParser(description="Example headless IDA script")
    parser.add_argument("file", help="Path to file or IDB to open")
    args = parser.parse_args()

    ida_options = IdaCommandOptions(auto_analysis=True)
    with Database.open(args.file, ida_options) as db:
        print("Functions in the database:")
        for function in db.functions:
            print(f"{hex(function.start_ea)}: {function.name}")


if __name__ == "__main__":
    main()
