#print the data type of float type
a = 10.0
print(type(a))

#check the data type of changed form float type
b = 10.3    #float type은 반드시 소수점을 붙여야함, 그렇지 않으면 정수형으로 인식
c = 10.7
d = int(a) +int(b)
print(d)

e = "6.7"
f = float(e)
print(type(e))  #따옴표가 있으므로 e는 str type
print(f)    #f는 float type
#str을 int로 바꾸기 위해서는 먼저 float로 바꾼 후, int로 바꿔야 한다.