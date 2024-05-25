import speech_recognition as aa  
import pyttsx3 
import pywhatkit 
import datetime
import wikipedia



listener=aa.Recognizer()


machine=pyttsx3.init()

def talk(text):
    machine.say(text)
    
machine.runAndWait()


def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listining to u .........")
            speech=listener.listen(origin)
            instruction=listener.recognize_google(speech)
            instruction=instruction.lower()
            if"deva" in instruction:
                print(instruction)
        
        
    except:
        pass
    return instruction
    
    
def play_deva():
        instruction=input_instruction()
        print(instruction)
        if "play" in instruction:
            song=instruction.trplace('play'," ")
            talk("playing" + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruction:
            time=datetime.datetime.now().strftime('%I:%M%p')
            talk('current time'+time)
            
        elif 'date' in instruction:
            date=datetime.datetime.now().strftime('%d/%m/%y')
            talk("todays date"+date )
            
        elif 'how are you' in instruction:
            talk("i am fine how are you")
            
        elif 'what is your name' in instruction:
            talk("my name is deva, what can i do for you") 
        
        elif 'who is ' in instruction:
            human=instruction.replace('who is', " ")
            info = wikipedia.summary(human,1)
            print(info)
            talk(info)
            
        else:
            talk('please repeat ')
            
play_deva()
            
        
        