# Если файла test.txt нет, то создается, если есть то очищается
pr=open('test.txt','w')
pr.write('Привет малыш мой как дела?')
pr.close()
p=open('test.txt', 'r').read() #
print(p)
pr=open(r'test.txt').read()
print(pr)
print(type(pr), pr)
print(type(pr), p)