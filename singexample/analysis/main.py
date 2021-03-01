"""Example file for importing and pathing within the project."""
import sys

import pandas as pd
import singexample as se


def print_examples():
    """Print out examples using imports and storage."""
    print("You ran the Python file!")
    print(sys.argv)
    print(se.project_root())
    print(se.storage_root())

    df = pd.read_csv(se.storage_root() / "iris.csv")
    df.to_csv(se.outputs_root() / "iris.csv")
    print(df)


print_examples()
