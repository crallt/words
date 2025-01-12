import random 
words_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]

def get_word():
    l = random.choice(words_list)
    return l

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

def uu(n):
    z = ',./123456789@!&^%'
    for i in n:
        if i in z:
            return False


def play(word):
    tries = 6  
    print('Давайте играть в угадайку слов!')
    display_hanagman(tries)
    l = get_word()
    guessed = False

    word_completion = '_' * len(word)
    print('Начальное слово: ',word_completion)


    while guessed == False:
        z = input()
        if uu(z) == False:
            z = input('слово или буква не содержит ,./123456789@!&^%')
        if z == l:
            print('Ответ верный!') 
            return   
        if z in guessed_letters:
            print('такая буква уже была названа попробуй еще')
            z = input()
        if z in l:
            

                        # сигнальная метка             # список уже названных букв
    guessed_words = []             # список уже названных слов
                            





play(get_word())
