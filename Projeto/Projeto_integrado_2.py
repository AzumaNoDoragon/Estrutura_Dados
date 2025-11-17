import streamlit as st
from binarytree import Node
import re

# ======== Funções auxiliares ========
def limpar_numero(valor):
    """Converte texto como para inteiro."""
    if isinstance(valor, str):
        valor = re.sub(r"[^\d]", "", valor)
        if valor == "":
            return None
        return int(valor)
    return valor

def inserir(raiz, valor):
    """Insere um valor numérico na árvore binária de busca (BST)."""
    if raiz is None:
        return Node(valor)
    if valor < raiz.value:
        raiz.left = inserir(raiz.left, valor)
    else:
        raiz.right = inserir(raiz.right, valor)
    return raiz

def construir_arvore(dados, chave, limite):
    """Constroi uma árvore binária de busca com base em uma chave (streams, danceability_%, energy_%) e limite de músicas."""
    raiz = None
    contador = 0

    for item in dados:
        if contador >= limite:
            break
        if chave not in item:
            continue
        val = limpar_numero(item[chave])
        if val is not None:
            raiz = inserir(raiz, val)
            contador += 1

    return raiz

def main(opcao, dados):
    if opcao != "Projeto Integrado 2":
        return

    st.title("Projeto Integrado 2 — Árvore Binária de Músicas (Spotify 2023)")

    st.subheader("Selecione a Árvore")
    escolha = st.radio(
        "Escolha o tipo de árvore:",
        [
            "Árvore Binária de Popularidade (streams)",
            "BST de Dançabilidade (danceability_%)",
            "BST de Energia Musical (energy_%)"
        ]
    )

    # Selecionar quantas músicas carregar
    n = st.slider("Quantidade de músicas carregadas (n)", 10, 500, 100, step=10)
    st.info(f"Serão carregadas as {n} primeiras músicas do arquivo para montar a árvore.")

    if dados is None:
        st.warning("Por favor, carregue o arquivo **spotify-2023.json** no menu lateral.")
        return
    
    if escolha == "Árvore Binária de Popularidade (streams)":
        chave = "streams"
    elif escolha == "BST de Dançabilidade (danceability_%)":
        chave = "danceability_%"
    else:
        chave = "energy_%"

    with st.spinner("Construindo árvore..."):
        arvore = construir_arvore(dados, chave, n)

    if arvore:
        st.graphviz_chart(arvore.graphviz())
    else:
        st.error("Não foi possível construir a árvore. Verifique o formato dos dados.")