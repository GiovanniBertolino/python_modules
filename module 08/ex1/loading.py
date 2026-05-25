import sys
import importlib


def show_pip_vs_poetry() -> None:
    print("\nComparison of dependency managers:\n")

    print("pip:")
    print("- installs packages in the current environment")
    print("- uses requirements.txt")
    print("- simpler and widely used")
    print("- no automatic dependency locking\n")

    print("poetry:")
    print("- manages virtual environments automatically")
    print("- uses pyproject.toml")
    print("- locks exact versions with poetry.lock")
    print("- better dependency resolution\n")


def loading() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    pandas = None
    numpy = None
    matplotlib = None
    pyplot = None
    plt = None
    try:
        pandas = importlib.import_module("pandas")
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("[MISSING] pandas - install with: pip install pandas")

    try:
        numpy = importlib.import_module("numpy")
        print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
    except ImportError:
        print("[MISSING] numpy - install with: pip install numpy")

    try:
        matplotlib = importlib.import_module("matplotlib")
        pyplot = importlib.import_module("matplotlib.pyplot")
        plt = pyplot
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready\n")
    except ImportError:
        print("[MISSING] matplotlib - install with: pip install matplotlib\n")

    dependencies = [pandas, numpy, matplotlib]
    if any(e is None for e in dependencies):
        print("Missing dependencies, install them first:")
        print("Installing with pip: pip install -r requirements.txt")
        print("Installing with Poetry: poetry install")
        sys.exit(1)

    show_pip_vs_poetry()
    print("Analyzing Matrix data...")
    data = numpy.random.randint(0, 100, size=1000)
    print("Processing 1000 data points...")
    dataframe = pandas.DataFrame({"matrix_signal": data})
    print("Generating visualization...\n")
    plt.plot(dataframe)
    plt.title('matrix_analysis')
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig('matrix_analysis.png')
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    loading()
