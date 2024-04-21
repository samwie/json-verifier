import argparse

from src.verify_policy import RolePolicyParser

parser = argparse.ArgumentParser(
    description="Script for verification JSON files in AWS::IAM::Role Policy format. To perform verification, input the JSON file location."
)

parser.add_argument("-d", "--directory", help="Path to JSON file (REQUIRED)")
args = parser.parse_args()


def main() -> bool:

    if not args.directory:
        parser.print_help()
        exit(0)

    policy_parser = RolePolicyParser(args.directory)

    try:
        result = policy_parser.verify()
        print(result)
    except (FileNotFoundError, ValueError, KeyError, TypeError) as e:
        print(type(e).__name__, e)
    except Exception as e:
        print(f"Unhandled exception:{type(e).__name__}")


if __name__ == "__main__":
    main()
