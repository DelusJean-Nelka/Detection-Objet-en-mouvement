import foregroundBackground
import camDetection
import os

# from comptage_objet.people_counter import comptage

def menu_principal():
    print("________________ MENU PRINCIPAL ___________________")
    print("1 - DETECTION DU MOUVEMENT ")
    print("2 - SUIVI AVEC LE FILTRE KALMAN ")
    print("3 - COMPTAGE DES OBJETS EN MOUVEMMENT")
    print("4 ou 'q' - QUITTER LE PROGRAMME ")


def sous_menu_detection_mouvement():
    print("________________ DETECTION DU MOUVEMENT ___________________")
    print("1 - MOG2 ")
    print("2 - KNN ")
    print("4 ou 'r' pour retourner au menu principal ")


def sous_menu_comptage_object():
    print("________________ COMPTAGE DES OBJETS ___________________")
    print("1 - COMPTAGE ")
    print("3 ou 'r' pour retourner au menu principal ")


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_principal()
    print("Choisissez un nombre : ")
    ch_menu = input()

    if ch_menu == '1':
        # os.system('cls' if os.name == 'nt' else 'clear')
        camDetection.cam_detection()
    elif ch_menu == '2':
        foregroundBackground.removeBackground()
    elif ch_menu == '3':
        print("menu 3")
    elif ch_menu == '4' or ch_menu == 'q':
        break

