import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr
import sounddevice as sd
import wavio as wv
import pyttsx3
import webbrowser
import os
import time
import random
import ctypes
import datetime


client_id = '8259f7767f264d1ca4b9864c7078efb7'
client_secret = '66561e488585439fbce9d943aac9bbbc'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:61579'
agora = datetime.datetime.now()
horas = agora.hour
minutos = agora.minute
segundos = agora.second

scope = "user-read-playback-state user-modify-playback-state playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret))

def adicionar_playlists(playlists):
    for nome, url in playlists.items():
        playlist_id = url.split('/')[-1].split('?')[0]
        sp.playlist_add_items(playlist_id, [])
        print(f"Playlist '{nome}' adicionada com sucesso!")


def iafala(fala):
    engine = pyttsx3.init()
    engine.say(fala)
    engine.runAndWait()

def grava():
    freq = 48000
    duration = 2.5
    gravacao = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    print('Ouvindo...')
    sd.wait()
    wv.write('minhavoz.wav', gravacao, freq, sampwidth=2)
    limpar_chat()
    print('...')
    time.sleep(1)
    limpar_chat()

ativado = False

def pesquisaggl(fala): 
    search = fala.replace('pesquisar', '') 
    webbrowser.open(f'https://www.google.com/search?q={search}')

def contar_piada():
    piadas = [
        "Por que o cego não pode ser arquiteto? Porque ele não vê a planta baixa.",
        "Por que o canibal não come palhaços? Porque eles fazem graça.",
        "Qual é a semelhança entre um juiz e um criminoso? Ambos têm suas penas.",
        "Por que o esqueleto não brigou? Porque ele não tem coragem no corpo.",
        "O que um tomate assassino disse para o outro? 'Ketchup com você'.",
        "Por que o cadáver foi expulso da festa? Porque estava sem vida social.",
        "Qual é o cúmulo do vegetarianismo? Ser enterrado em covas rasas.",
        "O que acontece quando o dentista está entediado? Ele vai fazer um canal no dentista.",
        "Por que os esqueletos não brigam? Porque eles não têm nervos.",
        "Qual é a fruta mais suicida? O kiwi, ele sempre se corta.",
        "Por que o livro de matemática não aguenta mais? Porque ele tem muitos problemas.",
        "O que a bruxa disse para a mãe dela? 'Mãe, me dá um doce ou eu te lanço uma maldição'.",
        "Por que o lápis não foi ao enterro? Porque ele não tem grafite para ir.",
        "Qual é o carro que todos gostam? O funerária, porque ele sempre tem um caixão no porta-malas.",
        "Por que a galinha atravessou a rua? Para fugir do abatedouro.",
        "Por que a lata foi ao psicólogo? Porque ela estava se achando muito amassada.",
        "Qual é o cúmulo da burrice? Ir ao cinema ver 'O Exorcista' e levar uma vassoura.",
        "O que o livro de ciências disse para o livro de matemática? 'Você é muito complicado'.",
        "Por que a banana não tem família? Porque ela nasceu de cacho.",
        "Qual é o cúmulo da falsidade? Dar um abraço de tamanduá e dizer 'que bom te ver'.",
        "Por que o cachorro estava com o telhado na cabeça? Porque ele era um 'vira-lata'."
        "Por que o cemitério é o lugar mais popular da cidade? Porque as pessoas estão morrendo para entrar lá!",
        "Por que o vampiro não gosta de andar de avião? Porque ele tem medo de perder o voo!",
        "Por que a planta foi ao terapeuta? Porque ela tinha problemas de raiz!",
        "Por que o elefante não usa computador? Porque ele tem medo do mouse!",
        "Por que o esqueleto não foi à festa? Porque ele não tinha corpo para ir!",
        "Por que o pintinho atravessou a rua? Para mostrar que não era galinha!",
        "Qual é o tipo de vinho que não pede identificação? O vinho 'mais-velho'!",
        "Por que o astronauta não consegue se concentrar no espaço? Porque ele sempre perde a gravidade!",
        "Por que o gato não gosta de jogar futebol? Porque ele tem medo de ser um 'gato goleiro'!",
        "Por que o lápis não pode ser piloto? Porque ele sempre quebra na curva!",
        "Por que o mar não tem cabelo? Porque ele está sempre 'ondulado'!",
        "Por que a água foi presa? Porque ela roubou um banco!",
        "Por que a nuvem foi ao psicólogo? Porque ela estava se sentindo 'cumulonimbus'!",
        "Por que o livro não saía com a calculadora? Porque ele tinha medo de ser multiplicado!",
        "O que o café disse para o leite? 'Meu maior desejo é ser misturado a você!'",
        "Por que o cachorro entrou na aula de música? Porque ele queria aprender a 'latir notas'!",
        "Qual é o lugar mais seguro para esconder um corpo? A segunda página do Google!",
        "Por que a salsicha não pode ser médica? Porque ela é um 'embutido'!",
        "Por que a velhinha não usa relógio? Porque ela tem tempo de sobra!",
        "Por que o atleta não foi ao restaurante? Porque ele estava de regime!",
        "Por que a lâmpada foi presa? Porque ela era acusada de iluminar demais!"
        "Há quem diga que Mc Kevin foi melhor que Michael Jackson mas, pelo menos Michael Jackson ia até o chão e voltava"
        "O que as pernas de um paraplégico tem em comum com o comunismo? Ambos não funcionam"
        "Curiosidade curiosa: os golfinhos cutucam baiacus porque eles liberam uma substância que deixa os golfinhos doidões. Isso mesmo, até os golfinhos têm o baseado deles"
        "Como o espermatozóide de um cadeirante foi o mais rápido?"
    ]
    return random.choice(piadas)


def cumprimento_resposta():
    respostas = [
        "Bom dia! Como posso te ajudar?", 
        "Olá! O que posso fazer por você hoje?", 
        "Oi! Estou aqui para ajudar, em que posso ser útil?",
        "Bom dia! Em que posso te ajudar?", 
        "Olá! Como posso ser útil hoje?", 
        "Oi! Estou aqui para ajudar, o que você precisa?",
        "Olá! Como posso te ajudar agora?",
        "Bom dia! Em que posso ser útil hoje?", 
        "Oi! Como posso te ajudar agora?",
        "Bom dia! Estou à disposição, o que você precisa?",
        "Olá! Estou aqui para ajudar, em que posso ser útil?",
        "Bom dia! Como posso te auxiliar hoje?",
        "Olá! Como posso ajudar você agora?",
        "Bom dia! Estou disponível para ajudar, o que você precisa?",
        "Olá! Estou aqui para ajudar, em que posso ser útil?",
        "Bom dia! Em que posso ser útil hoje?",
        "Oi! Como posso te ajudar agora?",
        "Bom dia! Estou à disposição, o que você precisa?",
        "Olá! Como posso te auxiliar agora?",
        "Bom dia! Como posso ajudar você hoje?"
    ]
    return random.choice(respostas)

def despedida_resposta():
    respostas = [
        "Até mais!", 
        "Tchau! Volte sempre.", 
        "Até a próxima!",
        "Até logo!", 
        "Tenha um bom dia!", 
        "Até mais tarde!",
        "Tchau! Foi um prazer ajudar.", 
        "Até mais! Se precisar, estou por aqui.", 
        "Até breve!",
        "Até logo! Se precisar de algo, estou à disposição.",
        "Tchau! Espero ter ajudado.",
        "Até mais! Qualquer coisa, estou aqui.",
        "Tchau! Até a próxima vez.",
        "Até logo! Se precisar de mais alguma coisa, me avise.",
        "Tchau! Que seu dia seja ótimo!",
        "Até mais! Qualquer dúvida, estou à disposição.",
        "Tchau! Estou disponível se precisar de mais alguma coisa.",
        "Até logo! Se precisar de ajuda, é só chamar.",
        "Tchau! Espero ter sido útil.",
        "Até a próxima! Qualquer coisa, estou por aqui."
    ]
    return random.choice(respostas)

def agradecimento_resposta():
    respostas = [
        "De nada!", 
        "Não há de quê!", 
        "Estou aqui para ajudar.",
        "Sem problemas!", 
        "Estou à disposição!", 
        "Foi um prazer ajudar!",
        "É para isso que estou aqui!", 
        "Qualquer coisa, estou por aqui!", 
        "Não mencione!", 
        "Estou aqui para isso!",
        "Não precisa agradecer!", 
        "É um prazer!", 
        "Estou à disposição para ajudar!", 
        "Fico feliz em ajudar!", 
        "Sempre às ordens!",
        "Estou aqui para isso mesmo!", 
        "Por nada!", 
        "Não foi nada!", 
        "Foi um prazer!", 
        "Qualquer coisa, estou à disposição!"
    ]
    return random.choice(respostas)

def reconhecimento_resposta():
    respostas = [
        "Comando reconhecido.", 
        "Entendi o comando.", 
        "Tudo certo, comando entendido.",
        "Compreendido!", 
        "Recebido!", 
        "Comando aceito!",
        "Entendido!", 
        "Claro!", 
        "Sem problemas!",
        "OK!", 
        "Perfeitamente!", 
        "Estou a postos!",
        "Comando entendido e aceito!", 
        "Recebido e entendido!",
        "Claro, estou pronta para te ajudar!",
        "Entendido, estou à disposição!",
        "Compreendido, o que mais você precisa?",
        "Comando recebido com sucesso!",
        "Estou pronta para seguir suas instruções!",
        "Tudo certo, estou pronta para ajudar!"
    ]
    return random.choice(respostas)

def apresentação():
    apresentação = [
        "Olá! Eu sou Zero, uma IA pronta para facilitar seu dia. Posso abrir aplicativos, tocar músicas, pesquisar e muito mais!",
        "Oi! Eu sou a Zero, sua assistente virtual. Estou aqui para ajudar com várias tarefas, como abrir aplicativos, tocar música e fazer pesquisas!",
        "E aí! Me chamo Zero, uma IA pronta para tornar sua vida mais fácil. Posso abrir apps, tocar músicas, pesquisar e muito mais!",
        "Hey! Sou a Zero, sua assistente pessoal. Posso ajudar com várias coisas, como abrir apps, tocar música e pesquisar na web!",
        "E aew! Eu sou a Zero, uma IA feita para facilitar sua vida. Posso abrir apps, tocar músicas e muito mais!",
        "Oi, sou a Zero! Uma assistente pronta para ajudar. Posso abrir apps, tocar músicas e fazer pesquisas!",
        "Olá! Eu sou Zero, sua assistente virtual. Estou aqui para ajudar em várias tarefas, como abrir apps, tocar músicas e pesquisar!",
        "Hey! Aqui é a Zero, pronta para facilitar sua vida. Posso abrir apps, tocar músicas e fazer pesquisas para você!",
        "E aí! Sou a Zero, sua assistente pessoal. Posso te ajudar com várias coisas, como abrir apps, tocar música e fazer pesquisas!",
        "Prazer! Eu sou a Zero, uma IA pronta para facilitar sua vida. Posso abrir aplicativos, tocar músicas, pesquisar e muito mais!"
    ]
    return random.choice(apresentação)


def limpar_chat():
    os.system('cls' if os.name == 'nt' else 'clear')

def suspender_sistema():
    powrprof = ctypes.WinDLL("powrprof.dll")
    powrprof.SetSuspendState(0, 1, 0)

def desligar_sistema():
    os.system("shutdown /s /t 1")


xingamentom = ["vadia", "puta", "arrombada", "vagabunda", "safada", "pobre", "inútil", "máquina de lavar louça", "fudida", "burra"]

xingamentoh = ["vagabundo", "preto", "arrombado", "vagabundo", "inútil", "pobre", "fudido", "desempregado", "virgem"]

xingamentoc = ["Vai se foder", "Vai se fuder", "filho da puta", "desempregado fudido", "passa fome", "pobre fudido", "Vai tomar no cu"]

xingamentocop = ["vai se fuder", "filho da puta", "desempregado fudido", "passa fome", "pobre fudido", "Vai tomar no cu"]
    

while True:
    if not ativado:
        print("Aguardando o comando de ativação...")
        grava()
        r = sr.Recognizer()
        filename = 'minhavoz.wav'
        with sr.AudioFile(filename) as source:
            audio_data = r.record(source)
            try:
                texto = r.recognize_google(audio_data, language='pt-br')
                print('Você disse:' + texto)
                if texto == '0' or texto == 'zero' or texto == 'ligar' or texto == 'sero':
                    texto = 'zero'
            except sr.UnknownValueError:
                texto = ""

            if texto == '0' or texto == 'zero' or texto == 'ligar' or texto == 'sero':
                iafala(reconhecimento_resposta() + " Agora estou ativada.")
                ativado = True
            elif 'desligar' in texto.lower() or 'sair' in texto.lower():
                iafala(despedida_resposta())
                time.sleep(1)
                limpar_chat()
                break

    else:
        grava()
        r = sr.Recognizer()
        filename = 'minhavoz.wav'
        with sr.AudioFile(filename) as source:
            audio_data = r.record(source)
            try:
                texto = r.recognize_google(audio_data, language='pt-br')
                print('Você disse:' + texto)
                if texto == '0' or texto == 'zero' or texto == 'ligar' or texto == 'sero':
                    texto = 'zero'
            except sr.UnknownValueError:
                texto = ""

        fala = texto.lower()

        if fala == 'bom dia' or fala ==  'boa noite' or fala == 'cheguei':
            iafala(cumprimento_resposta())

        elif fala == 'obrigado' or fala == 'agradecido':
            iafala(agradecimento_resposta())

        elif fala == 'conte uma piada':
            iafala(contar_piada())

        if 'pesquisar' in fala:
            pesquisaggl(fala)

        elif fala == 'abrir spotify':
            iafala("Abrindo spotify")
            webbrowser.open('https://open.spotify.com/intl-pt')

        elif fala == 'abrir youtube':
            iafala("Abrindo YouTube")
            webbrowser.open('https://www.youtube.com/')

        elif fala == 'abrir blood strike':
            iafala('Abrindo Blood Strike')
            os.startfile('C:/Users/stonk/bloodstrike/launcher.exe')
            os.startfile('E:/importante/Automatic Mouse and Keyboard 5.2.9.2 + Crack-20240129T045523Z-001/Automatic Mouse and Keyboard 5.2.9.2 + Crack/Crack/AutoMouseKey.exe')

        elif fala == 'desligar' or fala == 'sair':
            iafala(despedida_resposta())
            time.sleep(1)
            break

        elif fala == 'limpar' or fala == 'limpar chat':
            limpar_chat()

        elif fala == 'modo de espera' or fala == 'suspender' or fala == 'já volto':
            iafala('Voltando ao modo de espera...')
            ativado = False

        elif fala == 'tocar mix':
            iafala('Tocando mix diario')
            playlist_uri = 'https://open.spotify.com/playlist/37i9dQZF1E37KkqbdConyC?si=7a42a6f38fe94ac0'
            sp.start_playback(context_uri=playlist_uri)

        elif fala == 'tocar playlist para jogar' or fala == 'playlist para jogar' or fala == 'música para jogar':
            iafala('Tocando a playlist para jogar.')
            playlist_uri = 'https://open.spotify.com/playlist/4S8at0p9gFCzWxlyy50L8Q?si=298d15df530b4743'
            sp.start_playback(context_uri=playlist_uri)

        elif fala == 'tocar rap':
            iafala('Tocando a playlist de rap.')
            playlist_uri = 'https://open.spotify.com/playlist/7bicDFaQYlp9DUgF3XNyZK?si=7e6e9b8348914450'
            sp.start_playback(context_uri=playlist_uri)

        elif fala == 'tocar funk':
            iafala('Tocando a playlist de funk.')
            playlist_uri = 'https://open.spotify.com/playlist/5nRiuP8eC5tCY2MpX8qr0q?si=f7b033bf91dd49b2'
            sp.start_playback(context_uri=playlist_uri)

        elif fala ==  'pausar':
            iafala('Pausando música.')
            sp.pause_playback()

        elif fala ==  'continuar' or fala ==  'retomar':
            iafala('Retomando música.')
            sp.start_playback()

        elif fala == 'pular' or fala == 'pular musica' or fala == 'pular música':
            iafala('Pulando música.')
            sp.next_track()

        elif fala ==  'voltar' or fala == 'voltar musica' or fala == 'voltar música':
            iafala('Voltando para a música anterior.')
            sp.previous_track()
        
        elif fala in xingamentom:
            respostah = random.choice(xingamentoh)
            iafala(f'Me respeita seu {respostah}')
            
        elif fala in xingamentoc:
            respostacop = random.choice(xingamentocop)
            iafala(f"Cuidado com o que diz seu {respostacop}")

        elif fala == 'abrir discord':
            iafala('Abrindo Discord')
            os.startfile('C:/Users/stonk/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord')

        elif fala == 'suspender sistema':
            iafala('Suspendendo o sistema, aguarde...')
            time.sleep(1)
            suspender_sistema()

        elif fala == 'desligar computador':
            iafala('Desligando o computador, aguarde...')
            time.sleep(1)
            desligar_sistema()

        elif fala ==  'introdução' or fala == 'quem é você' or fala == 'se apresente':
            iafala(apresentação())

        elif fala == 'abrir minecraft':
            iafala('Abrindo minecraft')
            os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/CMClient Launcher')

        elif fala == 'que horas são?' or fala == 'que horas são' or fala == 'horas':
            iafala(f'São {horas} horas e {minutos} minutos')
            