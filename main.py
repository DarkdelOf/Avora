import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import os

otherquestAudio = AudioSegment.from_mp3("sfx/otherquest.mp3")
pauseAudio = AudioSegment.from_mp3("sfx/pause.mp3")
unpauseAudio = AudioSegment.from_mp3("sfx/unpause.mp3")
engine = pyttsx3.init()
shutdown = 0
frase = None
pause = 0
CHROME = os.path.join("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
from playwright.sync_api import sync_playwright


# Função para ouvir e reconhecer a fala
def ouvir_microfone(shutdown):

    global questionsound
    global pause
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa1: ")

        # Toca um áudio definindo o início do comando
        play(otherquestAudio)

        # Armazena o que foi dito numa variavel
        audio = microfone.listen(source)



    # Repeat the code until shutdown is 1
    while shutdown != 1:
        try:

            if pause == 1:
                with sr.Microphone() as source:
                    # Chama um algoritmo de reducao de ruidos no som
                    microfone.adjust_for_ambient_noise(source)

                    # Armazena o que foi dito numa variavel
                    audio = microfone.listen(source)



            # Passa a variável para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio, language='pt-BR')

            # Despausa a Avora
            if "despause" in frase or "despausa" in frase:
                engine.say("Dando continuidade ao serviço")
                engine.runAndWait()
                play(unpauseAudio)
                pause = 0

            # Pausa a Avora
            if frase.startswith("ávora") or frase.startswith("árvore") or frase.startswith("abóbora") or frase.startswith("afora") or frase.startswith("agora"):
                if "pause" in frase:
                    engine.say("Pausando o serviço")
                    engine.runAndWait()
                    play(pauseAudio)
                    pause = 1

            if pause == 1:
                continue


            # Abre o navegador
            if frase.startswith("Abrir") or frase.startswith("Abra") or frase.startswith("abra") or frase.startswith("abrir"):
                if "navegador" in frase or "Google" in frase or "Chrome" in frase or "Google Chrome" in frase:
                    try:
                        os.popen('C:\Program Files\Google\Chrome\Application\chrome.exe', 'r', 1)
                    except:
                        continue
                    engine.say("Abrindo o navegador")
                    engine.runAndWait()
                    frase = "reinit th while"


            # Fecha o navegador
            if frase.startswith("Feche") or frase.startswith("Fecha") or frase.startswith("feche") or frase.startswith("fecha"):
                if "navegador" in frase or "Google" in frase or "Chrome" in frase or "Google Chrome" in frase:
                    os.system('taskkill /im chrome.exe')
                    engine.say("Fechando o navegador")
                    engine.runAndWait()
                    frase = "reinit th while"


            # Desliga a Avora
            if frase == "desligue":
                shutdown = 1
                engine.say("Desligando.")
                engine.runAndWait()

            # Faz a Avora repetir uma frase
            if frase.startswith("repita depois de mim"):
                engine.say(frase[21:])
                engine.runAndWait()
                frase = "reinit th while"

            # Avora explica quem é
            if frase.startswith("ávora") or frase.startswith("árvore") or frase.startswith("abóbora") or frase.startswith("afora") or frase.startswith("agora"):
                if "quem é você" in frase or 'Quem é você' in frase:
                    engine.say(
                        "Sou uma assistente virtual disposta a te ajudar nas tarefas do dia a dia, no trabalho, ou mesmo no lazer.")
                    engine.runAndWait()
                    frase = "reinit th while"

            # Comandos musica
            if frase.startswith("defina"):
                engine.say('procurando por' + frase[6:])
                engine.runAndWait()
                with sync_playwright() as p:
                    try:
                        browser = p.chromium.launch()
                        page = browser.new_page()
                        page.goto("https://www.google.com")
                        if frase != 'defina':
                            page.locator(
                                'xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').fill(
                                'wikipedia')
                            page.locator(
                                'xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
                            page.locator('xpath=//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3').click()
                            page.locator('xpath=//*[@id="searchform"]').click()
                            page.locator(
                                'xpath=/html/body/div[1]/div/header/div[2]/div/div/div/form/div/div/div[1]/input').fill(
                                frase[6:])
                            page.locator('xpath=//*[@id="searchform"]/div/button').click(timeout=2000)
                            WikipediaResponse = page.locator(
                                'xpath=//*[@id="mw-content-text"]/div[1]/p[1]').inner_text(timeout=2000)
                            print(WikipediaResponse)
                            engine.say(WikipediaResponse)
                            engine.runAndWait()
                            browser.close()
                            frase = "reinit th while"
                        else:
                            engine.say('Não entendi')
                            engine.runAndWait()
                            frase = 'reinit th while'
                    except:
                        try:
                            browser = p.chromium.launch()
                            page = browser.new_page()
                            page.goto("https://www.google.com")
                            if frase != 'defina':
                                page.locator(
                                    'xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').fill(
                                    'wikipedia en')
                                page.locator(
                                    'xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
                                page.locator('xpath=//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3').click()
                                page.locator('xpath=//*[@id="p-search"]').click()
                                page.locator(
                                    'xpath=//*[@id="searchInput"]').fill(
                                    frase[6:])
                                page.locator('xpath=//*[@id="searchButton"]').click(timeout=2000)
                                WikipediaResponse = page.locator(
                                    'xpath=//*[@id="mw-content-text"]/div[1]/p[1]').inner_text(timeout=2000)
                                print(WikipediaResponse)
                                engine.say(WikipediaResponse)
                                engine.runAndWait()
                                browser.close()
                                frase = "reinit th while"
                            else:
                                engine.say('Não entendi')
                                engine.runAndWait()
                                frase = 'reinit th while'
                        except:
                            engine.say('Não encontrei nada sobre.')
                            engine.runAndWait()
                            frase = 'reinit th while'













            if "reinit th while" in frase:

                with sr.Microphone() as source:
                    # Chama um algoritmo de reducao de ruidos no som
                    microfone.adjust_for_ambient_noise(source)

                    # Frase para o usuario dizer algo
                    print("Diga alguma coisa2: ")

                    # Toca um áudio definindo o início do comando
                    play(otherquestAudio)

                    # Armazena o que foi dito numa variavel
                    audio = microfone.listen(source)
                    continue

            if frase == None:
                with sr.Microphone() as source:
                    # Chama um algoritmo de reducao de ruidos no som
                    microfone.adjust_for_ambient_noise(source)

                    # Frase para o usuario dizer algo
                    print("Diga alguma coisa3: ")

                    # Toca um áudio definindo o início do comando
                    play(otherquestAudio)

                    # Armazena o que foi dito numa variavel
                    audio = microfone.listen(source)
                    continue

            if shutdown == 1:
                break


            else:
                engine.say("Não entendi, repita por favor.")
                engine.runAndWait()
                with sr.Microphone() as source:
                    # Chama um algoritmo de reducao de ruidos no som
                    microfone.adjust_for_ambient_noise(source)

                    # Frase para o usuario dizer algo
                    print("Diga alguma coisa4: ")

                    # Toca um áudio definindo o início do comando
                    play(otherquestAudio)

                    # Armazena o que foi dito numa variavel
                    audio = microfone.listen(source)
                    continue






        # Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnknownValueError:
            with sr.Microphone() as source:
                # Chama um algoritmo de reducao de ruidos no som
                microfone.adjust_for_ambient_noise(source)

                # Armazena o que foi dito numa variavel
                audio = microfone.listen(source)
            print("fora de comando")
            continue

ouvir_microfone(shutdown)