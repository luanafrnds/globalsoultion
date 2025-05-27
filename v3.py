print("\n--- Relatório de Todos os Desastres Registrados ---")
for i in range(quantidade_desastres):
    print(f"\n--- Desastre {i + 1} ---")
    print(f"Tipo de desastre: {tipos_desastre[i]}")
    print(f"País: {paises[i]}")
    print(f"Cidade: {cidades[i]}")
    print(f"Bairro: {bairros[i]}")
    print(f"Rua: {ruas[i]}")
    print(f"Total de pessoas afetadas: {total_pessoas_afetadas[i]}")
    print(f"Número de crianças: {criancas[i]}")
    print(f"Número de adultos: {adultos[i]}")
    print(f"Número de idosos: {idosos[i]}")
    print(f"Número de pessoas com mobilidade reduzida: {mobilidade_reduzida[i]}")
    print(f"Número de feridos: {feridos[i]}")


total_geral_afetados = sum(total_pessoas_afetadas)


total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade_reduzida = sum(mobilidade_reduzida)
total_feridos = sum(feridos)


categorias_afetadas = {
    "Crianças": total_criancas,
    "Adultos": total_adultos,
    "Idosos": total_idosos,
    "Mobilidade reduzida": total_mobilidade_reduzida,
    "Feridos": total_feridos
}


print("\n--- INÍCIO DA ANÁLISE DE DADOS ---")

print(f"\nTotal de desastres registrados: {quantidade_desastres}")


total_geral_afetados = sum(total_pessoas_afetadas)
print(f"Total geral de pessoas afetadas em todos os desastres: {total_geral_afetados}")

total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade_reduzida = sum(mobilidade_reduzida)
total_feridos = sum(feridos)

print("\nTotal de Pessoas por Categoria:")
print(f"  Crianças: {total_criancas}")
print(f"  Adultos: {total_adultos}")
print(f"  Idosos: {total_idosos}")
print(f"  Pessoas com mobilidade reduzida: {total_mobilidade_reduzida}")
print(f"  Feridos: {total_feridos}")


categorias_afetadas = {
    "Crianças": total_criancas,
    "Adultos": total_adultos,
    "Idosos": total_idosos,
    "Pessoas com mobilidade reduzida": total_mobilidade_reduzida,
    "Feridos": total_feridos
}

categoria_mais_afetada = "Nenhuma"
if categorias_afetadas:

    categoria_mais_afetada = max(categorias_afetadas, key=categorias_afetadas.get)
    print(f"\nCategoria mais afetada no geral: {categoria_mais_afetada} (Total: {categorias_afetadas[categoria_mais_afetada]})")
else:
    print("\nNão foi possível identificar a categoria mais afetada (sem dados).")



print(f"\n--- Desastre com o MAIOR NÚMERO de Afetados ---")
if total_pessoas_afetadas: # Garante que há desastres registrados

    indice_maior_afetados = total_pessoas_afetadas.index(max(total_pessoas_afetadas))

    print(f"Tipo de desastre: {tipos_desastre[indice_maior_afetados]}")
    print(f"Total de pessoas afetadas: {total_pessoas_afetadas[indice_maior_afetados]}")
    print(f"Local: {ruas[indice_maior_afetados]}, {bairros[indice_maior_afetados]}, {cidades[indice_maior_afetados]}, {paises[indice_maior_afetados]}")
else:
    print("Não há desastres registrados para identificar o de maior número de afetados.")

print("\n--- FIM DA ANÁLISE DE DADOS ---")

