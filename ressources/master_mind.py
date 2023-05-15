import random


def master_mind():
    hidden_word = pick_a_word()
    # print("le mot a trouver est:", hidden_word)
    find = False
    used_word = set()

    while not find:
        in_good = 0
        in_bad = 0
        out = 0
        # list_hidden_word = list(hidden_word)
        print(f"Entrez un mot de {len(hidden_word)} lettres:")
        user_word = input()
        verified_word = verify_a_word(user_word, hidden_word)
        if verified_word:
            used_word.add(user_word)

            for i in range(len(hidden_word)):
                if user_word[i] in hidden_word:
                    if verify_letter_placement(user_word[i], hidden_word[i]):
                        in_good += 1
                    else:
                        in_bad += 1
                else:
                    out += 1
            # print("\n".join(used_word))
            print(print_pos_letter(in_good, in_bad, out))
            if user_word == hidden_word:
                find = True
                print("Bravo champion")

        else:
            print("entree invalide")
    relance_jeu()


def relance_jeu():
    print('Voulez_vous rejouez ? O/N')
    rejouer = input().upper()
    if rejouer == "O":
        return master_mind()
    elif rejouer == "N":
        print("A bientot.")


def print_pos_letter(in_good, in_bad, out):
    return f'- - - - -\nlettre bien placé(s): {in_good}\
        \nlettre mal placé(s): {in_bad}\
        \nlettre pas dans le mot: {out}\n- - - - -'


def print_word_used(list_of_words):
    for i in range(len(list_of_words)):
        print(list_of_words[i])
    # print("- - - - -")


def verify_letter_placement(letter, letter_compare):
    """
    Renvoi True si la lettre est bien placé,
    sinon false
    """
    return letter == letter_compare


def verify_a_word(word, word_compare):
    """
    Compare la longueur de deux mots,
    si le premier est composé de lettre et sans espace
    """
    good_length = len(word) == len(word_compare)
    good_char = word.isalpha()
    no_space = " " not in word
    return good_length and good_char and no_space


def pick_a_word():
    """
    Pick French random word in file text
    """
    # index = random.randint(0, len(liste_mot) - 1)
    # return liste_mot[index]


master_mind()
