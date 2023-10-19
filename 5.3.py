input_str1 = input("Введите первую строку: ")
input_str2 = input("Введите вторую строку: ")
input_str1 = input_str1.replace(" ", "").lower()
input_str2 = input_str2.replace(" ", "").lower()
if set(input_str1) == set(input_str2):
    print("Эти строки являются анаграммами.")
else:
    print("Эти строки не являются анаграммами.")
