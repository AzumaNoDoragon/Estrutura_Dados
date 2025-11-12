import streamlit as st
from binarytree import Node

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
    st.subheader("Informações Gerais da Base")
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
    
    st.write("Os jogos mais vendidos foram:", maisVendidos)

def Fila():
    print()

def Hash():
    print()

def BTS():
    print()

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
        menor_ano, maior_ano = anosMinMax(dados)
        if menor_ano and maior_ano:
            anoJogos = slideBar(menor_ano, maior_ano, (menor_ano, maior_ano), 1, "Selecione o intervalo de anos:")
        
        nJogos = slideBar(5, 100, 50, 5)

    elif escolha == "Tabela Hash (Hashing)":
        nJogos = slideBar(100, 1000, 300, 5)
        nomeJogo = st.text_input("Nome do jogo:", placeholder="Digite o nome exato do jogo")
    
    elif escolha == "Árvore Binária de Busca (BST)":
        def insere(raiz, item):
            """Insere um novo nó na árvore com base em Global_Sales."""
            if raiz is None:
                return Node(f"{item['Name']} ({item['Global_Sales']})")
            valor_raiz = float(raiz.value.split("(")[-1].replace(")", ""))  # extrai vendas da string
            if item["Global_Sales"] < valor_raiz:
                raiz.left = insere(raiz.left, item)
            else:
                raiz.right = insere(raiz.right, item)
            return raiz

        nJogos = slideBar(5, 30, 15, 5)
        raiz = None
        count = 0
        
        for jogo in dados:
            if count >= nJogos:
                break
            item = {"Global_Sales": float(jogo["Global_Sales"]), "Name": jogo["Name"]}
            raiz = insere(raiz, item)
            count += 1
        
        if raiz != None:
            st.graphviz_chart(raiz.graphviz())
        else:
            st.error("Não foi possível construir a árvore. Verifique o formato dos dados.")
