print("Modus Tollens")

paraguas=int
while True :
    paraguas = int(input("Esta usando paraguas? (1 Si, 0 No): "))
    if paraguas==1:
        break
    if paraguas==0:
        break
    if paraguas!=1 and paraguas!=0:
        print("Inserte un valor valido")

# Modo de Inferencia
if paraguas == 1:
    print("Entonces esta lloviendo")
else:
    print("Entonces no esta lloviendo")