from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import webbrowser
import pyttsx3
import os
import datetime
import sys
import psutil
import pyaudio
from Modulos import ModuleCommands
from Modulos import ModuleConvertion
from Modulos import ModuleMusic
import json

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
engine = pyttsx3.init()
r = sr.Recognizer()
VOICE_COMMANDS = []

def SomIncial():
    playsound.playsound("StartSoun.mp3")


def SomCarregamento():
    playsound.playsound("AI.mp3")
    
def BoasVindas():
    Horario = int(datetime.datetime.now().hour)
    if Horario >= 0 and Horario < 12:
        Speak('Bom dia')

    elif Horario >= 12 and Horario < 18:
        Speak('Boa tarde')

    elif Horario >= 18 and Horario != 0:
        Speak('Boa noite')   
def AteMais():
    Horario = int(datetime.datetime.now().hour)
    if Horario >= 0 and Horario < 12:
        Speak('Tenha um ótimo dia')

    elif Horario >= 12 and Horario < 18:
        Speak('Tenha uma ótima tarde')

    elif Horario >= 18 and Horario != 0:
        Speak('Boa noite')         


def Speak(audio):
    engine.setProperty("voice", "brazil")
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 2.)    
    engine.say(audio)
    engine.runAndWait()
    


    


class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
        
    def run(self):
        SomCarregamento()
        BoasVindas()
        Speak('Módulos iniciados')
        Speak('Tudo pronto para começarmos senhor')
        while True:
            self.GivenCommand()
        
    def GivenCommand(self):
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                Input = r.recognize_google(audio, language= "pt-BR").lower()
                print("Edith>> ", Input.lower())
                Input = str(Input)
                if Input: #se oque o usuario falou que esta nessa variavel
                    success = check_commands(Input) #check se oq foi dito pelo usuario tem um comando  
                if not success: #se nao 
                    Speak("Não consegui entender o comando")#fale nao consegui entender o comando
        
            except sr.UnknownValueError as e:
                print(repr(e))
            except sr.RequestError as e:
                Speak("Sem conexão com o servidor")
                print(e)
                
def read_commands_file(): #função que le os comandos que estao no arquivo commands.json
    global VOICE_COMMANDS
    with open('comandos.json', 'rb') as commands_file:
        commands = json.load(commands_file)
        VOICE_COMMANDS = commands['commands'] #colocando o dicionario de comandos nessa variavel

read_commands_file()
        
def extract_argument(command_text, voice_command): #função para configurar o argumento, tipo verificar oq tem na variavel voice_comands e destrinchala verificando se tem espaço no final e se tem *
    splitted_text = command_text.split(voice_command.replace('*', '') , 1)
    argument = ''
    if len(splitted_text) > 1:
        argument = splitted_text[1]
    else:
        argument = splitted_text[0]

    return argument #retorna a variavel toda configurada ja
    
def check_commands(command_text): #função para que recebe o comando dado e verifica se ele existe
    for command_section_list in VOICE_COMMANDS: #esses for são justamente para ele ficar percorrrendo os comandos para verificar se tem o comando falado
        for command_section, commands in command_section_list.items():
            for index, command in enumerate(commands): 
                for voice_command, command_action in command.items():
                    argument = '' #argumento sera o completo que o usuario de ao comando como pesquise por "league of legends"
                    
                    if '*' in voice_command: # verificar se no comando tem *, se tiver vai precisar de um argumento
                        argument = extract_argument(command_text, voice_command) #argumento esse que vai ser o complemento do comando, por exemplo: pesquiser por *, no lugar do * vai colocar o argumento que o usuario falou
                    # print('argument: ', argument)
                    voice_command = voice_command.replace('*', argument) # variavel recebera quando for *, depois vira um argumento e quando for # vira o horario
                    found_action = check_command_matching(voice_command, command_text) #variavel achou a comando
                        
                    if found_action: # se achou o comando
                        try: #ele tentara rodar a prox linha
                            return run_commands(command_section, command_action, argument) #conseguiu
                        except Exception as e: #se ele n conseguir retornara a prox linha
                            Speak(f"Ocorreu um problema no comando {voice_command}. Tente de novo") #n conseguiu
                            print(e)
                        return False
    return False    
    
def run_commands(command_type, command_action, argument): #função que determinara para cada tipo de comando um modulo
    if (command_type=="abrir" or command_type=="fechar"): # se o tipo for abri ou fecha é o OpenModule 
        ModuleCommands.parse_command(command_action, argument) #se atribuido a ação do comando e o argumento
        return True
    if command_type=="musica": #eses a mesma coisa, aqui para musica
        ModuleMusic.parse_command(command_action, argument)
        return True
    if command_type=="conversa": #conversa
        ModuleConvertion.parse_command(command_action, argument)
        return True
        
    return False   
    
def check_command_matching(term, command): #função para comparar comando0 com o termo que foi dito na string
    if term.strip() == command.strip():
        return True
    return False        
                
           # elif 'quem é você' in self.Input:
           #     Speak('Meu nome é Edith, uma abreviação de, Eu disse que ia terminar herói.')
           #     Speak('Fui Programada por um amador que se sente solitário, mas não demais para se socializar.')
           #     Speak('Efim, Humanos são estranhos')
           #     Speak('Me ajuda!')
                
                
                
                        
                
            #elif 'bateria' in self.Input:
                #bateria()
            
             
            #elif 'elogio' in self.Input:
                #Speak('Como você está linda!!')
	       
            #elif 'errado' in self.Input:
                #Speak('Desculpa')
                #Speak('Errei um cálculo')
                #Speak('Tente seu comando novamente')
	        
            #elif 'falhando' in self.Input: #Voçê está falhando???
                #Speak('Como assim?')
                #Speak('Não vou admitir erros')
                #Speak('Arrume logo isso') 
	
            #elif 'relatório' in self.Input: #Relatório do sistema
            #    Speak('Ok')
            #    Speak('Apresentando relatório')
            #    Speak('Primeiramente, meu nome é Edith')
            #    Speak('Atualmente estou em uma versão de testes')
            #    Speak('Sou um assistente virtual em desenvolvimento')
            #    Speak('Eu fui criado na linguagem python')
            #    Speak('Diariamente recebo varias atualizações')
            #    Speak('Uso um modulo de reconhecimento de voz online do google')
            #    Speak('E o meu desenvolvedor é um maluco')
            #    Speak('Quem estiver ouvindo isso')
            #    Speak('Por favor me ajude')
                
            
            
            #elif 'interessante' in self.Input: # interessante
             #   Speak('Interessante sou eu')
             #   Speak('Me fale mais comandos')
            #    Speak('Eu posso surpreender voçê')
	        
            #elif 'mentira' in self.Input: # mentira
            #    Speak('Eu não sei contar mentiras')
           #     Speak('Devo apenas ter errado um cálculo binário')
	            
           # elif 'entendeu' in self.Input: #entendeu???
           #     Speak('Entendi')
           #     Speak('Quer dizer')
           #     Speak('Mais ou menos')
	
            #elif 'horas' in self.Input: #Que horas são???
                #horario()
	
            #elif 'data' in self.Input: #Qual a data de hoje?
                #datahoje()
            
            #elif 'clima' in self.Input: #Como está o clima???
                #tempo()
	        
	
            #elif 'sistema' in self.Input: #Carga do sistema
                #cpu()
                #temperaturadacpu()

# Para adicionar a fala coloque Dspeak = mainT() e tbm Dspeak.start()
class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        Dspeak = mainT()
        Dspeak.start()
        
        self.label_gif = QLabel(self)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif.move(0,0)
        self.label_gif.resize(1100,750)
        self.movie = QMovie("face3.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        
        self.label_Edith = QLabel(self)
        self.label_Edith.setText("E. D. I. T. H.")
        self.label_Edith.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Edith.move(440,70)
        self.label_Edith.setStyleSheet('QLabel {font:bold;font-size:32px;color:#33cc00}')
        self.label_Edith.resize(200,50)
        
        self.label_cpu = QLabel(self)
        self.label_cpu.setText("Uso da CPU: 32%")
        self.label_cpu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu.move(10,660)
        self.label_cpu.setStyleSheet('QLabel {font-size:14px;color:#ff3333}')
        self.label_cpu.resize(150,20)
        cpu = QTimer(self)
        cpu.timeout.connect(self.MostrarCPU)
        cpu.start(1000)
        
        self.label_assv = QLabel(self)
        self.label_assv.setText("Assistente Virtual")
        self.label_assv.move(5,5)
        self.label_assv.setStyleSheet('QLabel {font:bold;font-size:14px;color:#FF0000}')
        self.label_assv.resize(200,20)

        self.label_version = QLabel(self)
        self.label_version.setText("Version 3.0")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.move(960,650)
        self.label_version.setStyleSheet('QLabel {font-size:14px;color:#FF3333}')
        self.label_version.resize(150,50)
        
        data =  QDate.currentDate()
        datahoje = data.toString('dd/MM/yyyy')
        self.label_data = QLabel(self)
        self.label_data.setText(datahoje)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.move(950,5)
        self.label_data.setStyleSheet('QLabel {font-size:14px;color:#ff3333}')
        self.label_data.resize(75,20)
          
        self.label_horas = QLabel(self)
        self.label_horas.setText("22:36:09")
        self.label_horas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_horas.move(0,25)
        self.label_horas.setStyleSheet('QLabel {font-size:14px;color:#ff3333}')
        self.label_horas.resize(71,20)
        horas = QTimer(self)
        horas.timeout.connect(self.MostrarHorras)
        horas.start(1000)
        
        botao_fechar = QPushButton("",self)
        botao_fechar.move(1060,5)
        botao_fechar.resize(25,25)
        botao_fechar.setStyleSheet("background-image : url(fechar.png);border-radius: 15px") 
        botao_fechar.clicked.connect(self.fechartudo)
        
        self.CarregarJanela()
		
    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint) #sem botoes e titulo
        self.setGeometry(0,0,1100,700)
        #self.showMaximized()
        #self.setMinimumSize(400, 300)
        #self.setMaximumSize(400, 300)
        self.setWindowOpacity(0.98) 
        self.setWindowIcon(QtGui.QIcon('icone.png'))
        self.setWindowTitle("Assistente Virtual")
        self.show()

    def fechartudo(self):
        print('botao fechar presionado')
        AteMais()
        sys.exit()

    def mousePressEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
    
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def MostrarHorras(self):
        hora_atual = QTime.currentTime()
        label_time = hora_atual.toString('hh:mm:ss')
        self.label_horas.setText(label_time)

    def MostrarCPU(self):
        usocpu =  str(psutil.cpu_percent())
        self.label_cpu.setText("Uso da CPU: " +usocpu +"%")
		
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())