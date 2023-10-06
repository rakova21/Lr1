#          С клавиатуры вводится текст, определить, сколько в нём
#       гласных, а сколько согласных. В случае равенства вывести на экран все
#       гласные буквы. Посчитать количество слов в тексте.

print('введите строку')
s = input()
w=s.split()
num=len(w)
print('слов в строке:', num)
count1 = 0
count2 = 0
glasn = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
soglasn = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
gl = ""
for i in range(len(glasn)):
    if glasn[i] in s:
        count1 += 1
        gl += glasn[i];
for j in range(len(soglasn)):
    if soglasn[j] in s:
        count2 += 1
print('количество гласных букв в строке:', count1)
print('количество согласных букв в строке:', count2)
if count2 == count1:
    print('гласные буквы: ',gl)

