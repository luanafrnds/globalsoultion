for i in range(quantidade_desastres):
    print(f"\n--- Coletando dados para o desastre {i + 1} ---")


    tipos_desastre.append(input("Tipo de desastre (ex: incêndio, enchente): "))
    paises.append(input("País: "))
    cidades.append(input("Cidade: "))
    bairros.append(input("Bairro: "))
    ruas.append(input("Rua: "))


    total_pessoas_afetadas.append(int(input("Quantidade total de pessoas afetadas: ")))
    print("\n--- Quantidade de pessoas em cada categoria ---")
    criancas.append(int(input("Crianças: ")))
    adultos.append(int(input("Adultos: ")))
    idosos.append(int(input("Idosos: ")))
    mobilidade_reduzida.append(int(input("Pessoas com mobilidade reduzida: ")))
    feridos.append(int(input("Feridos: ")))

print("\n--- Coleta de dados concluída! ---")