import numpy as np

from src.matrix import ArithmeticMatrixArray, Matrix

if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))
    with open("./artifacts/3.1/matrix+.txt", "w") as file:
        file.write(str(matrix1 + matrix2))
    with open("./artifacts/3.1/matrix*.txt", "w") as file:
        file.write(str(matrix1 * matrix2))
    with open("./artifacts/3.1/matrix@.txt", "w") as file:
        file.write(str(matrix1 @ matrix2))

    matrix1 = ArithmeticMatrixArray(np.random.randint(0, 10, (10, 10)))
    matrix2 = ArithmeticMatrixArray(np.random.randint(0, 10, (10, 10)))
    (matrix1 + matrix2).write("./artifacts/3.2/matrix+.txt")
    (matrix1 * matrix2).write("./artifacts/3.2/matrix*.txt")
    (matrix1 @ matrix2).write("./artifacts/3.2/matrix@.txt")

    print(matrix1)
    print(matrix2)

    # check that error is raised
    try:
        Matrix([[1, 2], [1]])
    except ValueError as e:
        print(e)

    try:
        Matrix([[1, 2], [1, 2]]) + [[1, 2], [1, 2]]
    except ValueError as e:
        print(e)

    try:
        Matrix([[1, 2], [1, 2]]) + Matrix([[1], [1]])
    except ValueError as e:
        print(e)

    try:
        Matrix([[1, 2], [1, 2]]) * Matrix([[1], [1]])
    except ValueError as e:
        print(e)

    try:
        Matrix([[1, 2], [1, 2]]) @ Matrix([[1], [1]])
    except ValueError as e:
        print(e)
