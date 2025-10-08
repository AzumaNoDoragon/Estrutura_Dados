
class Aluno:
    def __init__(self, nome: str, notas: list[float]):
        self.nome = nome
        self.notas = notas
        self.media = sum(notas) / len(notas) if notas else 0.0

def ler_float_list(msg: str, quantidade: int) -> list[float]:
    while True:
        try:
            linha = input(msg).strip()
            partes = linha.replace(",", ".").split()
            if len(partes) != quantidade:
                print(f"Por favor, informe exatamente {quantidade} notas separadas por espaço.")
                continue
            return [float(p) for p in partes]
        except ValueError:
            print("Entrada inválida. Use números (ex.: 7.5 8 9).")
    return []

def main():
    # Quantos alunos e quantas notas?
    while True:
        try:
            n = int(input("Quantos alunos? ").strip())
            if n <= 0:
                print("Informe um inteiro positivo.")
                continue
            break
        except ValueError:
            print("Informe um inteiro válido.")
    while True:
        try:
            m = int(input("Quantas notas por aluno? ").strip())
            if m <= 0:
                print("Informe um inteiro positivo.")
                continue
            break
        except ValueError:
            print("Informe um inteiro válido.")

    turma: list[Aluno] = []

    # Entrada de dados
    for i in range(n):
        nome = input(f"Nome do aluno {i+1}: ").strip()
        notas = ler_float_list(f"Digite {m} nota(s) de {nome}, separadas por espaço: ", m)
        turma.append(Aluno(nome, notas))

    # Media da turma
    media_turma = sum(a.media for a in turma) / n if n else 0.0

    # Saída formatada (nao soube fazer uma formatacao bonita, usei muito do GPT aqui)
    print("\n=== RESULTADOS ===")
    largura_nome = max([len(a.nome) for a in turma] + [4])  # pelo menos "Nome"
    cabecalho = f"{'Nome'.ljust(largura_nome)}  Notas{' '*(3*m-5)}  Média"
    print(cabecalho)
    print("-" * (len(cabecalho)))

    for a in turma:
        notas_str = " ".join(f"{x:.2f}" for x in a.notas)
        print(f"{a.nome.ljust(largura_nome)}  {notas_str}  {a.media:.2f}")

    print(f"\nMédia da turma: {media_turma:.2f}")

if __name__ == "__main__":
    main()


