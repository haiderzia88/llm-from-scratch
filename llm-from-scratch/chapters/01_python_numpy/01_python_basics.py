"""Chapter 01, Lesson 01: Learn Python basics for LLM development.

Run: python chapters/01_python_numpy/01_python_basics.py
"""


def multiply_numbers(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b


def main() -> None:
    # 1. Variables
    learning_rate = 0.01
    sentence = "I am learning LLMs"
    numbers = [10, 20, 30]
    print("VARIABLES")
    print("Learning rate:", learning_rate)
    print("Sentence:", sentence)
    print("Numbers:", numbers)

    # 2. Python list indexing: 0 is the first element, -1 is the last.
    tokens = ["I", "love", "Python"]
    print("\nLIST INDEXING")
    print("tokens[0] :", tokens[0])      # I
    print("tokens[1] :", tokens[1])      # love
    print("tokens[2] :", tokens[2])      # Python
    print("tokens[-1]:", tokens[-1])     # Python
    print("tokens[-2]:", tokens[-2])     # love
    print("len(tokens):", len(tokens))   # 3

    # 3. Loops
    print("\nLOOPS — doubled numbers")
    for number in [2, 4, 6]:
        print(number * 2)

    # 4. Functions
    print("\nFUNCTIONS")
    print("3 times 4 =", multiply_numbers(3, 4))

    # Your turn:
    # - Make a list of four programming languages.
    # - Print its final element using a negative index.
    # - Make a function that adds two numbers.


if __name__ == "__main__":
    main()
