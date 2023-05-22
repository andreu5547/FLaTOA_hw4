import subprocess

# Считывание графа из текстового файла
def read_graph_from_file(filename):
    graph = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                u, v = map(int, line.split())
                graph.append((u, v))
    return graph

# Функция для поиска петель в графе
def find_loops(graph):
    loop_counts = {}
    for edge in graph:
        u, v = edge
        if u == v:
            loop_counts[edge] = loop_counts.get(edge, 0) + 1
    return loop_counts

# Ввод названия файла с графом
filename = input("Введите название файла с графом: ")

# Загрузка графа из файла
graph = read_graph_from_file(filename)

# Запрос на ввод пользователя для определения ориентированности ребер
is_directed = input("Сделать ребра направленными? (y/n): ").lower() == 'y'

# Создание кода Graphviz в формате DOT
dot_code = 'digraph G {\n' if is_directed else 'graph G {\n'
for edge in graph:
    u, v = edge
    edge_str = f'{u} {"->" if is_directed else "--"} {v}'
    dot_code += f'    {edge_str};\n'
dot_code += '}'

# Сохранение кода Graphviz в файл DOT
dot_file = 'graph.dot'
with open(dot_file, 'w') as file:
    file.write(dot_code)

# Вызов Graphviz из системы для визуализации
output_file = 'graph_output.png'
subprocess.call(['dot', '-Tpng', dot_file, '-o', output_file])
print(f"Граф успешно выведен в файл {output_file}.")

# Поиск петель в графе
loops = find_loops(graph)
if loops:
    print("Найдены петли:")
    for edge, count in loops.items():
        print(f"Ребро {edge[0]} - количество петель: {count}")
else:
    print("Петли не найдены.")
