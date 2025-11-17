import streamlit as st
from binarytree import Node
from collections import deque
import random
import matplotlib.pyplot as plt

### Funções de inicialização e modularização do código ###
def slideBar(min, max, value, stepMove, text = "Escolha a quantidade de jogos:") -> tuple[int, int, int]:
    """Cria um slider no Streamlit com os parâmetros recebidos."""
    return st.slider(text, min, max, value, step=stepMove)

def anosMinMax(dados) -> tuple[int, int]:
    """Retorna o menor e o maior ano encontrados em uma lista de dicionários JSON."""
    anos = []

    for jogo in dados:
        ano = jogo.get("Year")
        if isinstance(ano, (int, float)):
            anos.append(int(ano))
        elif isinstance(ano, str) and ano.isdigit():
            anos.append(int(ano))

    if anos:
        menor_ano = min(anos)
        maior_ano = max(anos)
    else:
        menor_ano = maior_ano = None
    
    return menor_ano, maior_ano

def menu() -> str:
    """Exibe o menu de seleção principal dentro de um expander."""
    with st.expander("Mostrar opções"):
        escolha = st.radio(
            "Selecione o que deseja fazer:", [
                "Informações Gerais",
                "Listas (list)",
                "Fila (deque)",
                "Tabela Hash (Hashing)",
                "Árvore Binária de Busca (BST)"
            ]
        )
    return escolha

### Funções de estrutura do código ###
def carregarInfoGerais(dados):
    """Exibe informações básicas da base de dados (tamanho, colunas, amostra)."""
    st.subheader("Informações Gerais")
    st.write("Número total de linhas:", len(dados))
    st.write("Número total de colunas:", len(list(dados[0].keys())))
    st.write("Colunas principais:", list(dados[0].keys()))
    st.write("5 primeiras linhas:", dados[:5])

def lista(dados):
    """Ordena e exibe os jogos mais vendidos utilizando uma lista."""
    nJogos = slideBar(10, 200, 100, 5)

    jogosOrganizados = sorted(dados, key=lambda x: float(x["Global_Sales"]), reverse=True)
    maisVendidos = []
    for jogo in jogosOrganizados[:nJogos]:
        maisVendidos.append(jogo["Name"])
    
    st.subheader("Lista")
    st.write("Os jogos mais vendidos foram:", maisVendidos)

def fila(dados):
    """Permite organizar e visualizar os jogos dentro de uma fila (deque)."""
    def buttonMenu() -> str:
        """Submenu interno para escolher o tipo de ordenação"""
        with st.expander("Mostrar opções"):
            escolha = st.radio(
                "Selecione como deseja organizar:", [
                    "Por vendas globais crescente",
                    "Por vendas globais decrescente",
                    "Por Ano de lançamento crescente",
                    "Por Ano de lançamento decrescente",
                    "Por nome em ordem alfabetica crescente",
                    "Por nome em ordem alfabetica decrescente"
                ]
            )
        return escolha
    
    def ordenaPor(chave, ordem, tipo = float):
        """Função auxiliar para ordenação"""
        try:
            return sorted(filaJogos, key=lambda x: tipo(x[chave]), reverse=ordem)
        except Exception as e:
            st.error(f"Erro ao executar: {e}")

    menorAno, maiorAno = anosMinMax(dados)
    if menorAno and maiorAno:
        anoJogos = slideBar(menorAno, maiorAno, (menorAno, maiorAno), 1, "Selecione o intervalo de anos:")
    
    nJogos = slideBar(5, 100, 50, 5)

    # Criação da fila filtrando jogos pelo ano
    filaJogos = deque()
    for jogo in dados:
        lancado = jogo.get("Year")
        if isinstance(lancado, (int, float)) and anoJogos[0] <= lancado <= anoJogos[1]:
            filaJogos.append({
                "Name": jogo["Name"],
                "Year": jogo["Year"],
                "Global_Sales": jogo["Global_Sales"]
            })

    # Escolha de ordenação e exibição
    button = buttonMenu()
    if button == "Por vendas globais crescente":
        ordenado = ordenaPor("Global_Sales", False)
    elif button == "Por vendas globais decrescente":
        ordenado = ordenaPor("Global_Sales", True)
    elif button == "Por Ano de lançamento crescente":
        ordenado = ordenaPor("Year", False)
    elif button == "Por Ano de lançamento decrescente":
        ordenado = ordenaPor("Year", True)
    elif button == "Por nome em ordem alfabetica crescente":
        ordenado = ordenaPor("Name", False, str)
    elif button == "Por nome em ordem alfabetica decrescente":
        ordenado = ordenaPor("Name", True, str)

    st.subheader("Fila")
    st.write("Os jogos mais vendidos foram:", list(ordenado)[:nJogos])

def tabelaHash(dados):
    """Simula uma tabela hash simples com inserção e busca de jogos."""
    def inserir(jogo, valor) -> int:
        """Insere um par (chave, valor) na tabela."""
        colisoes = 0
        indice = hash(jogo) % tamHash
        if tabela[indice]:
            colisoes += 1
        tabela[indice].append((jogo, valor))
        return colisoes
    
    def buscar(jogo) -> list:
        """Busca um valor associado à chave (nome do jogo)."""
        indice = hash(jogo) % tamHash
        tabelaJogosEncontrados = []
        for nome, infoJogo in tabela[indice]:
            if nome == jogo:
                tabelaJogosEncontrados.append((nome, infoJogo))
        return tabelaJogosEncontrados
    
    tamHash = slideBar(100, 1000, 300, 5, "Tamanho da hash")
    nJogos = slideBar(100, len(dados), min(2500, len(dados)), 5)
    
    tabela = [[] for _ in range(tamHash)]
    colisoes = 0

    # Inserção dos jogos na tabela
    for jogo in dados[:nJogos]:
        colisoes += inserir(
            jogo["Name"],
            { 
                "Platform": jogo["Platform"],
                "Year": jogo["Year"],
                "Genre": jogo["Genre"],
                "Global_Sales": jogo["Global_Sales"],
            }
        )

    with st.expander("Informações adicionais"):
        st.write("Quantidade de colisões:", colisoes)
        st.write("Fator de carga:", round(nJogos / tamHash, 2))
        maior_bucket = max(tabela, key=lambda b: len(b))
        st.write("Tamanho do maior bucket:", len(maior_bucket))
        with st.expander("Mostrar maior bucket"):
            indice_maior_bucket = tabela.index(maior_bucket)
            st.write("Índice do maior bucket:", indice_maior_bucket)
            st.write(maior_bucket)

    # Busca ou exibição completa
    nomeJogo = st.text_input("Nome do jogo:", placeholder="Digite o nome exato do jogo")
    if nomeJogo:
        resultado = buscar(nomeJogo)
        if resultado:
            st.write("Jogo(s) encontrado(s):")
            st.write(resultado)
        else:
            st.warning("Jogo não encontrado.")
    else:
        st.subheader("Todos os jogos na tabela hash:")
        nomes = []
        for bucket in tabela:
            for nome, _ in bucket:
                nomes.append(nome)
        st.write("Jogos inseridos:", nomes)

def BTS(dados):
    """Cria e exibe uma árvore binária de busca baseada nos N jogos mais vendidos, porem em ordem aleatoria."""
    def insere(raiz, valor, nome):
        """Insere um novo nó na árvore com base em Global_Sales."""
        if raiz is None:
            return Node(f"{nome} ({valor})")  # nó armazena uma tupla: (Global_Sales, Name)
        
        valor_raiz = float(raiz.value.split("(")[-1].strip(")"))
        if valor < valor_raiz:
            raiz.left = insere(raiz.left, valor, nome)
        else:
            raiz.right = insere(raiz.right, valor, nome)
        return raiz
    
    # Contar nós folha
    def contar_folhas(no):
        if no is None:
            return 0
        if no.left is None and no.right is None:
            return 1
        return contar_folhas(no.left) + contar_folhas(no.right)

    nJogos = slideBar(5, 30, 15, 5)
    jogosOrdenados = sorted(dados, key=lambda x: float(x["Global_Sales"]), reverse=True)
    jogosTop = jogosOrdenados[:nJogos]
    random.shuffle(jogosTop)
    
    # Montagem da árvore
    raiz = None
    for jogo in jogosTop:
        valor = float(jogo["Global_Sales"])
        nome = jogo["Name"]
        raiz = insere(raiz, valor, nome)
    
    if raiz:
        folhas = contar_folhas(raiz)
        st.write(f"**Quantidade de nós folha:** {folhas}")
        st.write(f"**Altura da árvore:** {raiz.height}")
        st.subheader("Visualização da Árvore Binária de Busca (BST)")
        st.graphviz_chart(raiz.graphviz())
    else:
        st.error("Não foi possível construir a árvore. Verifique o formato dos dados.")

def main(opcao, dados):
    """Executa a lógica da aba 'Projeto Final' conforme a escolha do usuário."""
    if opcao != "Projeto Final":
        return

    st.title("Projeto Final")
    if dados is None:
        st.warning("Por favor, carregue o arquivo no menu lateral.")
        return
    escolha = menu()

    if escolha == "Informações Gerais":
        carregarInfoGerais(dados)

    elif escolha == "Listas (list)":
        lista(dados)
    
    elif escolha == "Fila (deque)":
        fila(dados)

    elif escolha == "Tabela Hash (Hashing)":
        tabelaHash(dados)
    
    elif escolha == "Árvore Binária de Busca (BST)":
        BTS(dados)
