x = 'Day, mice. "Year" is a mistake!'
alf_en = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alf_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
z=''
a = []
b = ""
for i in range(len(x)):
    if x[i].isalpha():
        z+=x[i]
    if x[i]==" ":
        z+=x[i]
txt = z.split()
for i in range(len(txt)):
    total = len(txt[i])
    a.append(total)
y = x.split(" ")
for j in range(len(y)):
    for i in range(len(y[j])):
        for k in range(len(alf_en)//2):
            if y[j][i].isalpha() and y[j][i] == alf_en[k]:
                b+=(alf_en[k+a[j]])

            if y[j][i].isalpha() and y[j][i] == alf_EN[k]:
                b+=(alf_EN[k+a[j]])
        if not y[j][i].isalpha():
            b+=(y[j][i])




print(b)