import requests
import threading
from tkinter import *
from time import *

def update():
while 1:
        sleep(1)
        #ver tabela de letras que correspodem ao formato do relógio
        #https://www.programiz.com/python-programming/datetime/strftime
        time_string = strftime("%H:%M:%S")
        time_label.config(text=time_string)
        
            
        #date_string = strftime("%d %B %Y") dia mes ano
        date_month = strftime("%B")
        months_eng =   ["January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"]
        meses_pt = ["Janeiro",
                    "Fevereiro",
                    "Março",
                    "Abril",
                    "Maio",
                    "Junho",
                    "Julho",
                    "Agosto",
                    "Setembro",
                    "Outubro",
                    "Novembro",
                    "Dezembro"]
        
        months_day_len = len (months_eng)
        
        for f in range (0,months_day_len):
            if date_month == months_eng[f]:
                date_month = meses_pt[f]
                
        date_string = strftime("%d ") + date_month + strftime(" %Y")
        
        date_label.config(text=date_string)

def atualiza_dados():
    while 1:
        sleep(2)
        resposta = requests.get('http://192.168.1.1/')
        dados = resposta.text
        
        if resposta.status_code==200:
            print("OK") #se diferente de 200 erro de ligação
            connection.config(text="OK")
        else:
            print(resposta.status_code) #se diferente de 200 erro de ligação
            connection.config(text="ERROR")
        
        dados_separados = dados.split("e")  
        temp = dados_separados[0] + "ºC"
        temperatura.config(text=temp)
        print("temperatura ", temp)
        hum = dados_separados[1] + "%"
        #hum = "%"
        print("humidade    ", hum)
        humidade.config(text=hum)


window = Tk()



window.geometry("420x520")
window.title("Leitura de Dados")

icon = PhotoImage(file='ico.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")


hotImage = PhotoImage(file='temperatura.png')
hotLabel = Label(image=hotImage)
hotLabel.grid(row=0,column=0,padx=10,rowspan=1)

humImage = PhotoImage(file='humidade.png')
humLabel = Label(image=humImage)
humLabel.grid(row=0,column=1, padx=10, pady=10,rowspan=1)


label_temperatura = Label(window,text="temperatura",font=("Ink Free",20))
label_temperatura.grid(row=4,column=0,columnspan=1, sticky=N, padx=10)

label_humidade = Label(window,text="humidade",font=("Ink Free",20))
label_humidade.grid(row=4,column=1,columnspan=1, sticky=N, padx=10)

temperatura = Label(window,font=("Ink Free",30))
temperatura.grid(row=5,column=0,columnspan=1, sticky=N, padx=10, pady=10)

humidade = Label(window,font=("Ink Free",30))
humidade.grid(row=5,column=1,columnspan=1, sticky=N, padx=10, pady=10)

date_label = Label(window,font=("Ink Free",30))
date_label.grid(row=6,column=0,columnspan=2, sticky=N, padx=10, pady=10)

connection = Label(window,font=("Ink Free",30))
connection.grid(row=7,column=0,columnspan=2, sticky=N, padx=10, pady=10)

time_label = Label(window,font=("Ink Free",30))
time_label.grid(row=8,column=0,columnspan=2, sticky=N, padx=10, pady=10)

threading.Thread(target=atualiza_dados).start()
threading.Thread(target=update).start()

window.mainloop()
