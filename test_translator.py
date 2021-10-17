from translate import Translator
from config import *
translator = Translator(MODEL_PATH)

all_langs = translator.get_supported_langs()
print(all_langs)
