def menu():
    print('\n')
    print("Choice 1: Lancez la calculatrice")
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
        expression = input("Entrez une expression mathématique : ")

        # Supprimer les espaces pour simplifier l'analyse
        expression = expression.replace(" ", "")

        # Utiliser une approche d'analyse syntaxique pour évaluer l'expression
        resultat = evaluer_expression(expression)

        # Afficher le résultat
        history.append(f" {expression} = {resultat}")
        print(f"Le résultat de l'expression {expression} est égal à {resultat}")

    except ValueError:
        print("Erreur : Veuillez entrer une expression mathématique valide.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro n'est pas autorisée.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

def evaluer_expression(expression):
    operateurs = []
    valeurs = []
    index = 0

    while index < len(expression):
        if expression[index].isdigit() or (index == 0 and expression[index] == '-'):
            # Si le caractère est un chiffre ou un signe moins au début, obtenir la valeur numérique complète
            valeur = ""
            while index < len(expression) and (expression[index].isdigit() or expression[index] == '.'):
                valeur += expression[index]
                index += 1
            valeurs.append(float(valeur))
        elif expression[index] in "+-*/":
            # Si le caractère est un opérateur, traiter les opérations avec une priorité plus élevée
            while (operateurs and priorite(operateurs[-1]) >= priorite(expression[index])):
                effectuer_operation(valeurs, operateurs)
            operateurs.append(expression[index])
            index += 1
        elif expression[index] == '(':
            # Si le caractère est une parenthèse ouvrante, traiter récursivement l'expression à l'intérieur
            sous_expression, index = extraire_sous_expression(expression, index)
            valeur_sous_expression = evaluer_expression(sous_expression)
            valeurs.append(valeur_sous_expression)
        elif expression[index] == ')':
            # Ignorer les parenthèses fermantes, elles seront traitées par les opérations précédentes
            index += 1
        else:
            raise ValueError("Caractère non valide dans l'expression : " + expression[index])

    # Traiter les opérations restantes
    while operateurs:
        effectuer_operation(valeurs, operateurs)

    return valeurs[0]

def priorite(operateur):
    if operateur in "+-":
        return 1
    elif operateur in "*/":
        return 2
    return 0

def effectuer_operation(valeurs, operateurs):
    operateur = operateurs.pop()
    nombre2 = valeurs.pop()
    nombre1 = valeurs.pop()
    if operateur == '+':
        valeurs.append(nombre1 + nombre2)
    elif operateur == '-':
        valeurs.append(nombre1 - nombre2)
    elif operateur == '*':
        valeurs.append(nombre1 * nombre2)
    elif operateur == '/':
        if nombre2 == 0:
            raise ZeroDivisionError("Division par zéro n'est pas autorisée.")
        valeurs.append(nombre1 / nombre2)
        

def extraire_sous_expression(expression, index):
    count_parentheses = 1
    sous_expression = ""

    start_index = index + 1

    while count_parentheses > 0 and index < len(expression) - 1:
        index += 1
        if expression[index] == '(':
            count_parentheses += 1
        elif expression[index] == ')':
            count_parentheses -= 1

    if count_parentheses == 0:
        sous_expression = expression[start_index:index]
    else:
        raise ValueError("Parenthèses non équilibrées dans l'expression")

    return sous_expression, index

def show_history(history):
    print("\nHistorique:")
    for calc in history:
        print(calc)


def delete_history(history):
    history.clear()
    print("L'historique de la calculatrice a été supprimé")

calculator()