import numpy as np
from termcolor import colored
from math import fabs


class Matrix():
    def __init__(self, M_сol, N_str):
        self.M_сol = M_сol
        self.N_str = N_str
        self.__initialization_matrix1 = None
        self.__initialization_matrix2 = None
        self.__operations = None
        self.__transpose = None
        self.__is_square = None
        self.__is_identity = None
        self.__is_zero = None
        self.__is_diagonal = None
        self.__output = None
        self.__download = 'test'

    @property
    def initialization_matrix1(self):
        return self.__initialization_matrix1

    @initialization_matrix1.setter
    def initialization_matrix1(self, matrix):
        self.matrix = matrix
        count = 0
        list = self.matrix
        for item in list:
            count += len(item)
        sum_args = self.M_сol * self.N_str
        if count == sum_args:
            self.__initialization_matrix1 = np.array(self.matrix).reshape(
                self.M_сol, self.N_str)
        else:
            print(
                colored("Input error! Cannot convert an array of size:",
                        'red'), colored(int(count), 'red'),
                colored("to form:", 'red'), colored(int(self.M_сol), 'red'),
                colored('x', 'red'), colored(int(self.N_str), 'red'))
        #print(self.__initialization_matrix1)

    @property
    def initialization_matrix2(self):
        return self.__initialization_matrix2

    @initialization_matrix2.setter
    def initialization_matrix2(self, matrix):
        self.matrix = matrix
        count = 0
        list = self.matrix
        for item in list:
            count += len(item)
        sum_args = self.M_сol * self.N_str
        if count == sum_args:
            self.__initialization_matrix2 = np.array(self.matrix).reshape(
                self.M_сol, self.N_str)
        else:
            print(
                colored("Input error! Cannot convert an array of size:",
                        'red'), colored(int(count), 'red'),
                colored("to form:", 'red'), colored(int(self.M_сol), 'red'),
                colored('x', 'red'), colored(int(self.N_str), 'red'))
        #print(self.__initialization_matrix2)

    def is_identity(self):
        A = np.identity(self.N_str)
        B = self.__initialization_matrix1
        equal = np.allclose(A, B)
        print(equal)
        return self.__is_identity

    def is_square(self):
        A = self.M_сol
        B = self.N_str
        if A == B:
            print('True')
            return self.__is_square

    def is_zero(self):
        A = np.zeros((self.M_сol, self.N_str))
        B = self.__initialization_matrix1
        equal = np.allclose(A, B)
        print(equal)
        return self.__is_zero

    def is_diagonal(self):
        A = np.diagflat(self.__initialization_matrix1)
        ta = np.trace(A)
        B = self.__initialization_matrix1
        tb = np.trace(B)
        if fabs(ta) == fabs(tb):
            print('True')
            return self.__is_diagonal
        else:
            print('False')

    def transpose(self, matrix):
        self.M1 = self.__initialization_matrix1
        self.M2 = self.__initialization_matrix2
        if matrix == 'M1':
            M1 = np.transpose(self.M1)
            print(M1)
            return M1
        if matrix == 'M2':
            M2 = np.transpose(self.M2)
            print(M2)
            return M2

    @property
    def operations(self):
        return self.__operations

    @operations.setter
    def operations(self, operator):
        self.operator = operator
        M1 = self.__initialization_matrix1
        M2 = self.__initialization_matrix2
        if self.operator == '+':
            M = M1 + M2
        if self.operator == '-':
            M = M1 - M2
        if self.operator == '**':
            M = M1**M2
        if self.operator == '*':
            M = M1 * M2
        if self.operator == '/':
            M = M1 / M2
        print(M)

    
  
    
    def output(self):
        M = self.__initialization_matrix1
        a = []
        for a in M:
            for matrix in a:
                print(matrix, end=' ')
            print()
          
         

   


test = Matrix(3, 3)
test.initialization_matrix1 = [[2, 0, 0], [0, -158, 0], [0, 0, -38]]
test.initialization_matrix2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

#test.operations = '-'
#test.transpose('M1')
test.is_square()
#test.is_identity()
#test.is_zero()
#test.is_diagonal()
#test.output()


class HorizontalVector(Matrix):
    def __init__(self, M_сol, N_str):
        super().__init__(M_сol, N_str)


test2 = HorizontalVector(4, 3)
test2.initialization_matrix1 = [[2, 1, 1], [3, 3, 4], [5, 3, 8], [6, 9, 7]]

#test2.output()


class VerticalVector(Matrix):
    def __init__(self, M_сol, N_str):
        super().__init__(M_сol, N_str)


test3 = VerticalVector(4, 4)
test3.initialization_matrix1 = [[2, 1, 1, 768], [3, 3, 4, 123], [5, 3, 8, 135],
                                [6, 9, 7, 987]]
#test3.output
