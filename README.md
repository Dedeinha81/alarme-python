Como o Código Funciona

O código foi desenvolvido para ser simples, mas com uma lógica bem interessante. Ele verifica continuamente se o horário atual bate com o horário configurado no alarme, e quando isso acontece, toca o som escolhido. O recurso de Snooze é chamado quando você decide adiar o alarme por 5 minutos.

Explicação do Código

Importação das bibliotecas:

tkinter e filedialog para a interface gráfica.

playsound para tocar o som do alarme.

time e datetime para controlar o tempo e verificar quando o alarme deve tocar.

Função principal do alarme: A função alarme() fica rodando e verificando a cada 30 segundos se o horário do alarme chegou. Quando o horário é alcançado, o som é tocado.

Função de Snooze: Quando você digita "snooze", o alarme é adiado por 5 minutos.



Código do Projeto

Escolher o som: A função escolher_som() permite que você selecione um arquivo MP3 para ser tocado quando o alarme disparar.

Configuração do alarme: A função configurar_alarme() pega os valores de hora e minuto digitados e começa a verificar o horário continuamente.

Interface gráfica: Usei o Tkinter para criar uma interface simples onde você pode configurar o alarme e selecionar o som.



Como Rodar o Código
Certifique-se de ter o Python 3.x instalado no seu computador.

Clone o repositório ou baixe o código.

Instale as dependências com o seguinte comando:

pip install playsound

Execute o script:

python alarme.py

A interface gráfica vai aparecer, e você poderá configurar o alarme, escolher o som e ajustar o horário.
