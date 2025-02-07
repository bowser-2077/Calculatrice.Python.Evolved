import random
def menu_math():

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Liste Des Operateur Possible
    print("Calculatrice🧮")
    operation = input("Entré Une Operation(+ - x / **):") #Ne Pas Espacez sinon il yaura une erreur
    num1 = float(input("Entrer Un Nombre: "))
    num2 = float(input("Entrer Un Autre Nombre: "))

#Addition
    if operation == "+":
        resultat = num1 + num2
        print("🟰")
        print(round(resultat, 3)) #Arrondir le Resultat a 3 si c'est en virgule (Vous Pouvez Le Modifiez )
#Soustraction
    elif operation == '-':
        resultat = num1 - num2
        print("🟰")
        print(round(resultat, 3))    #Arrondir le Resultat a 3 si c'est en virgule (Vous Pouvez Le Modifiez )
#Multiplication
    elif operation == 'x':
        resultat = num1 * num2
        print("🟰")
        print(round(resultat, 3)) #Arrondir le Resultat a 3 si c'est en virgule (Vous Pouvez Le Modifiez )
#Division
    elif operation == '/':
        resultat = num1 / num2
        print("🟰")
        print(round(resultat, 3))     #Arrondir le Resultat a 3 si c'est en virgule (Vous Pouvez Le Modifiez )
#Puissance
    elif operation == '**':
        resultat = num1 ** num2
        print("🟰")
        print(round(resultat, 3)) #Arrondir le Resultat a 3 si c'est en virgule (Vous Pouvez Le Modifiez )
    else:
        print(f"Erreur 404 {operation} est Invalide Veuillez Ressayer")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def CalculMentale():
    print("🧠🔢Calcul Mentale🧠🔢")
    while True:
        print("1.Facile🟩")
        print("2.Intermediaire🟨")
        print("3.Difficile🟧")
        print("4.Génie🟥")
        print("5.Retour↪️")
        choix = input("🌀Choississez La Difficulté : ")

        if choix == "1":
            Facile()
        elif choix == "2":
            Intermediaire()
        elif choix == "3":
            Difficile()
        elif choix == "4":
            Génie()
        elif choix == "5":
            Retour()
        else:
            print("❌ Option invalide, Ressayez encore.")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Facile():
    print(f"Difficulté 🟩Facile🟩 Est Choisi")


    def generer_exercice():
        """Génère un exercice de mathématique aléatoire"""
        operations = ["+", "-"] #Configurable Vous Pouvez Enlevez Ou Ajoutez Des Operations
        op = random.choice(operations)  # Choisir une opération aléatoire
        num1 = random.randint(0, 10)  # Configurable Nombre aleatoire pour num1
        num2 = random.randint(0, 10)  # Configurable Nombre aleatoire pour num2

        if op == "/":  # Assurer que la division donne un nombre entier
            while num1 % num2 != 0:  # On veut éviter les divisions avec reste
                num1 = random.randint(1, 10) # Configurable Nombre aleatoire pour num2
                num2 = random.randint(1, 10) # Configurable Nombre aleatoire pour num2

        question = f"{num1} {op} {num2}"
        reponse = eval(question)  # Calculer la réponse
        return question, reponse

    # Demander combien d'exercices l'utilisateur veut (max 100)
    while True:
        try:
            nb_exercices = int(input("💠Combien d'exercices voulez-vous ? (max 100) : "))
            if 1 <= nb_exercices <= 100:  # Configurable au dela de 100 si vous le souhaitez
                break
            else:
                print("❌ Veuillez entrer un nombre minimum 1 ")
        except ValueError:
            print("❌ Entrée invalide, veuillez entrer un nombre entier.")

    score = 0  # Score de l'utilisateur

    # Générer et poser les exercices
    for i in range(nb_exercices):
        question, reponse_correcte = generer_exercice()
        while True:
            try:
                reponse_utilisateur = float(input(f"Exercice {i + 1}: {question} = "))
                if reponse_utilisateur == reponse_correcte:
                    print("✅ Correct !")
                    score += 1
                else:
                    print(f"❌ Faux ! La bonne réponse était {reponse_correcte}.")
                break
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")

    # Afficher le score final
    print(f"\n🎯 Vous avez obtenu {score}/{nb_exercices} bonnes réponses !")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Intermediaire():
        print(f"Difficulté 🟨Intermediaire🟨 Est Choisi")

        def generer_exercice():
            """Génère un exercice de mathématique aléatoire"""
            operations = ["+", "-", "*"]  # Configurable Vous Pouvez Enlevez Ou Ajoutez Des Operations
            op = random.choice(operations)  # Choisir une opération aléatoire
            num1 = random.randint(0, 50)  # Configurable Nombre aleatoire pour num1
            num2 = random.randint(0, 50)  # Configurable Nombre aleatoire pour num2

            if op == "/":  # Assurer que la division donne un nombre entier
                while num1 % num2 != 0:  # On veut éviter les divisions avec reste
                    num1 = random.randint(1, 50)  # Configurable Nombre aleatoire pour num2
                    num2 = random.randint(1, 50)  # Configurable Nombre aleatoire pour num2

            question = f"{num1} {op} {num2}"
            reponse = eval(question)  # Calculer la réponse
            return question, reponse

        # Demander combien d'exercices l'utilisateur veut (max 100)
        while True:
            try:
                nb_exercices = int(input("💠Combien d'exercices voulez-vous ? (max 100) : "))
                if 1 <= nb_exercices <= 100:  # Configurable au dela de 100 si vous le souhaitez
                    break
                else:
                    print("❌ Veuillez entrer un nombre minimum 1 ")
            except ValueError:
                print("❌ Entrée invalide, veuillez entrer un nombre entier.")

        score = 0  # Score de l'utilisateur

        # Générer et poser les exercices
        for i in range(nb_exercices):
            question, reponse_correcte = generer_exercice()
            while True:
                try:
                    reponse_utilisateur = float(input(f"Exercice {i + 1}: {question} = "))
                    if reponse_utilisateur == reponse_correcte:
                        print("✅ Correct !")
                        score += 1
                    else:
                        print(f"❌ Faux ! La bonne réponse était {reponse_correcte}.")
                    break
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide.")

        # Afficher le score final
        print(f"\n🎯 Vous avez obtenu {score}/{nb_exercices} bonnes réponses !")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Difficile():
        print(f"Difficulté 🟧Difficile🟧 Est Choisi")

        def generer_exercice():
            """Génère un exercice de mathématique aléatoire"""
            operations = ["+", "-", "*","/"]  # Configurable Vous Pouvez Enlevez Ou Ajoutez Des Operations
            op = random.choice(operations)  # Choisir une opération aléatoire
            num1 = random.randint(1, 200)  # Configurable Nombre aleatoire pour num1
            num2 = random.randint(1, 200)  # Configurable Nombre aleatoire pour num2

            if op == "/":  # Assurer que la division donne un nombre entier
                while num1 % num2 != 0:  # On veut éviter les divisions avec reste
                    num1 = random.randint(1, 200)  # Configurable Nombre aleatoire pour num2
                    num2 = random.randint(1, 200)  # Configurable Nombre aleatoire pour num2

            question = f"{num1} {op} {num2}"
            reponse = eval(question)  # Calculer la réponse
            return question, reponse

        # Demander combien d'exercices l'utilisateur veut (max 100)
        while True:
            try:
                nb_exercices = int(input("💠Combien d'exercices voulez-vous ? (max 100) : "))
                if 1 <= nb_exercices <= 100:  # Configurable au dela de 100 si vous le souhaitez
                    break
                else:
                    print("❌ Veuillez entrer un nombre minimum 1 ")
            except ValueError:
                print("❌ Entrée invalide, veuillez entrer un nombre entier.")

        score = 0  # Score de l'utilisateur

        # Générer et poser les exercices
        for i in range(nb_exercices):
            question, reponse_correcte = generer_exercice()
            while True:
                try:
                    reponse_utilisateur = float(input(f"Exercice {i + 1}: {question} = "))
                    if reponse_utilisateur == reponse_correcte:
                        print("✅ Correct !")
                        score += 1
                    else:
                        print(f"❌ Faux ! La bonne réponse était {reponse_correcte}.")
                    break
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide.")

        # Afficher le score final
        print(f"\n🎯 Vous avez obtenu {score}/{nb_exercices} bonnes réponses !")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Génie():
    print(f"Difficulté 🟥Genie🟥 Est Choisi")

    def generer_exercice():
        """Génère un exercice de mathématique aléatoire"""
        operations = ["+", "-", "*", "/","**"]  # Configurable Vous Pouvez Enlevez Ou Ajoutez Des Operations
        op = random.choice(operations)  # Choisir une opération aléatoire
        num1 = random.randint(1, 1000)  # Configurable Nombre aleatoire pour num1
        num2 = random.randint(1, 1000)  # Configurable Nombre aleatoire pour num2

        if op == "/":  # Assurer que la division donne un nombre entier
            while num1 % num2 != 0:  # On veut éviter les divisions avec reste
                num1 = random.randint(1, 1000)  # Configurable Nombre aleatoire pour num2
                num2 = random.randint(1, 1000)  # Configurable Nombre aleatoire pour num2

            # Assurer que la puissance ne soit pas trop grande
        if op == "**":
            num2 = random.randint(2, 3)  # On limite la puissance à 2 ou 3 pour éviter des nombres énormes
        question = f"{num1} {op} {num2}"
        reponse = eval(question)  # Calculer la réponse
        return question, reponse

    # Demander combien d'exercices l'utilisateur veut (max 100)
    while True:
        try:
            nb_exercices = int(input("💠Combien d'exercices voulez-vous ? (max 100) : "))
            if 1 <= nb_exercices <= 100:  # Configurable au dela de 100 si vous le souhaitez
                break
            else:
                print("❌ Veuillez entrer un nombre minimum 1 ")
        except ValueError:
            print("❌ Entrée invalide, veuillez entrer un nombre entier.")

    score = 0  # Score de l'utilisateur

    # Générer et poser les exercices
    for i in range(nb_exercices):
        question, reponse_correcte = generer_exercice()
        while True:
            try:
                reponse_utilisateur = float(input(f"Exercice {i + 1}: {question} = "))
                if reponse_utilisateur == reponse_correcte:
                    print("✅ Correct !")
                    score += 1
                else:
                    print(f"❌ Faux ! La bonne réponse était {reponse_correcte}.")
                break
            except ValueError:
                print("❌ Veuillez entrer un nombre valide.")

    # Afficher le score final
    print(f"\n🎯 Vous avez obtenu {score}/{nb_exercices} bonnes réponses  !")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

A = ["Ne triche pas avec ta calculatrice, elle sait tout... mais pas toi !",
"Les erreurs font partie du calcul, mais corrige-les avant le résultat final.",
"Les maths, c'est magique : un problème, une formule, et hop, une solution !",
"Utilise ta tête avant ta calculette, elle a plus de mémoire qu'elle !",
"Les maths, c'est comme un sport : plus tu pratiques, plus tu deviens fort !",
"Les maths, ce n'est pas juste trouver la réponse, c'est comprendre comment y arriver.",
"Les chiffres ne mentent pas... mais toi, tu peux te tromper, alors vérifie !",
"Un bon raisonnement vaut mieux qu’un calcul rapide et faux.",
"Chercher une solution, c'est déjà faire la moitié du travail en maths.",
"J'espere Que Tu Ne Triche Pas Avec Une Calculatrice :) ", "E = Mc² ",
"Les maths, c’est comme les légumes : c’est bon pour toi, mais tu n’as pas envie d’en faire.",
"Je voulais être bon en maths… puis j’ai vu la gueule des fractions.",
"Diviser par zéro, c’est comme manger de la soupe avec une fourchette… ça sert à rien.",
"En maths comme en amour, une petite erreur de calcul et c’est la chute libre.",
"En maths, j’ai toujours eu la moyenne… du tiers inférieur de la classe.",
"Ma note en maths ressemble à une fonction exponentielle… mais dans le mauvais sens.",
"Faire des maths en été, c’est comme faire du feu dans un désert… ça sert à rien et ça fait mal.",
"Mon prof de maths m’a dit ‘Tu finiras par comprendre’… J’espère que c’est pas sur mon lit de mort.",
"Les maths, c'est simple : soit tu réussis, soit tu pleures en regardant ta copie.",
"Ma note en maths est tellement basse qu’elle est six pieds sous terre.",
"Mes résultats en maths ressemblent à la Bourse de 1929… une chute libre sans retour.",
"J’ai essayé de résoudre une équation… maintenant elle est inscrite sur ma pierre tombale.",
"Si un jour je disparais, cherchez-moi sous ma pile de devoirs de maths.",
"Mon prof m’a dit ‘Les maths, c’est la vie’… Maintenant je comprends pourquoi j’ai envie d’en finir.",
"Les maths, c’est comme une maladie incurable… sauf que personne ne cherche de remède.",
"Les intégrales m’ont vidé de mon énergie… et bientôt de mon sang.","➡️ https://guns.lol/jexorvoid ⬅️",
"Mon cerveau a tenté de comprendre un problème… il est actuellement en soins intensifs.",
"J’ai voulu faire un exercice de maths… maintenant je suis en PLS dans un coin de la pièce.",
"Les maths ne m’ont pas encore tué… mais elles s’acharnent.","Regarde Mes Autres Projets Posté Sur Github : BuingDavidTheStyle","Mon Discord: buinggamer ",
"Fait Moi Un Don Pour Me Soutenir Stv ! ","Paye 29.99$ avec -10% de reduction pour debloquer toutes les fonctionnalité (Non je blague c'est gratuit F-R-E-E)",
"Quesqui est Jaune Et qui attend ?","ERROR 404 Please Check Your Connection And Restart (:"
]


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Retour():
    print("Vous Avez Choisi 'Retour↪️'")
    while True:
        print("\n📌 MENU PRINCIPAL")
        print("▶️Selectionnez Une option: 1 , 2 ou 3")
        print("1.Calculatrice🧮")
        print("2.🧠🔢Calcul Mentale🧠🔢")
        print("3.Quitter❌")
        print(random.choice(A))
        print(random.choice(A))
        print("Credit: B.David, 2025 ")
        choix = input("Choisissez une option ❓ : ")

        if choix == "1":
            menu_math()
        elif choix == "2":
            CalculMentale()
        elif choix == "3":
            quit()
        else:
            print("❌ Option invalide, Ressayez encore.")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
while True:
    print("\n📌 MENU PRINCIPAL")
    print("▶️Selectionnez Une option: 1 , 2 ou 3")
    print("1.Calculatrice🧮")
    print("2.🧠🔢Calcul Mentale🧠🔢")
    print("3.Quitter❌")
    print(random.choice(A))
    print(random.choice(A))
    print("Credit: B.David ")
    choix = input("Choisissez une option ❓ : ")

    if choix == "1":
        menu_math()
    elif choix == "2":
        CalculMentale()
    elif choix == "3":
        print("👋 Au revoir !")
        break
    else:
        print("❌ Option invalide, Ressayez encore.")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#