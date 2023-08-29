print("Modus Ponens")

clima=int
while True :
    clima = int(input("Esta lloviendo? (1 Si, 0 No): "))
    if clima==1:
        break
    if clima==0:
        break
    if clima!=1 and clima!=0:
        print("Inserte un valor valido")

# Modo de Inferencia
if clima == 1:
    print("Entonces usa paraguas")
else:
    print("Entonces no uses paraguas")