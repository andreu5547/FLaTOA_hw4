import random
import time
import matplotlib.pyplot as plt


# Генерация случайного графа
def generate_random_graph(num_vertices, loop_chance, edge_chance):
    graph = []
    for u in range(num_vertices):
        for v in range(num_vertices):
            if u != v:
                if random.random() <= edge_chance:
                    graph.append((u, v))
        if random.random() <= loop_chance:
            graph.append((u, u))
    return graph


# Функция для поиска петель в графе
def find_loops(graph):
    loop_counts = {}
    for edge in graph:
        u, v = edge
        if u == v:
            loop_counts[edge] = loop_counts.get(edge, 0) + 1
    return loop_counts


# Запрос на ввод параметров графа
max_vertices = int(input("Введите максимальное количество вершин: "))
loop_chance = 0.6
edge_chance = 1
num_tests = int(input("Введите количество тестов для каждого количества вершин: "))

edges = []
avg_times = []

# Выполнение тестов для каждого количества ребер
for num_vertices in range(0, max_vertices + 1, max_vertices // 10):
    total_time = 0
    num_edges = 0
    # Выполнение тестов
    for i in range(num_tests):
        # Генерация случайного графа
        graph = generate_random_graph(num_vertices, loop_chance, edge_chance)

        # Вычисление количества ребер
        num_edges = len(graph)

        # Засечка времени выполнения
        start_time = time.time()

        # Поиск петель в графе
        loops = find_loops(graph)

        # Засечка времени выполнения
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time

    # Вычисление среднего времени выполнения
    avg_time = total_time / num_tests

    edges.append(num_edges)
    avg_times.append(avg_time)

# Построение графика зависимости времени выполнения от количества ребер
plt.plot(edges, avg_times, marker='o')
plt.xlabel('Количество ребер')
plt.ylabel('Среднее время выполнения (сек)')
plt.title('Зависимость времени выполнения от количества ребер')
plt.grid(True)
plt.show()
