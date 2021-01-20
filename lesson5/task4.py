number_dict = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
from googletrans import Translator

translator = Translator()

with open('for_translation', 'r') as inf:
    translation = [f'{number_dict[int(line.rstrip().split("—")[1])]} — {line.rstrip().split("—")[1]}\n' for line in
                   inf]
    with open('my_translation.txt', 'w') as of:
        of.writelines(translation)
    inf.seek(0)
    translations = translator.translate(inf.readlines(), dest='ru')
    with open('google_translation.txt', 'w') as of:
        of.writelines([translation.text + '\n' for translation in translations])
