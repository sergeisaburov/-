# ЧТЕНИЕ ФАЙЛА ------------------------- БУКВА r
# # f = open(r'test.txt')
# text = open(r'test.txt').read()
# создать файл test.txt в папке с запускаемым файлом
p=open('test.txt', 'r').read() #
print(p)
print(open('test.txt', 'r').read())
pr=open(r'test.txt').read()
print(pr)
print(open(r'test.txt').read())
pr=open(r'test.txt').close()
print(pr)
p=open(r'test.txt').close()
print(p)
# считаем количество символов(пробел тоже символ) в тексте
print(len((open(r'test.txt').read())))
# считаем количество символов(пробел тоже символ) в тексте но тут неоходимо в строку преобразовать или ставить запятые
print('В данном файле',len((open(r'test.txt').read())),'сиволов')
print('В данном файле: '+str(len((open(r'test.txt').read())))+' сиволов')