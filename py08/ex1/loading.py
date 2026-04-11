import sys
import importlib


def get_version(module_name: str) -> str | None:
    try:
        mod = importlib.import_module(module_name)
        return getattr(mod, "__version__", "unknown")
    except ImportError:
        return None


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    dependencies = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization"
    }

    missing_packages = False


    for pkg, desc in dependencies.items():
        version = get_version(pkg)
        if version:
            print(f"[OK] {pkg} ({version})")
        else:
            print(f"[FAIL] {pkg} is missing!")
            missing_packages = True

    if missing_packages:
        print("\nCRITICAL ERROR: Missing required programs.")
        print("To load these programs using pip:")
        print("  pip install -r requirements.txt")
        print("\nTo load these programs using Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
        sys.exit(1)

    # Print readiness status
    for desc in dependencies.values():
        print(f"{desc} ready")

    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    # Simulating Matrix data using numpy as required
    np.random.seed(42)
    matrix_data = np.random.rand(1000, 2)
    df = pd.DataFrame(matrix_data, columns=["Resonance", "Frequency"])

    print("Generating visualization...")
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Resonance"], df["Frequency"], c='green', alpha=0.5,
                marker='.')
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Resonance")
    plt.ylabel("Frequency")

    # Save the output
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
