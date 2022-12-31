import pyttsx3
import subprocess
import speech_recognition as sr

engine = pyttsx3.init()
shutdown = 0
frase = None
pause = 0

# Função para ouvir e reconhecer a fala
def ouvir_microfone(shutdown):

    global pause
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

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

            if "despause" in frase:
                engine.say("Dando continuidade ao serviço")
                engine.runAndWait()
                pause = 0


            if frase.startswith("ávora") \
                    and "pause" in frase:
                engine.say("Pausando o serviço")
                engine.runAndWait()
                pause = 1

            if pause == 1:
                continue


            # Abre o navegador
            if frase.startswith("Abrir") or frase.startswith("Abra") \
                    and "navegador" in frase or "Google" in frase or "Chrome" in frase or "Google Chrome" in frase:
                subprocess.check_call([r"C:\Program Files\Google\Chrome\Application\chrome.exe"])
                engine.say("Abrindo o navegador")
                engine.runAndWait()
                frase = "reinit th while"

            if frase == "desligue":
                shutdown = 1
                engine.say("Desligando.")
                engine.runAndWait()

            if frase.startswith("repita depois de mim"):
                engine.say(frase[21:])
                engine.runAndWait()
                frase = "reinit th while"




            if "reinit th while" in frase:

                with sr.Microphone() as source:
                    # Chama um algoritmo de reducao de ruidos no som
                    microfone.adjust_for_ambient_noise(source)

                    # Frase para o usuario dizer algo
                    print("Diga alguma coisa: ")

                    # Armazena o que foi dito numa variavel
                    audio = microfone.listen(source)
                    continue

            if frase == None:
                with sr.Microphone() as source:
                    # Chama um algoritmo de reducao de ruidos no som
                    microfone.adjust_for_ambient_noise(source)

                    # Frase para o usuario dizer algo
                    print("Diga alguma coisa: ")

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
                    print("Diga alguma coisa: ")

                    # Armazena o que foi dito numa variavel
                    audio = microfone.listen(source)
                    continue


            # Retorna a frase pronunciada
            print("Você disse: " + frase)




        # Se nao reconheceu o padrao de fala, exibe a mensagem
        except sr.UnknownValueError:
            with sr.Microphone() as source:
                # Chama um algoritmo de reducao de ruidos no som
                microfone.adjust_for_ambient_noise(source)

                # Frase para o usuario dizer algo
                print("Diga alguma coisa: ")

                # Armazena o que foi dito numa variavel
                audio = microfone.listen(source)
                continue

ouvir_microfone(shutdown)