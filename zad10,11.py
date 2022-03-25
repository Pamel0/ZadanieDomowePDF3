# liczby = open("liczby.txt","w")
# for y in range(0,100):
#     if(y%4==0):           #sekwencja
#         liczby.write(str(y))   #genererowania (brakowało str)
#         liczby.write(" ")   #liczb podzielnych przez 4

liczby=open("liczby.txt","r")
print(liczby.read())
