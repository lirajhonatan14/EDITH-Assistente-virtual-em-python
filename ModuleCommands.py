import webbrowser #importa biblioteca de navegação
import subprocess #importar biblioteca de controle de subprocessos
import pyttsx3

engine = pyttsx3.init()

def parse_command(command_action, argument=""):#função verefica qual é web e qual é executavel e recarga de comandos

  if command_action[0:3]=="web":
    open_link(command_action[4:], argument)
    Speak("Pesquisando " + argument)
  elif command_action[0:4]=="path":
    open_program(command_action[5:])
    Speak("Abrindo " + argument)
  

def Speak(audio):
  engine.setProperty("voice", "brazil")
  engine.setProperty("rate", 150)
  engine.setProperty("volume", 2.)
  engine.say(audio)
  engine.runAndWait()
    
    
def open_link(link, argument=""): #funçao para abrir link google ou qualquer outro site para pesquisas
  print(f'{link}/search?q={argument}')
  webbrowser.get('windows-default').open_new(f'{link}/search?q={argument}')

def open_program(path): #função para abrir o programa
  subprocess.Popen([path, '-new-tab'])

