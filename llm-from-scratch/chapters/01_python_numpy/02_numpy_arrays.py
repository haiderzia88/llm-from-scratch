"""Chapter 01, Lesson 02: NumPy arrays, shapes, and operations.

Run: python chapters/01_python_numpy/02_numpy_arrays.py
"""
import numpy as np


def main() -> None:
    # A scalar has no axes; a vector has one axis; a matrix has two.
    scalar = np.array(5)
    vector = np.array([2, 4, 6])
    matrix = np.array([[1, 2, 3], [4, 5, 6]])

    print("SCALAR, VECTOR, MATRIX")
    for name, value in [("Scalar", scalar), ("Vector", vector), ("Matrix", matrix)]:
        print(f"{name}: {value}, ndim={value.ndim}, shape={value.shape}")

    # * multiplies matching elements. Dot product adds matching products.
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("\nELEMENT-WISE MULTIPLICATION")
    print("a * b =", a * b)               # [4, 10, 18]
    print("\nDOT PRODUCT")
    print("np.dot(a, b) =", np.dot(a, b))  # 32

    # NumPy broadcasts a length-2 vector across the rows of a 2x2 matrix.
    inputs = np.array([[2, 3], [1, 4]])
    bias = np.array([0.1, 0.2])
    print("\nBROADCASTING")
    print("inputs + bias =\n", inputs + bias)

    # Your turn: calculate the shape of a (3, 4) matrix.
    # Calculate the dot product of [2, 4, 6] and [1, 3, 5].


if __name__ == "__main__":
    main()
