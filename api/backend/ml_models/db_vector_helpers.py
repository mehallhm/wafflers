"""
"""

from scipy.sparse import csr_matrix
from scipy.sparse import vstack


def string_to_sparse_matrix(sparse_matrix_string):
    """
    Converts a string representation of a sparse matrix back to a SciPy sparse matrix.

    Parameters:
    sparse_matrix_string (str): String representation of the sparse matrix.

    Returns:
    scipy.sparse.csr_matrix: The decoded sparse matrix.
    """
    if not sparse_matrix_string.startswith("SparseMatrix("):
        raise ValueError("Invalid sparse matrix string format.")

    # Extract the matrix dimensions and entries
    try:
        prefix, dims_and_entries = sparse_matrix_string.split("(", 1)
        dims, entries = dims_and_entries.split(", [")
        entries = entries.rstrip("])")

        rows, cols = map(int, dims.split(", "))
        entry_tuples = entries.split("), (")

        row_indices = []
        col_indices = []
        data = []

        # Iterate through the entries and parse them
        for entry in entry_tuples:
            entry = entry.strip("()")
            row, col, value = entry.split(", ")
            row_indices.append(int(row))
            col_indices.append(int(col))
            data.append(float(value))

        # Create the sparse matrix
        sparse_matrix = csr_matrix(
            (data, (row_indices, col_indices)), shape=(rows, cols)
        )
        return sparse_matrix

    except Exception as e:
        raise ValueError("Failed to parse sparse matrix string: " + str(e))


def stack_matrices(matrices):
    return vstack([*matrices])
