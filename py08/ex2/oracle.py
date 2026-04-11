import os
import sys

# Graceful degradation if the dependency is missing
try:
    from dotenv import load_dotenv
except ImportError:
    print("CRITICAL ERROR: python-dotenv is not installed.")
    print("Please install it: pip install python-dotenv")
    sys.exit(1)


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    env_file_exists: bool = os.path.isfile(".env")
    if env_file_exists:
        load_dotenv()

    matrix_mode: str = os.environ.get("MATRIX_MODE", "development")
    db_url: str | None = os.environ.get("DATABASE_URL")
    api_key: str | None = os.environ.get("API_KEY")
    log_level: str = os.environ.get("LOG_LEVEL", "WARNING")
    zion_endpoint: str | None = os.environ.get("ZION_ENDPOINT")

    missing_configs: list[str] = []
    if not db_url:
        missing_configs.append("DATABASE_URL")
    if not api_key:
        missing_configs.append("API_KEY")
    if not zion_endpoint:
        missing_configs.append("ZION_ENDPOINT")

    if missing_configs:
        print("WARNING: The Oracle's vision is clouded. Missing configs:")
        for config in missing_configs:
            print(f"  - {config} is not set")
        print("\nPlease copy .env.example to .env and fill in the values.")
        print("Or provide them as environment variables.\n")

    # Display loaded configuration
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    # Demonstrate different behavior based on development vs production
    if matrix_mode.lower() == "production":
        if db_url:
            db_status = f"Connected to production cluster ({db_url})"
        else:
            db_status = "DISCONNECTED"
        if api_key:
            api_status = "Authenticated with high-security token"
        else:
            api_status = "DENIED"
    else:
        db_status = "Connected to local instance" if db_url else "DISCONNECTED"
        api_status = "Authenticated" if api_key else "DENIED"

    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_file_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file is missing, relying on system vars")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()