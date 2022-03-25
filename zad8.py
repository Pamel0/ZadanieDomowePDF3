# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print("To jest ")
#         print(cos)
#         print(" co lubie ")
#         print(rzeczy[cos])
#
# to_lubie(slodycze="czekolada", rozrywka=['gry', 'filmy'])


def Zakupy( **CENA):
    ilosc=(CENA)
    suma= 0 #zapamiętać =0 inaczej nie ruszy
    for i in CENA: #może być cokolwiek zamiast i
      suma += CENA[i]
    return suma

print(Zakupy(masło=6.5, mleko=10, cukier=2.3))

# a = 10
# a += 5
# print(a)
