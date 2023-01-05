import pygame
import speech_recognition as sr
import pyttsx3


pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
r = sr.Recognizer()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('GUI Speech Recognition')

gameDisplay.fill(white)
carImg = pygame.image.load('voice_wave.GIF')
gameDisplay.blit(carImg,(0,0))

def close():
    pygame.quit()
    quit()


def SpeakText(command):
    gameDisplay.blit(carImg, (0, 0))
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



while (1):

    try:


        with sr.Microphone() as source2:


            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)


            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say " + MyText)
            SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")


