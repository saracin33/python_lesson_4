# ДЗ №4
import random
list_names = ['Женя', 'Стас', 'Варя', 'Лина', 'Петя', 'Саша', 'Вася', 'Иван', 'Маша', 'Вова', 'Миша', 'Аня', 'Тома', 'Егор', 'Гриша', 'Клава', 'Зина', 'Яков', 'Кузя', 'Илья']
new_list_names = random.choices(list_names, k=100)
print(new_list_names)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F:
# Не знаю правильно или нет, но выполнил этот пункт взяв за основу алгоритм из ДЗ №3
dict_temp = {}
def frequent_name():
    for i in range(len(new_list_names)):
        sum_temp = 0
        word = new_list_names[i]
        for a in range(len(new_list_names)):
            if word == new_list_names[a]:
                sum_temp += 1
        dict_temp[word] = sum_temp
frequent_name()
new_list = list(dict_temp.items())
new_list.sort(key = lambda i: i[1],reverse = True)
print(new_list[:1])

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
dict_temp = {}
letter_list=list(map(lambda x: x[0],new_list_names))
for letter in letter_list:
     if (letter in dict_temp):
        dict_temp[letter] += 1
     else:
        dict_temp[letter] = 1
new_list = list(dict_temp.items())
new_list.sort(key = lambda i: i[1])
print(new_list[0])