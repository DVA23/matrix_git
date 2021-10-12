#Work with matrix

Need to create class Matrix. It must has:
1.1 constructor list of lists;
1.2 Method __str__ that transform matrix into row
1.3 Method size w/o arguments that return tuples - numbers of rows and numbers of columns

2.1 Method __add__ that receive matrix with same size and return summ of two matrix
2.2 Method __mul__ that receive INT or FLOAT and return multiply matrix on scalar(mat * scalar)
2.3 Method __rmul__. The same method like __mul__ but it return multiply scalar on matrix (scalar * mat)

3.1 Added to method __add__ error message if size of two matrix is different
3.2 Realized transpose method
3.3 Added static method transposed