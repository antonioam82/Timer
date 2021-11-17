import time
from datetime import date
import os
from colorama import init, Back, Fore, Style
import calendar

init()

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ").lower()
    return(c)

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n
    

def pregunta(timer):
    AD=ns(input("¿Incluir ambos dias en el computo?(n/s): ").lower())
    if AD==("s"):
        timer=timer+1
    return(timer)   
        

def nums(a):
    while a<1 or a>9999:
        a=OKI(input("Año no valido: "))
    return a

def mes(m):
    while m>12 or m<1:
        m=OKI(input("Hay 12 meses,(introduce un valor entre 1 y 12 ambos incluidos): "))
    return(m)


def mess(a,m,d):
    M1=date(a,m,1)
    if a<9999 or m<12:
        if m==12:
            M2=date(a+1,1,1)
        else:
            M2=date(a,m+1,1)
        MD=abs(M1-M2)
        while d>MD.days or d<1:
            d=OKI(input("La cifra del día está fuera del rango para el mes escogido: "))
    else:
        while d>31:
            d=OKI(input("La cifra del día está fuera del rango para el mes escogido: "))
    return d

def meses(Fm):
    A=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    n=0
    for i in A:
        n+=1
        if int(Fm[1])==n:
            return i
            break
def semana(n):
    N=-1
    for i in("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"):
        N+=1
        if N==n:
            return(i)
            break

conti = "s"
while(conti == "s"):
    print(Back.BLUE+"            __________________________________________             ")
    print(Back.BLUE+"           /__   ____________________________________/             ")
    print(Back.BLUE+"             /  / __   _________   ______   ________               ")
    print(Back.BLUE+"            /  / |  | |  _   _  | | =====| |  ----_/               ")
    print(Back.BLUE+"           /__/  |__| |_| |_| |_| |______| |_|  \_\                ")
    print(Back.BLUE+"*******************************************************************")
    print(Back.RESET+"")
    print(Fore.GREEN+"-------------------------ESCOJA UNA OPCIÓN-------------------------")
    print("A) Calcular número de días entre una fecha y la actual.")
    print("B) Calcular número de días entre dos fechas.")  
    print("C) Conocer fecha a partir del número de días.")
    print("-------------------------------------------------------------------"+Fore.RESET)
    op=input("Introduzca aquí su opción: ").upper()
    
    while op!=("A") and op!=("B") and op!=("C"):
        op=input("Escriba solo \'A\',\'B\' o \'C\' segun su opción: ").upper()
    today=date.today()
    cal=ns(input("¿Desea ver calendarios?(n/s): ").lower())
    if op==("A"):
        a=nums(OKI(input("\nAño del suceso: ")))#;a=nums(OKI(a))
        m=mes(OKI(input("Mes del suceso: ")))#;m=mes(OKI(m))
        d=OKI(input("Dia del suceso: "));#d=OKI(d)
        Di=mess(a,m,d)
        D1=date(a,m,Di)
        if D1==(today):
            print(Fore.YELLOW+"Hoy es",D1)
        timer=abs(D1-today).days
        timer=pregunta(timer)
        if D1>today:
            print(Fore.YELLOW+"\nQuedan {} dias para la fecha escogida.".format(timer))
        else:
            print(Fore.YELLOW+"\nHan transcurrido {} dias desde la fecha escogida.".format(timer))
        print("({} semanas y {} dias).".format(str(int(timer/7)),timer%7))
        if cal==("s"):
            print(Fore.GREEN+"")
            CAL=calendar.c.prmonth(a,m)
            
    if op==("B"):
        a=nums(OKI(input("\nAño del primer suceso: ")))#;a=nums(OKI(a))
        m=mes(OKI(input("Mes del primer suceso: ")))#;m=mes(OKI(m))
        d=OKI(input("Día del primer suceso: "))#;d=OKI(d)
        Di=mess(a,m,d)
        D1=date(a,m,Di)
        Dist1=abs(D1-today).days
        a2=nums(OKI(input("\nAño del segundo suceso: ")))#;a2=nums(OKI(a2))
        m2=mes(OKI(input("Mes del segundo suceso: ")))#;m2=mes(OKI(m2))
        d2=OKI(input("Día del segundo suceso: "))#;d2=OKI(d2)
        Dii=mess(a2,m2,d2)
        D2=date(a2,m2,Dii)
        Dist2=abs(D2-today).days
        if (D1<=today and D2<=today) or (D1>=today and D2>=today):
            timer=abs(Dist1-Dist2)
            timer=pregunta(timer)
            if D1<=today and D2<=today:
                #print("")
                print(Fore.YELLOW+"\nTranscurrieron {} dias entre las dos fechas indicadas.".format(timer))
            else:
                print(Fore.YELLOW+"\nTranscurriran {} dias entre las dos fechas indicadas.".format(timer))
            print("({} semanas y {} dias).\n".format(str(int(timer/7)),timer%7))
        else:
            timer=(Dist1+Dist2)
            timer=pregunta(timer)
            print(Fore.YELLOW+"\nTranscurrirán {} dias entre las dos fechas indicadas.".format(timer))
            print("({} semanas y {} dias).\n".format(str(int(timer/7)),timer%7))
            
        if cal==("s"):
            print(Fore.GREEN+"")
            CAL=calendar.c.prmonth(a,m)
            print("")
            CAL2=calendar.c.prmonth(a2,m2)
        
    if op==("C"):
        num=OKI(input("\nEscriba el número de días: "))
        pas_fut=input("¿Al pasado (\'p\') o al futuro (\'f\'): ").lower()
        while pas_fut!=("p") and pas_fut!=("f"):
            pas_fut=input("Esciba solo \'p\'o\'f\'según su opción: ").lower()
        Dia1=date(1,1,1);HOY=int((today-Dia1).days)+1
        Dia_ult=date(9999,12,31);fut_hoy=int((Dia_ult-today).days)
        if pas_fut==("p"):
            while num>HOY:
                print(Fore.YELLOW+"La cantidad introducida es superior al numero de dias transcurridos, el máximo es de",HOY-1,"dias.")
                num=OKI(input("Prueba con otro número: "))
            dist=HOY-num
            dateo=date.fromordinal(dist)
            date_spl=str(dateo).split("-")
            mes_nom=meses(date_spl)
            week_day=(dateo).weekday()
            dia_semana=semana(week_day)
            print(Fore.YELLOW+"\nHace {} días era {} {} de {} de {}.".format(num,dia_semana,date_spl[2],mes_nom,date_spl[0]))
        if pas_fut==("f"):
            while num>fut_hoy:
                print(Fore.YELLOW+"La cantidad introducida es superior al numero de dias restantes, el máximo es de",fut_hoy,"dias")
                num=OKI(input("Prueba con otro número: "))
            dist=HOY+num
            dateo=date.fromordinal(dist)
            date_spl=str(dateo).split("-")
            mes_nom=meses(date_spl)
            week_day=(dateo).weekday()
            dia_semana=semana(week_day)
            print(Fore.YELLOW+"\nDentro de {} días será {} {} de {} de {}.".format(num,dia_semana,date_spl[2],mes_nom,date_spl[0]))
        if cal==("s"):
            print(Fore.GREEN+"")
            CAL=calendar.c.prmonth(int(date_spl[0]),int(date_spl[1]))

    print(Fore.RESET+"")
    conti=ns(input("\n¿Desea continuar?(n/s): ").lower())
    
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")
