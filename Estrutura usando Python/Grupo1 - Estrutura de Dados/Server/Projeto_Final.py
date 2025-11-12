import streamlit as st
from binarytree import Node
from collections import deque
import random

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
    """Retorna a escolha feita na aba de opções"""
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
    """Exibe informações básicas sobre a base de dados: 
        - 5 primeiras linhas 
        - Número total de linhas 
        - Número de colunas 
        - Lista das colunas principais"""
    st.subheader("Informações Gerais")
    st.write("Número total de linhas:", len(dados))
    st.write("Número total de colunas:", len(list(dados[0].keys())))
    st.write("Colunas principais:", list(dados[0].keys()))
    st.write("5 primeiras linhas:", dados[:5])

def lista(dados):
    nJogos = slideBar(10, 200, 100, 5)

    jogosOrganizados = sorted(dados, key=lambda x: float(x["Global_Sales"]), reverse=True)
    maisVendidos = []
    for jogo in jogosOrganizados[:nJogos]:
        maisVendidos.append(jogo["Name"])
    
    st.subheader("Lista")
    st.write("Os jogos mais vendidos foram:", maisVendidos)

def fila(dados):
    def buttonMenu() -> str:
        """Retorna a escolha feita na aba de opções"""
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
        try:
            return sorted(filaJogos, key=lambda x: tipo(x[chave]), reverse=ordem)
        except Exception as e:
            st.error(f"Erro ao executar: {e}")

    menorAno, maiorAno = anosMinMax(dados)
    if menorAno and maiorAno:
        anoJogos = slideBar(menorAno, maiorAno, (menorAno, maiorAno), 1, "Selecione o intervalo de anos:")
    
    nJogos = slideBar(5, 100, 50, 5)

    filaJogos = deque()
    for jogo in dados:
        lancado = jogo.get("Year")
        if isinstance(lancado, (int, float)) and anoJogos[0] <= lancado <= anoJogos[1]:
            filaJogos.append({
                "Name": jogo["Name"],
                "Year": jogo["Year"],
                "Global_Sales": jogo["Global_Sales"]
            })
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
    def inserir(jogo, valor):
        """Insere um par (chave, valor) na tabela."""
        indice = hash(jogo) % nJogos
        tabela[indice].append((jogo, valor))
    
    def buscar(jogo):
        """Busca um valor associado à chave."""
        indice = hash(jogo) % nJogos
        tabelaJogosEncontrados = []
        for nome, infoJogo in tabela[indice]:
            if nome == jogo:
                tabelaJogosEncontrados.append((nome, infoJogo))
        return tabelaJogosEncontrados

    nJogos = slideBar(100, 1000, 300, 5)
    nomeJogo = st.text_input("Nome do jogo:", placeholder="Digite o nome exato do jogo")
    
    tabela = [[] for _ in range(nJogos)]

    for jogo in dados[:nJogos]:
        inserir(
            jogo["Name"],
            { 
                "Platform": jogo["Platform"],
                "Year": jogo["Year"],
                "Genre": jogo["Genre"],
                "Global_Sales": jogo["Global_Sales"],
            }
        )
    
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

    nJogos = slideBar(5, 30, 15, 5)
    jogos_ordenados = sorted(dados, key=lambda x: float(x["Global_Sales"]), reverse=True)
    jogos_top = jogos_ordenados[:nJogos]
    random.shuffle(jogos_top)
    
    raiz = None
    for jogo in jogos_top:
        valor = float(jogo["Global_Sales"])
        nome = jogo["Name"]
        raiz = insere(raiz, valor, nome)
    
    if raiz:
        st.subheader("Visualização da Árvore Binária de Busca (BST)")
        st.graphviz_chart(raiz.graphviz())

        # Contar nós folha
        def contar_folhas(no):
            if no is None:
                return 0
            if no.left is None and no.right is None:
                return 1
            return contar_folhas(no.left) + contar_folhas(no.right)
        
        folhas = contar_folhas(raiz)
        st.write(f"**Quantidade de nós folha:** {folhas}")
        st.write(f"**Altura da árvore:** {raiz.height}")
    else:
        st.error("Não foi possível construir a árvore. Verifique o formato dos dados.")

def main(opcao, dados):
    if opcao != "Projeto Final":
        return

    st.title("Projeto Final")
    '''if dados is None:
        st.warning("Por favor, carregue o arquivo no menu lateral.")
        return'''
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
