nomes = list(input("Digite os nomes: ").split())
total_nomes = len(nomes)

nota_total = []

for i in nomes:
    
    nota_por_aluno = []

    for i in range(3):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas_por_aluno.append(nota)

    notas_totais.append(notas_por_aluno)

for i in range(len(nomes)):
    print(f"{nomes[i]} ficou com as notas: {notas_dos_alunos[i]}")
