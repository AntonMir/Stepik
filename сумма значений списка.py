s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
e = int(s[4])
f = int(s[5])
if (a+b+c) == (d+e+f):
    print ('Счастливый')
elif (a+b+c) != (d+e+f):
    print ('Обычный')