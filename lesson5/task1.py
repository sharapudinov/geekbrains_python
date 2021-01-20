with open('file1.txt','w') as f:
    while True:
        line=input("введите строку для сохранения (пустая срока для выхода): ")
        if line =='':
            break
        f.write(line+'\n')