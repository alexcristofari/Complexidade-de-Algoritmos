import time
import numpy as np
import matplotlib.pyplot as plt

def multiply_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Os vetores devem ter o mesmo tamanho")
    result = [vector1[i] * vector2[i] for i in range(len(vector1))]
    return result

def multiply_vector_matrix(vector, matrix):
    if len(vector) != len(matrix):
        raise ValueError("O tamanho do vetor deve ser igual ao número de linhas/colunas da matriz")
    result = [sum(vector[j] * matrix[j][i] for j in range(len(vector))) for i in range(len(matrix))]
    return result

def multiply_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("As matrizes devem ter o mesmo tamanho")
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    return result

def generate_random_vector(size):
    return [np.random.randint(1, 10) for _ in range(size)]

def generate_random_matrix(size):
    return [[np.random.randint(1, 10) for _ in range(size)] for _ in range(size)]

def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time

sizes = [500]

vector_times = []
vector_matrix_times = []
matrix_times = []

for size in sizes:
    vector1 = generate_random_vector(size)
    vector2 = generate_random_vector(size)
    matrix = generate_random_matrix(size)

    vector_time = measure_execution_time(multiply_vectors, vector1, vector2)
    vector_times.append(vector_time)

    vector_matrix_time = measure_execution_time(multiply_vector_matrix, vector1, matrix)
    vector_matrix_times.append(vector_matrix_time)

    matrix_time = measure_execution_time(multiply_matrices, matrix, matrix)
    matrix_times.append(matrix_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, vector_times, marker='o', label='Multiplicação de Vetores')
plt.plot(sizes, vector_matrix_times, marker='o', label='Multiplicação de Vetor por Matriz')
plt.plot(sizes, matrix_times, marker='o', label='Multiplicação de Matrizes')
plt.title('Tempos de execução dos algoritmos')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo de execução (segundos)')
plt.xscale('log')
plt.yscale('log')
plt.xticks(sizes, sizes)
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
