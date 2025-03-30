import numbers
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        if any(map(lambda row: len(row) != self.width, matrix)):
            raise ValueError("Incorrect dimension")

    def __add__(self, another_matrix):
        self._check_matrix(another_matrix)
        return Matrix([[self.matrix[i][j] + another_matrix.matrix[i][j]
                        for j in range(self.width)] for i in range(self.height)])

    def __mul__(self, another_matrix):
        self._check_matrix(another_matrix)
        return Matrix([[self.matrix[i][j] * another_matrix.matrix[i][j]
                        for j in range(self.width)] for i in range(self.height)])

    def __matmul__(self, another_matrix):
        self._check_matrix(another_matrix)
        return Matrix([[sum([self.matrix[i][k] * another_matrix.matrix[k][j]
                             for k in range(self.width)]) for j in range(another_matrix.width)]
                       for i in range(self.height)])

    def __str__(self):
        return str(self.matrix)

    def _check_matrix(self, another_matrix):
        if not isinstance(another_matrix, Matrix):
            raise ValueError("Given object is not a matrix")
        if self.height != another_matrix.height or self.width != another_matrix.width:
            raise ValueError("Given matrix has a wrong dimension")


# given from https://numpy.org/doc/2.2/reference/generated/numpy.lib.mixins.NDArrayOperatorsMixin.html
class ArithmeticArray(np.lib.mixins.NDArrayOperatorsMixin):
    # One might also consider adding the built-in list type to this
    # list, to support operations like np.add(array_like, list)
    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of
            # _HANDLED_TYPES. Use ArrayLike instead of type(self)
            # for isinstance to allow subclasses that don't
            # override __array_ufunc__ to handle ArrayLike objects.
            if not isinstance(
                x, self._HANDLED_TYPES + (Matrix,)
            ):
                return NotImplemented
        # Defer to the implementation of the ufunc
        # on unwrapped values.
        inputs = tuple(x.matrix if isinstance(x, Matrix) else x for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.matrix if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

    def write(self, path):
        with open(path, 'w') as file:
            file.write(str(self.__dict__['matrix']))

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return f"""
Matrix height: {self.__dict__['height']}
Matrix width: {self.__dict__['width']} 
Matrix itself: \n{self.__dict__['matrix']}
"""


class ArithmeticMatrixArray(ArithmeticArray, Matrix):
    pass


__all__ = [
    'Matrix',
    'ArithmeticArray',
    'ArithmeticMatrixArray'
]
