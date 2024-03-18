def sort_(files):
    # Создаётся словарь: ключи - имена файлов, значения - содержимое в виде списков из строк файлов
    files = {f: open(f, 'r', encoding='utf-8').readlines() for f in files}
    print(files)
    # Сортируется словарь по значению (по количеству элементов в списках)
    files = sorted(files.items(), key=lambda x: len(x[1]))
    # Записывается в итоговый файл
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in files:
            f.write(file[0] + '\n' + str(len(file[1])) + '\n' + ''.join(file[1]) + '\n')


# На входе - список файлов
sort_(['1.txt', '2.txt', '3.txt'])
