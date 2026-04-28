import sys
import importlib


def show_pip_vs_poetry() -> None:
    print("\nComparison of dependency managers:")
    print("\npip    : simple, universal, installs in the active environment")
    print("poetry : manages specific versions, automatic file locking")
    print("pip use the file: 'requirements.txt'")
    print("poetry use the file: 'pyproject.toml'\n")
    return


def loading() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependancies:")
    pandas = None
    numpy = None
    matplotlib = None
    try:
        pandas = importlib.import_module("pandas")
        print(f"[OK] pandas  ({pandas.__version__}) - Data manpulation ready")
    except ImportError:
        print("[MISSING] pandas - install with: pip install pandas")

    try:
        numpy = importlib.import_module("numpy")
        numpy_v = numpy.__version__
        print(f"[OK] numpy  ({numpy_v}) - Numerical computation ready")
    except ImportError:
        print("[MISSING] numpy - install with: pip install numpy")

    try:
        matplotlib = importlib.import_module("matplotlib")
        matplotlib.pyplot = importlib.import_module("matplotlib.pyplot")
        matplotlib_v = matplotlib.__version__
        print(f"[OK] matplotlib  ({matplotlib_v}) - Visualization ready\n")
    except ImportError:
        print("[MISSING] matplotlib - install with: pip install matplotlib\n")

    dependancies = [pandas, numpy, matplotlib]
    if any(e is None for e in dependancies):
        print("Missing dependencies, install them first:")
        print("Installing with pip: pip install -r requirements.txt")
        print("Installing with Poetry: poetry install")
        sys.exit(1)

    show_pip_vs_poetry()
    print("Analyzing Matrix data...")
    datas = numpy.array(numpy.random.randint(99, size=(1000)))
    print("Processing 1000 data points...")
    dataframe = pandas.DataFrame(datas)
    print("Generating visualization...\n")
    plt = matplotlib.pyplot
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
