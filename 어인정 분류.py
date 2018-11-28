while(True):
    a = input()
    list_a = a.split()
    list_a.reverse()
    #print(list_a)
    #i = list_a[0] + ' ' + 'INJEONG' + '\n'
    if len(list_a) < 3:
        i = list_a[1] + ' ' + list_a[0] + '\n'
    elif list_a[0] == 'INJEONG':
        i = list_a[1] + ' ' + list_a[0] + '\n'
    elif list_a[1] == 'INJEONG':
        i = list_a[2] + ' ' + list_a[1] + ' ' + list_a[0] + '\n'
    else:
        i = ''
    #print(i)
    f = open('word.txt', 'a')
    f.write(i)
f.close()