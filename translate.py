from googletrans import Translator

class translate:
    def __init__(self):
        self.translator = Translator(service_urls=[
          'translate.google.com',
          'translate.google.co.kr',
        ])

    def translation(self, string):
        translated = self.translator.translate(string, src='hi', 
                                              dest='ja')
        print(translated.pronunciation)
        return translated.pronunciation