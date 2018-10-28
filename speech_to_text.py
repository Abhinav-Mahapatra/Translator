import speech_recognition as sr

class speech_to_text:
    def __init__(self):
        self.r = sr.Recognizer()
    def main_process(self):
        with sr.Microphone() as source:
            print("Say Something: ")
            audio = self.r.listen(source)
            print("Processing....")
        try:
            self.output = self.r.recognize_google(audio, language='hi-IN')
            print("Text: "+self.output)
        except Exception as e:
            print("There has been some Issue: "+str(e))
        return self.output
