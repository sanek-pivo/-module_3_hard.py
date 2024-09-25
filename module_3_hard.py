# Создаём функцию для данных строк и чисел
def calculate_structure_sum(data_structure):
    summa = 0
    # Создаем цикла 1 summa для name и names
    if isinstance(data_structure, dict):
        for name, names in data_structure.items():
            summa += calculate_structure_sum(name)
            summa += calculate_structure_sum(names)
            # создаем цикл 2 список,кортэж,множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
            # создаем цикл 3 целое число и число с плавающей запятой
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
        # создаем цикл 4 задействовав функцию len
    elif isinstance(data_structure, str):
        summa += len(data_structure)
        return summa # возврат из функции значения summa


data_structure = [    # данные взятые из условия задачи
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # вывод результата программы