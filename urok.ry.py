try:
    with open('gggg.txt', 'a+') as file:
        file.write('Viva la viva')
        file.seek(0)
        s = file.readlines()
        print(s)
except FileNotFoundError:
    print('Невозможно открыть файл')
except:
    print('Ошибка при рабте с файлом')

finally:
    print(file.closed)
