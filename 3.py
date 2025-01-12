import random






#def play(word):
def display_hanagman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''']
     
    return stages[tries]     



def found(text, char, w, tries, z_z):
    start = 0
    z = 0
    indexes = []
    while True:
        index = text.find(char, start)
        if index == -1:
            if z == 0:
                tries = tries - 1
                print(display_hanagman(tries))
                #print('Вы проиграли, загаданое слово: ', l)
            for i in indexes:
                f = l[i]
                w = w[:i] + f + w[i+1:] 

            return w, tries
        z = z +1
        indexes.append(index)
        start = index + 1

    


def uu(n):
    z = ',./123456789@!&^%'
    for i in n:
        if i in z:
            return False


def get_word():
    words_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]
    l = random.choice(words_list)
    return l

l = get_word()
print(l)
ss = False
tries = 6

w = '_' * len(l)
z_z = 0

def play(w,l,tries,z_z):
    if z_z > 0:
        l = get_word()
        print(l)
    else:
        False   

    while ss == False:
        z = input("Введите букву или слово целиком: \n")

        if uu(z) == False:
            print('введен неверный знак')
            continue         

        if len(z) == 1:
            if z in w:
                print('введенная вами буква уже есть, введите другую')
                continue

            if w == l:
                print("Вы победили!")
                z_z= z_z +1
                tt = input("Хотите сыграть еще раз? Да /n")
                if tt == 'Да' or tt == 'да':
                    play(w,l, tries, z_z)
                break
            else:
                indexes = found(l, z,w, tries, z_z)
                w, tries = indexes
                if tries == 0:
                    print('Вы проиграли загаданное слово: ', l)
                    z_z= z_z +1
                    tt = input("Хотите сыграть еще раз? Да \n")
                    if tt == 'Да' or tt == 'да':
                        play(w,l, tries, z_z)
                    else:
                        break
                print('Количество оставшихся жизней: ', tries)
                print(w)

        else:
            if z == l:
                print('Ответ верный!')
                z_z= z_z +1
                tt = input("Хотите сыграть еще раз? Да \n")
                if tt == 'Да' or tt == 'да':
                    play(w,l, tries, z_z)
                else:
                    break
            else:
                tries = tries - 1

                print('Количество оставшихся жизней: ', tries)
                #print('fffdfd')
                print(display_hanagman(tries))
                if tries == 0:
                    print('Вы проиграли загаданное слово: ', l)
                    z_z= z_z +1
                    tt = input("Хотите сыграть еще раз? Да \n")
                    if tt == 'Да' or tt == 'да':
                        play(w,l, tries, z_z)
                    else:
                        break


play(w,l, tries, z_z)



