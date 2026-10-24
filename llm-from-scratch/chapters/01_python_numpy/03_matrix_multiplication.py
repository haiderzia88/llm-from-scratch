"""Chapter 01, Lesson 03: Matrix multiplication and shapes.

Run: python chapters/01_python_numpy/03_matrix_multiplication.py

Rule: (m x n) @ (n x p) -> (m x p). The inner dimensions must match.
"""
import numpy as np


def main() -> None:
    # Example 1: (2 x 2) @ (2 x 2) -> (2 x 2)
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print("2x2 @ 2x2")
    print(a @ b)  # [[19, 22], [43, 50]]

    # Example 2: (5 x 2) @ (2 x 2) -> (5 x 2)
    five_by_two = np.array([
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
    ])
    two_by_two = np.array([[1, 2], [3, 4]])
    product = five_by_two @ two_by_two
    print("\n5x2 @ 2x2")
    print(product)
    print("Result shape:", product.shape)  # (5, 2)

    # Example 3: (2 x 2) @ (5 x 2) is NOT valid.
    print("\n2x2 @ 5x2")
    try:
        print(two_by_two @ five_by_two)
    except ValueError:
        print("Invalid: 2 columns in the left matrix != 5 rows in the right matrix")

    # Example 4: basic neural-network-like linear layer (not trained).
    inputs = np.array([2.0, 3.0])
    weights = np.array([[0.1, 0.4], [0.2, 0.5]])
    bias = np.array([0.1, -0.3])
    outputs = inputs @ weights + bias
    print("\nLinear layer output:", outputs)  # [0.9, 2.0]

    # Your turn: predict the shape of (3 x 4) @ (4 x 6).


if __name__ == "__main__":
    main()
