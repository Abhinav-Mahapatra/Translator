import speech_to_text
from text_to_speech import text_speech
import translate
import time

obj = speech_to_text.speech_to_text()
obj2 = translate.translate()
while 1:
    string = obj.main_process()
    if string == "क्विड" or string == "क्विट":
        break
    string = obj2.translation(string)
    text_speech(str(string))
    time.sleep(3)