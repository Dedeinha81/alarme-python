
import tkinter as tk
from tkinter import filedialog
from playsound import playsound
import time
from datetime import datetime

# Função para tocar o alarme
def tocar_alarme(som_alarme):
    playsound(som_alarme)

# Função para configurar o alarme
def configurar_alarme():
    hora = int(entry_hora.get())
    minuto = int(entry_minuto.get())
    som = som_alarme.get()
    label_status.config(text=f'Alarme configurado para {hora}:{minuto} com som {som}')
    alarme(hora, minuto, som)

# Função para adiar o alarme (Snooze)
def snooze_alarme(som_alarme):
    label_status.config(text="Alarme adiado por 5 minutos!")
    time.sleep(5 * 60)  # Adia por 5 minutos
    tocar_alarme(som_alarme)

# Função principal que verifica o horário
def alarme(hora, minuto, som_alarme):
    while True:
        now = datetime.now()
        if now.hour == hora and now.minute == minuto:
            tocar_alarme(som_alarme)
            user_input = input("Digite 'snooze' para adiar o alarme: ")
            if user_input.lower() == 'snooze':
                snooze_alarme(som_alarme)
            break
        time.sleep(30)  # Verifica a cada 30 segundos

# Função para escolher o som do alarme
def escolher_som():
    arquivo_som = filedialog.askopenfilename(title="Escolher Som", filetypes=(("Arquivos MP3", "*.mp3"), ("Todos os arquivos", "*.*")))
    label_som.config(text=f'Som escolhido: {arquivo_som}')
    som_alarme.set(arquivo_som)

# Interface gráfica
root = tk.Tk()
root.title("Alarme com Snooze e Escolha de Som")

# Labels e entradas para a hora e minuto
label_hora = tk.Label(root, text="Hora (0-23):")
label_hora.pack()

entry_hora = tk.Entry(root)
entry_hora.pack()

label_minuto = tk.Label(root, text="Minuto (0-59):")
label_minuto.pack()

entry_minuto = tk.Entry(root)
entry_minuto.pack()

# Botão para escolher o som
button_som = tk.Button(root, text="Escolher Som", command=escolher_som)
button_som.pack()

# Exibe o nome do som escolhido
label_som = tk.Label(root, text="Nenhum som escolhido")
label_som.pack()

# Variável para armazenar o caminho do som
som_alarme = tk.StringVar()
som_alarme.set("alarme.mp3")  # Valor padrão

# Botão para configurar o alarme
button_configurar = tk.Button(root, text="Configurar Alarme", command=configurar_alarme)
button_configurar.pack()

# Status do alarme
label_status = tk.Label(root, text="Configuração do alarme")
label_status.pack()

root.mainloop()
