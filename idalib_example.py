import argparse

# NOTE: you have to import idapro first
import idapro

# Then the usual IDAPython imports
import idautils
import idaapi


def main():
    parser = argparse.ArgumentParser(description="Example headless IDA script")
    parser.add_argument("file", help="Path to file or IDB to open")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )
    args = parser.parse_args()

    if args.verbose:
        idapro.enable_console_messages(True)

    print(f"Opening database {args.file} with idalib")
    idapro.open_database(args.file, run_auto_analysis=True)

    idaapi.auto_wait()
    print(f"Auto-analysis completed for {args.file}")

    print("Functions in the database:")
    for func_ea in idautils.Functions():
        print(f"{hex(func_ea)}: {idaapi.get_func_name(func_ea)}")


if __name__ == "__main__":
    main()
