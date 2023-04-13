"""
MASTER MIND

l'ordi choisit un mot dans une liste

TANT QUE mot pas trouver ou trop de tour:
    copie = mot a trouver
    in_good = 0
    in_bad = 0
    out = 0
    le joueur rentre une combinaison de lettre
        verif que l'input
            que des lettre
            autant de lettre que dans le mot a trouver

    SI verif:
        pour chaque lettre de l'utilisateur
            SI presente dans copie mot a trouver
                bien placer +1
                mal placer +0
            enlever la lettre de la copie

            SINON
                pas presente +0

        indiquer au joueur combien de lettre son bonne et bien placé (in_good)
                                                bonne et mal placé (in_bad)
                                                pas bonne(out)
"""
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
    return f'- - - - -\nlettre bien placé(s): {in_good}\nlettre mal placé(s): {in_bad}\nlettre pas dans le mot: {out}\n- - - - -'


def print_word_used(list_of_words):
    for i in range(len(list_of_words)):
        print(list_of_words[i])
    # print("- - - - -")


def verify_letter_placement(letter, letter_compare):
    """
    renvoi True si la lettre est bien place,
    sinon false
    """
    return letter == letter_compare


def verify_a_word(word, word_compare):
    """
    compare la longueur de deux mots, si le premier est composé de lettre et sans espace
    """
    good_lenght = len(word) == len(word_compare)
    good_char = word.isalpha()
    no_space = " " not in word
    return good_lenght and good_char and no_space


def pick_a_word():
    liste_mot = [
        "age",
        "aller",
        "ami",
        "amour",
        "animaux",
        "appareil",
        "apprendre",
        "arbre",
        "argent",
        "art",
        "attention",
        "avant",
        "avenir",
        "avis",
        "beau",
        "besoin",
        "bon",
        "bout",
        "bruit",
        "cadeau",
        "campagne",
        "caractere",
        "carte",
        "cause",
        "celebre",
        "changement",
        "chanson",
        "choix",
        "chute",
        "cigarette",
        "ciel",
        "cinema",
        "client",
        "cœur",
        "coin",
        "colere",
        "compte",
        "copain",
        "corps",
        "couleur",
        "coup",
        "courir",
        "creer",
        "crise",
        "danger",
        "decouvrir",
        "decision",
        "dehors",
        "depart",
        "developper",
        "difficile",
        "diriger",
        "discussion",
        "droit",
        "durer",
        "echec",
        "ecole",
        "ecrire",
        "effet",
        "enfance",
        "enfants",
        "environ",
        "esprit",
        "essayer",
        "etat",
        "etudiant",
        "excellent",
        "faire",
        "famille",
        "fête",
        "fois",
        "français",
        "froid",
        "garder",
        "genre",
        "gouvernement",
        "grand",
        "gratuit",
        "habitude",
        "heure",
        "histoire",
        "hiver",
        "homme",
        "idee",
        "image",
        "impossible",
        "interessant",
        "jardin",
        "jeu",
        "joie",
        "journee",
        "laisser",
        "leçon",
        "lire",
        "livre",
        "loin",
        "longtemps",
        "main",
        "malheureux",
        "manquer",
        "mari",
        "matin",
        "mauvais",
        "mieux",
        "monde",
        "mot",
        "musique",
        "nouveau",
        "nuit",
        "objectif",
        "oeil",
        "oiseau",
        "oncle",
        "oublier",
        "parler",
        "partir",
        "passe",
        "pays",
        "penser",
        "personne",
        "peur",
        "photo",
        "pied",
        "plan",
        "plupart",
        "pouvoir",
        "premier",
        "prix",
        "probleme",
        "professeur",
        "quitter",
        "rapport",
        "regarder",
        "rester",
        "salle",
        "sante",
        "savoir",
        "sentiment",
        "seul",
        "silence",
        "soir",
        "sortir",
        "souffrir",
        "souvenir",
        "temps",
        "travailler",
        "trouver",
        "type",
        "vacances",
        "vent",
        "verite",
        "ville",
        "vivre",
        "voiture",
        "voix"]
    index = random.randint(0, len(liste_mot) - 1)
    return liste_mot[index]


master_mind()
