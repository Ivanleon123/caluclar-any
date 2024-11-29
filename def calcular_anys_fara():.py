def calcular_anys_fara():
    # Demanar l'any actual
    any_actual = int(input("Any actual: "))

    # Inicialitzar llistes per noms i anys de naixement
    noms = []
    naixements = []

    # Demanar noms i anys de naixement per 4 persones
    for i in range(4):
        nom = input(f"Nom de la persona {i + 1}: ")
        any_naixement = int(input(f"Any de naixement de {nom}: "))
        
        noms.append(nom)
        naixements.append(any_naixement)

    # Imprimir capçalera
    print("\nNom\t\tData naixement\tAnys que farà aquest any")
    print("-" * 50)

    # Calcular i imprimir els anys que farà cada persona
    for i in range(4):
        anys_fara = any_actual - naixements[i]
        print(f"{noms[i]}\t\t{naixements[i]}\t\t{anys_fara}")

# Executar el programa
calcular_anys_fara()