# основная логика
def ru_en(user_inp):
    help_list = []    # вспомогательный список
    chars = list(user_inp)    # список символов из user_inp
    for char in chars:
        index_of_char = list_ru.index(char)    # находим индекс символа в списке рус букв
        letter = list_en[index_of_char]    # letter = символу из англ списка по индексу рус символа
        help_list.append(letter)    # добавление символа в единый лист
        result = "".join(help_list)    # объединение символов в слово
    return result

def en_ru(user_inp):
    help_list = []    # вспомогательный список
    chars = list(user_inp)    # список символов из user_inp
    count = 0
    chars_len = len(chars)
    while count < chars_len:
        if chars[count] in {"h","t","s","c","y"}:    # поиск проблемных символов
            if chars[count] == "t" and count + 1 < chars_len and chars[count + 1] == "s":    # если t а после s то добавляется ц
                count += 2
                help_list.append("ц")
            elif chars[count] == "c" and count + 1 < chars_len and chars[count + 1] == "h":    # если c а после h то добавляется ч
                count += 2
                help_list.append("ч")
            elif chars[count] == "y" and count + 1 < chars_len and chars[count + 1] == "a":    # если y а после a то добавляется я
                count += 2
                help_list.append("я")
            elif chars[count] == "y" and count + 1 < chars_len and chars[count + 1] == "u":    # если y а после u то добавляется ю
                count += 2
                help_list.append("ю")
            elif chars[count] == "y" and count + 1 < chars_len and chars[count + 1] == "o":    # если y а после o то добавляется ё
                count += 2
                help_list.append("ё")
            elif chars[count] == "s" and count + 1 < chars_len and chars[count + 1] == "h":    # проверка на ш/щ
                if count + 3 < chars_len and chars[count + 2] == "c" and chars[count + 3] == "h":
                    count += 4
                    help_list.append("щ")
                else:
                    count += 2
                    help_list.append("ш")
            else:    # для h/t/s/c/y
                index_of_char = list_en.index(chars[count])    # находим индекс символа в списке анг букв
                letter = list_ru[index_of_char]    # letter = символу из рус списка по индексу англ символа
                help_list.append(letter)    # добавление символа в единый лист
                count += 1
        elif chars[count] in {"'", '"'}:    # ь/ъ
            if chars[count] == "'":
                help_list.append("ь")
                count += 1
            elif chars[count] == '"':
                help_list.append("ъ")
                count += 1
        else:    # остальные буквы
            index_of_char = list_en.index(chars[count])    # находим индекс символа в списке анг букв
            letter = list_ru[index_of_char]    # letter = символу из рус списка по индексу англ символа
            help_list.append(letter)    # добавление символа в единый лист
            count += 1
    result = "".join(help_list)    # объединение символов в слово
    return result 

def determinant(user_inp):    # проверка символов слова на принадлежность к одному из языков
    check_list = list(user_inp)    # список из слова
    count = 0
    for char in check_list:
        if char in list_ru or char in list_en:
            if char in list_ru:
                if char in {" ", ","}:
                    continue
                else: 
                    count += 1
            else:
                count -= 1
        else:
            return "_"
    if count > 0:
        return "1"
    else: return "2"
    
def translate(choice, user_inp):    # перевод 
    match choice:
        case "1":
            return ru_en(user_inp)
        case "2":
            return en_ru(user_inp)
        case "_":
            return "_"

# список букв
list_ru = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", 
"л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш",
 "щ", "ъ", "ы", "ь", "э", "ю", "я", " ", ","]
list_en = ["a", "b", "v", "g", "d", "e", "yo", "zh", "z", "i", "j", 
"k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", 
"ch", "sh", "shch",'"',"y", "'", "e", "yu", "ya", " ", ","]

# main
while True:
    print("-" * 15)
    user_inp = input("Введите ваше слово: ").strip().lower()
    if user_inp == "break":
        break
    elif not user_inp:
        print("-" * 15)
        print("Ошибка, некорректный ввод")
        continue
    elif translate(determinant(user_inp), user_inp) == "_":
        print("-" * 15)
        print("Ошибка, введен спец символ или цифра")
    else:
        print("-" * 15)
        print(f"Перевод: {translate(determinant(user_inp), user_inp)}")
        