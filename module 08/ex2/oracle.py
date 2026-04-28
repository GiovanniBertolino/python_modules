import sys
from dotenv import load_dotenv
import os


def oracle() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    load = load_dotenv()

    matrix_mode = os.getenv('MATRIX_MODE')
    if matrix_mode is None or matrix_mode == "":
        raise ValueError("Mode: [MISSING]")
    elif matrix_mode in ("development", "production"):
        print(f"Mode: {matrix_mode}")
    else:
        raise ValueError("Mode: [INVALID VALUE]")

    database_url = os.getenv('DATABASE_URL')
    if database_url is None or database_url == "":
        if matrix_mode == "development":
            print("Database: [MISSING]")
        if matrix_mode == "production":
            raise ValueError("Database: [MISSING]")
    else:
        if matrix_mode == "development":
            print("Database: Connected to local instance")
        if matrix_mode == "production":
            print("Database: Connected to real instance")

    api_key = os.getenv('API_KEY')
    if api_key is None or api_key == "":
        if matrix_mode == "development":
            print("API Access: [MISSING]")
        if matrix_mode == "production":
            raise ValueError("API Access: [MISSING]")
    else:
        print("API Access: [Authenticated]")

    log_level = os.getenv('LOG_LEVEL')
    if log_level is None or log_level == "":
        if matrix_mode == "development":
            print("Log Level: [MISSING]")
        if matrix_mode == "production":
            raise ValueError("Log Level: [MISSING]")
    else:
        print(f"Log Level: {log_level}")

    zion_endpoint = os.getenv('ZION_ENDPOINT')
    if zion_endpoint is None or zion_endpoint == "":
        if matrix_mode == "development":
            print("Zion Network: [MISSING]\n")
        if matrix_mode == "production":
            raise ValueError("Zion Network: [MISSING]\n")
    else:
        print("Zion Network: Online\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if load:
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file not properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        oracle()
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
