import pickle
books1 = ['ddfdf','dfdf',200]
books2 =['ccccc','vvvvv',250]
books3 =['aaaa','ssss', 500]

try:
    with open('out.bin', 'wb') as file:
        pickle.domp(books1,file)
        pickle.domp(books2, file)
        pickle.domp(books3,file)
except:
    print('Ошибка')




