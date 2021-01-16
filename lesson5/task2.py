with open('file1.txt','r') as f:
    lines= f.readlines()
    word_count = [len(line.split()) for line in lines]
print(f'Число строк в файле - {len(lines)}')
print('количество слов с строках - ', *word_count)