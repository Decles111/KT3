import random

word = ""
hint = ""
guessed = []
wrong = 0
max_wrong = 6
masked_word = ""

def load_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    data = {}
    for line in lines:
        w, h = line.strip().split(":")
        data[w] = h
    return data


def choose_word(words_dict):
    global word, hint, masked_word
    word = random.choice(list(words_dict.keys()))
    hint = words_dict[word]
    masked_word = "*" * len(word)


def show_state():
    print("\nСлово:", masked_word)
    print("Подсказка:", hint)
    print("Ошибок:", wrong)


def guess_letter():
    global guessed, wrong, masked_word

    letter = input("Введите букву: ")

    if letter in guessed:
        print("Уже была!")
        return

    guessed.append(letter)

    if letter in word:
        new_mask = ""
        for i in range(len(word)):
            if word[i] == letter:
                new_mask += letter
            else:
                new_mask += masked_word[i]
        masked_word = new_mask
    else:
        wrong += 1
        draw_gallows()


def draw_gallows():
    try:
        with open(f"gallows/{wrong}.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except:
        pass


def is_win():
    return masked_word == word


def is_lose():
    return wrong >= max_wrong


def play(words_file):
    words = load_words(words_file)
    choose_word(words)

    while True:
        show_state()
        guess_letter()

        if is_win():
            print("Вы победили")
            print("Слово:", word)
            break

        if is_lose():
            print("Вы проиграли")
            print("Слово:", word)
            break
