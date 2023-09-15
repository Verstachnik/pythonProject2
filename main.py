x = "Блажен, кто верует, тепло ему на свете!"
x1 = "To be, or not to be, that is the question!"
x2 = "Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг."
x3 = "Hawnj pk swhg xabkna ukq nqj."
alf_en = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alf_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
y2 = "абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"
y1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФЦЧЩШЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФЦЧШЩЪЫЬЭЮЯ"
n=int(input())
z=""
b=""
a = ""
c = ""
for i in range(len(x)):
    if x[i].isalpha() and x[i].islower():
        for j in range(len(y2)//2):
            if x[i]== y2[j]:
                z+=y2[j+n]
    if x[i].isalpha() and x[i].upper():
            for v in range(len(y1)//2):
                if x[i]==y1[v]:
                    z+=y1[v+n]
    if not x[i].isalpha():
        z+=x[i]
print(z)

for i in range(len(x1)):
    if x1[i].isalpha() and x1[i].islower():
        for j in range(len(alf_en)//2):
            if x1[i]== alf_en[j]:
                b+=alf_en[j+n]
    if x1[i].isalpha() and x1[i].upper():
        for v in range(len(alf_EN)//2):
            if x1[i]==alf_EN[v]:
                b+=alf_EN[v+n]            
    if not x1[i].isalpha():
        b+=x1[i]
print(b)

for i in range(len(x2)):
    if x2[i].isalpha() and x2[i].islower():
        for j in range(len(y2)//2):
            if x2[i]== y2[j]:
                a+=y2[j-n]
    if x2[i].isalpha() and x2[i].upper():
        for v in range(len(y1)//2):
            if x2[i]==y1[v]:
                a+=y1[v-n]            
    if not x2[i].isalpha():
        a+=x2[i]
print(a)

for i in range(len(x3)):
    if x3[i].isalpha() and x3[i].islower():
        for j in range(len(alf_en)//2):
            if x3[i]== alf_en[j]:
                c+=alf_en[j-n]
    if x3[i].isalpha() and x3[i].upper():
        for v in range(len(alf_EN)//2):
            if x3[i]==alf_EN[v]:
                c+=alf_EN[v-n]
    if not x3[i].isalpha():
        c+=x3[i]
print(c)