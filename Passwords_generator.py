import random as r


def choose(lang, digs, ups, punct, neodn):
    digits = '0123456789'
    if lang.lower() == 'русский' or lang.lower() == 'рус':
        chars = 'абвгдеёжзийклмнопрстуфхцчшщыъьэюя'
        if input('Хотите ли вы добавить в пароли английские буквы? ').lower() == 'да':
            chars += 'abcdefghijklmnopqrstuvwxyz'
    elif lang.lower() == 'english' or lang.lower() == 'eng':
        chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = chars.upper()
    punctuation = '!#$%&*+-=?@^_'
    nols = 'il1Lo0OоОеЕeEаАaApPрРIсcCСкКkKTТуy'
    if digs.lower() == 'да' or digs.lower() == 'yes':
        chars += digits
    if ups.lower() == 'да' or ups.lower() == 'yes':
        chars += uppercase_letters
    if punct.lower() == 'да' or punct.lower() == 'yes':
        chars += punctuation
    if neodn.lower() == 'да' or neodn.lower() == 'yes':
        for cr in nols:
            if cr in chars:
                chars = chars.replace(cr, '')
    return chars


def psw(number_ps, psw_lenght, chs):
    resls = []
    for i in range(number_ps):
        passw = ''
        for _ in range(psw_lenght):
            passw += chs[r.randint(0, len(chs) - 1)]
        resls.append(passw)
    return resls


language = input('На каком языке вы говорите?\nOn which language do you speak? ')
if language == 'русский' or language == 'рус':
    print(*psw(int(input('Сколько паролей вы хотите? ')), int(input('Какой длины будет каждый пароль? ')),
               choose(language, input('Хотите ли вы, чтобы в пароле были цифры? '),
                      input('Хотите ли вы, чтобы в пароле были заглавные буквы? '),
                      input('Хотите ли вы, чтобы в пароле были специальные символы? '),
                      input('Хотите ли вы исключить неоднозначные символы? '))), sep='\n')
elif language.lower() == 'english' or language.lower() == 'eng':
    print(*psw(int(input('How many passwords do you want? ')), int(input('Which lenght should be each password? ')),
               choose(language, input('Do you want digits in passwords? '),
                      input('Do you want capital letters in passwords? '),
                      input('Do you want special symbols in passwords? '),
                      input('Do you want to delete ambiguous symbols? '))), sep='\n')
else:
    print('Invalid language')

