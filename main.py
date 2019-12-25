import numpy as np
from termcolor import colored
from math import fabs


class Matrix():
    def __init__(self, M_сol, N_str):
        self.M_сol = M_сol
        self.N_str = N_str
        self.__initialization_matrix = None
        self.__operations = None
        self.__transpose = None
        self.__is_square = None
        self.__is_identity = None
        self.__is_zero = None
        self.__is_diagonal = None
        self.__output = None

   
    def initialization_matrix(self, matrix):
        self.matrix = matrix
        count = 0
        list = self.matrix
        for item in list:
            count += len(item)
        add_args = self.M_сol * self.N_str
        if count == add_args:
             self.__initialization_matrix = np.array(self.matrix).reshape(
                self.M_сol, self.N_str)
        else:
            print(
                colored("Input error! Cannot convert an array of size:",
                        'red'), colored(int(count), 'red'),
                colored("to form:", 'red'), colored(int(self.M_сol), 'red'),
                colored('x', 'red'), colored(int(self.N_str), 'red'))
        return  self.__initialization_matrix

    def is_identity(self):
        A = np.identity(self.N_str)
        B =  self.__initialization_matrix
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
        B =  self.__initialization_matrix
        equal = np.allclose(A, B)
        print(equal)
        return self.__is_zero

    def is_diagonal(self):
        A = np.diagflat( self.__initialization_matrix)
        ta = np.trace(A)
        B =  self.__initialization_matrix
        tb = np.trace(B)
        if fabs(ta) == fabs(tb):
            print('True')
            return self.__is_diagonal
        else:
            print('False')

    def transpose(self, matrix):
        self.matrix = matrix
        if matrix == 'M1':
            M1 = np.transpose(self.M1)
            print(M1)
            return M1

    def operations(self, operator, M2):
        self.operator = operator
        M1 =  self.__initialization_matrix
        self.M2 = M2
        if self.operator == '+':
            M = M1 + M2
        if self.operator == '-':
            M = M1 - M2
        if self.operator == '**':
            M = M1**M2
        if self.operator == '*':
            M = M1.dot(M2)
        if self.operator == '/':
            M = M1 / M2
        print(M)
        return self.__operations

    def output(self):
        M = self.__initialization_matrix
        for row in M:
            for matrix in row:
                print(matrix, end=' ')
            print()


class HorizontalVector(Matrix):
    def __init__(self, N_str, M_col = None):
      super().__init__(N_str, M_col)   

    
    def initialization_matrix(self, matrix):
      self.matrix = matrix
      count = 0
      list = self.matrix
      for item in list:
          count += len(str(item))
      column = self.M_сol    
      if count == column:
        self.__initialization_matrix = np.array(self.matrix).reshape( 1 , self.M_сol)
        print(self.__initialization_matrix)
        return self.__initialization_matrix
      else:
        print(colored("Vector dimension =", "red"), colored(int(count), "red"), colored(". Error! enter the correct vector dimension.", 'red'))
  
class VerticalVector(Matrix):
    def __init__(self, M_col, N_str = None):
      super().__init__(N_str, M_col)   

    
    def initialization_matrix(self, matrix):
      self.matrix = matrix
      count = 0
      list = self.matrix
      for item in list:
          count += len(str(item))
      string = self.N_str    
      if count == string:
        self.__initialization_matrix = np.array(self.matrix).reshape( self.N_str, 1 )
        print(self.__initialization_matrix)
        return self.__initialization_matrix
      else:
        print(colored("Vector dimension =", "red"), colored(int(count), "red"), colored(". Error! enter the correct vector dimension.", 'red')) 


test = Matrix(3, 3)
test.initialization_matrix([[16, 2, 2], [2, 2, 2], [2, 2, 2]])

test.operations('*', [[2, 2, 2], [2, 2, 2], [2, 2, 2]])
test.transpose([[2, 0, 0], [0, -158, 0], [0, 0, -38]])
#test.is_square()
#test.is_identity()
#test.is_zero()
#test.is_diagonal()
#test.output()

test3 = VerticalVector(4)
test3.initialization_matrix([2, 1, 1, 5])

test2 = HorizontalVector(4)
test2.initialization_matrix([2, 1, 1, 5])
