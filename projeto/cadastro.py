dados = []
banco_dados = []

while True:
    dados.clear()
    dados.append(input("Nome: "))
    dados.append(int(input("Idade: ")))
    while True:
        genero = str(input("Qual o seu genero? ")).strip().upper()[0]
    
        if genero == "M" or "F":
            
            if genero == "M":
                dados.append(genero)
                break
        
            elif genero == "F":
                dados.append(genero)
                break
    banco_dados.append(dados.copy())
        

    stop = str(input("Quer continuar [S/N]")).strip().upper()[0]
    if stop == "S" or "N":
        
        if stop == "S":
            print("proximo")

        elif stop == "N":
            break
    
        else:
            print("Dado invalido")
            break

