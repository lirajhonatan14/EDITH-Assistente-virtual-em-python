import subprocess #importar biblioteca de controle de subprocessos
import pyttsx3
import datetime
import sys
import playsound

engine = pyttsx3.init()

def parse_command(command_action, argument=""):#função verefica qual é web e qual é executavel e recarga de comandos

  if command_action[0:3]=="cnv":
    val = str(command_action[4:])
    if 'bom dia' in val: #Bom Dia E.D.I.T.H
        Horario = int(datetime.datetime.now().hour)
        if Horario >= 0 and Horario < 12:
            Speak('Olá')
            Speak('Bom dia')
        
        elif Horario >= 12 and Horario < 18:
            Speak('Agora não é mais de manhã')
            Speak('Já passou do meio dia')
            Speak('Estamos no período da tarde')
        
        elif Horario >= 18 and Horario != 0:
            Speak('Agora não é de manhã')
            Speak('Já estamos no período noturno')
            Speak('Boa noite')
  
    if 'boa tarde' in val:
        #Boa Tarde E.D.I.T.H
        Horario = int(datetime.datetime.now().hour)
        if Horario >= 0 and Horario < 12:
            Speak('Agora não é de tarde')
            Speak('Ainda é de manhã')
            Speak('Bom dia')
        
        elif Horario >= 12 and Horario < 18:
            Speak('Olá')
            Speak('Boa tarde')
        
        elif Horario >= 18 and Horario != 0:
            Speak('Agora não é de tarde')
            Speak('Já escureceu')
            Speak('Boa noite')

    if 'boa noite' in val: #Boa Noite E.D.I.T.H
        Horario = int(datetime.datetime.now().hour)
        if Horario >= 0 and Horario < 12:
            Speak('Agora não é de noite')
            Speak('Ainda estamos no período diurno')
            Speak('É de manhã')
            Speak('Bom dia')
        
        elif Horario >= 12 and Horario < 18:
            Speak('Agora não é de noite')
            Speak('Ainda estamos no período da tarde')
        
        elif Horario >= 18 and Horario != 0:
            Speak('Olá')
            Speak('Boa noite')
            
    if 'modo de combate' in val:
        Speak('Ativando modo de combate')
        playsound.playsound('efeito.mp3')
        
    if 'desligar' in val:
        Speak('Ok')
        Speak('Vou encerrar por enquanto')
        Speak('Até mais')
        AteMais()
        sys.exit()
    else:
        Speak(val)
    return val
        
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
    engine.setProperty("rate", 120)
    engine.setProperty("volume", 1.)    
    engine.say(audio)
    engine.runAndWait()

    
    
def fala(resp): #funçao para abrir link google ou qualquer outro site para pesquisas
  
    if 'bom dia' in val: #Bom Dia E.D.I.T.H
        Horario = int(datetime.datetime.now().hour)
        if Horario >= 0 and Horario < 12:
            Speak('Olá')
            Speak('Bom dia')
        
        elif Horario >= 12 and Horario < 18:
            Speak('Agora não é mais de manhã')
            Speak('Já passou do meio dia')
            Speak('Estamos no período da tarde')
        
        elif Horario >= 18 and Horario != 0:
            Speak('Agora não é de manhã')
            Speak('Já estamos no período noturno')
            Speak('Boa noite')
  
    if 'boa tarde' in val:
        #Boa Tarde E.D.I.T.H
        Horario = int(datetime.datetime.now().hour)
        if Horario >= 0 and Horario < 12:
            Speak('Agora não é de tarde')
            Speak('Ainda é de manhã')
            Speak('Bom dia')
        
        elif Horario >= 12 and Horario < 18:
            Speak('Olá')
            Speak('Boa tarde')
        
        elif Horario >= 18 and Horario != 0:
            Speak('Agora não é de tarde')
            Speak('Já escureceu')
            Speak('Boa noite')

    if 'boa noite' in val: #Boa Noite E.D.I.T.H
        Horario = int(datetime.datetime.now().hour)
        if Horario >= 0 and Horario < 12:
            Speak('Agora não é de noite')
            Speak('Ainda estamos no período diurno')
            Speak('É de manhã')
            Speak('Bom dia')
        
        elif Horario >= 12 and Horario < 18:
            Speak('Agora não é de noite')
            Speak('Ainda estamos no período da tarde')
        
        elif Horario >= 18 and Horario != 0:
            Speak('Olá')
            Speak('Boa noite')
    if 'desligar' in val:
        sys.exit()