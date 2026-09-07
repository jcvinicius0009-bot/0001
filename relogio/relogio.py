from datetime import datetime
from time import sleep
from rich import print


zero = [" ___ ","|   |", "|   |", "|___|"]


um = ["     ","    |","    |","    |"]


dois =[" ___ ", "    |"," --- ","|___ "]

tres = [" ___ ","    |"," ---|"," ___|"]

quatro = ["     ","|   |"," ---|","    |"]

cinco = [" ___","|    "," --- "," ___|"]

seis= [" ___ ","|    "," --- ","|___|"]

sete = ["  ___ ","    |","    |","    |"]

oito = [" ___ ","|   |","|---|","|___|"]

nove = [" ___ ","|   |"," ---|"," ___|"]

doispontos = ["    "," ** ","    "," ** "]








cor = input("Escolha uma cor para o relógio(em inglês): ")



cont = 0
while True:


    sleep(0.2)

    h= datetime.now()
    m= datetime.now()
    s= datetime.now()
    ms = (datetime.now())


    hora = h.strftime("%H")
    minuto = m.strftime("%M")
    segundo = s.strftime("%S")
    msegundo = str(ms.microsecond)


    #hora

    hora1 = hora[0]
    hora2 = hora[1]

    minuto1 = minuto[0]
    minuto2 = minuto[1]

    segundo1 = segundo[0]
    segundo2 = segundo[1]

    msegundo1 = msegundo[0]
    msegundo2 = msegundo[1]
    msegundo3 = msegundo[2]

    listageral = [hora1,hora2,"ponto",minuto1,minuto2,"ponto",segundo1,segundo2,"ponto",msegundo1,msegundo2,msegundo3]





    for i in range(0,4):
        print("")
        for j in listageral:
            
            match j:
                case "1":
                    print(f"[{cor}]{um[i]}[/]",end="")
                        
                case "2":
                    print(f"[{cor}]{dois[i]}[/]",end="")
                        
                case "3":
                    print(f"[{cor}]{tres[i]}[/]",end="")
                        
                case "4":
                    print(f"[{cor}]{quatro[i]}[/]",end="")
                        
                case "5":
                    print(f"[{cor}]{cinco[i]}[/]",end="")
                        
                case"6":
                    print(f"[{cor}]{seis[i]}[/]",end="")
                        
                case "7":
                    print(f"[{cor}]{sete[i]}[/]",end="")
                        
                case "8":
                    print(f"[{cor}]{oito[i]}[/]",end="")
                        
                case "9":
                    print(f"[{cor}]{nove[i]}[/]",end="")

                case "0":
                    print(f"[{cor}]{zero[i]}[/]",end="")

                case "ponto":
                    print(doispontos[i],end="")       


    cont += 1

    if cont == 1000:
        exit()
 