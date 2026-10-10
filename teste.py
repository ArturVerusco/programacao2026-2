nomes = input("Digite os nomes separados por espaço: ").split()
total_nomes = len(nomes)

notas_totais = []

for nome in nomes:
    print(f"\n--- Digite as 3 notas de {nome} ---")

    notas_por_aluno = []

    for i in range(3):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas_por_aluno.append(nota)

    notas_totais.append(notas_por_aluno)

print("\n=== Resultado Final ===")
for i in range(len(nomes)):
    print(f"{nomes[i]} ficou com as notas: {notas_totais[i]}")
