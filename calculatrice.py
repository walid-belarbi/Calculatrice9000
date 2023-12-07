def menu():
    print('\n')
    print("Choice 1: Lancez la Calculatrice")
    print("Choice 2: Affichez l'historique")
    print("Choice 3: Supprimer history")
    print("Choice 4: quitter")
    
def calculator():
    history = []

    while True:
        menu()
        choice = input("Entrez votre choix (1-4): ")

        if choice == '1':
            calculatrice(history)
        elif choice == '2':
            show_history(history)
        elif choice == '3':
            delete_history(history)
        elif choice == '4':
            print("Vous quittez la calculatrice. Au revoir!")
            break
        else:
            print("Erreur: Entrez un nombre entre 1 et 4.")


def calculatrice(history):
    try:
        nombre1 = float(input("Entrez le premier nombre: "))
        operateur = input("Entrez l'opérateur (+, -, *, /): ")
        nombre2 = float(input("Entrez le deuxième nombre: "))

        if operateur == '+':
            resultat = nombre1 + nombre2
        elif operateur == '-':
            resultat = nombre1 - nombre2
        elif operateur == '*':
            resultat = nombre1 * nombre2
        elif operateur == '/':
            if nombre2 == 0:
                raise ZeroDivisionError("Division par zéro impossible.")
            resultat = nombre1 / nombre2
        else:
            raise ValueError("Opérateur invalide. Utilisez l'un des opérateurs suivants : +, -, *, /")
        
        

        history.append(f"{nombre1} {operateur} {nombre2} est : {resultat}")
        print("Le Resultat est", resultat)
        
    except ValueError as ve:
        print(f"Erreur: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erreur: {zde}")
    except Exception as e:
        print(f"Erreur: {e}")
        
def show_history(history):
    print("\nHistorique:")
    for calc in history:
        print(calc)


def delete_history(history):
    history.clear()
    print("L'historique de la calculatrice a été supprimé")

calculator()