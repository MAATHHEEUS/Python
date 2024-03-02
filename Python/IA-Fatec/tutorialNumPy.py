# Tutorial NumPy
print("Tutorial NumPy")

# pip install numpy #- Instalar numpy
import numpy

# Array dimensões
arr = numpy.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

# Array copy VS view
arr = numpy.array([1, 2, 3, 4, 5])
copy = arr.copy()
arr[0] = 42

print(arr)
print(copy)

view = arr.view()
arr[0] = 42

print(arr)
print(view)

# Redimensionar
arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

# Ordenação
arr = numpy.array([3, 2, 0, 1])

print(numpy.sort(arr))

# Criando filtro 
arr = numpy.array([41, 42, 43, 44])

filter_arr = arr > 42 # Se for maior q 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)