text = input("Сонин текст: ")
upper_text = ''
text_next = True # начинаем с большой буквы
for i in text:
  if i.isalpha(): #ЕСЛИ БУКВА
    if text_next:
      upper_text += i.upper()
      text_next = False
    else:
      upper_text += i
  elif i in "!?.": # ЕСЛИ !.?
    upper_text += i
    text_next = True # означает что надо сделать следующую букву большую
  else: # все остальное
    upper_text += i
print(f"Исправленный текст: {upper_text} ")
# капец задача 2 дня решал.... и то пришлось использовать что не проходили isalpha 
# если что заметки это чтобы про это задачу не забывать очень интересная, чтобы если что можно было понять как она решается
