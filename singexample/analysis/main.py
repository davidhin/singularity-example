"""Example file for importing and pathing within the project."""
import sys

import pandas as pd
import singexample as se


def print_examples():
    """Print out examples using imports and storage."""
    print("You ran the Python file!")
    print(sys.argv)
    print(se.project_dir())
    print(se.storage_dir())

    df = pd.read_csv(se.external_dir() / "iris.csv")
    df.to_csv(se.outputs_dir() / "iris.csv")
    print(df)


print_examples()
