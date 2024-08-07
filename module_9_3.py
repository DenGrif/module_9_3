first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Cборка 1: zip
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# 2. Сборка 2: range и len
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

# Пример выполнения кода:
print(list(first_result))
print(list(second_result))