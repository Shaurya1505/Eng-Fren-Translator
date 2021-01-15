from translate import Translator
translator= Translator(from_lang="english",to_lang="french")
str = input('What do you want to translate?')
traslatedSentence= translator.translate(str)
print translatedSentence