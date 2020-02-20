

"""
first function to print the grid
"""
def print_grid(matrix):
    for i in range(9):
        for j in range(9):
            print(matrix[i][j]);

def found_in_row(matrix, row, value_expected):
    for i in range(9):
        if matrix[row][i]==expected:
            return True
        else:
            return False;

def foud_in_column(matrix, column, value_expected):
    for i in range(9):
        if matrix[i][column]==expected:
            return True
        else:
            return False;

def found_in_box(matrix, value_expected):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == value_expected:
                return True;
            else:
                return False;
