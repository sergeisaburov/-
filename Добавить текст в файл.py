# ЧТЕНИЕ ФАЙЛА ------------------------- БУКВА a
# открываем файл
f=open('ttt.txt','a')
#  дозаписываем в файл текст
f.write(' _запись в файл_ ')
print(open('ttt.txt', 'r').read())
#  закрываем файл
f.close()
# Все заработало
print('В данном файле: '+str(len((open(r'ttt.txt').read())))+' сиволов')
print('В данном файле',len((open(r'ttt.txt').read())),'сиволов')