from googletrans import Translator

translator = Translator()
inputs=input('entrez les mot >')


out=translator.translate(inputs, dest='en')
print(out.text)