from datetime import date
from VALID import opt, ns
import subprocess

while True:
    print("DETECTA-BISIESTOS")
    print("¿Que información desea ver?")
    print("A)AÑOS BISIESTOS Y NO BISIESTOS")
    print("B)SOLO AÑOS BISIESTOS")
    print("C)SOLO AÑOS NO BISIESTOS")
    op=opt(input("Introduzca aquí su opción: "),["A","B","C"])
    ran=input("Introduzca el rango de años separados por coma: ")
    años=ran.split(",")
    años.sort()
    for i in range(int(años[0]),(int(años[1]))+1):
        if i==9999:
            numdias=365
        else:
            D1=date(i,1,1)
            D2=date(i+1,1,1)
            numdias=(abs(D2-D1).days)
        if op==("A"):
            if numdias==366:
                print("El año",i,"es bisiesto")
            else:
                print("El año",i,"no es bisiesto")
        else:
            if op==("B") and numdias==366:
                print(i)
            elif op==("C") and numdias==365:
                print(i)
    conti=ns(input("¿Desa continuar: "))
    if conti==("n"):
        break
    subprocess.call(["cmd.exe","/C","cls"])
            
