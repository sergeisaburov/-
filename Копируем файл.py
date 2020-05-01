# ДЛЯ ТЕКСТОВЫХ ФАЙЛОВ
failname1 = input('какой текстовый файл скопировать(не картинку):')
failname2 = 'copy_'+ failname1

file1 = open(failname1,'r')
file2 = open(failname2,'w')

file2.write(file1.read())

file1.close()
file2.close()

# # # РАБОТАЕТ

# ДЛЯ любых ФАЙЛОВ
failname1 = input('какой ЛЮБОЙ файл скопировать(даже картинку):')
failname2 = 'copy_'+ failname1

file1 = open(failname1,'rb')
file2 = open(failname2,'wb')

file2.write(file1.read())

file1.close()
file2.close()

# РАБОТАЕТ