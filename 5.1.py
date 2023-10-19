n = int(input("Кол-во строк: "))
a = []
for i in range(n):
  a += [input(f"Введите {i+1} город: ")]
city_povtor = [city for city in a if a.count(city) > 1]
print(len(city_povtor))
