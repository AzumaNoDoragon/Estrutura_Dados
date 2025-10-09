import streamlit as st
import json

def error(opcao):
    if opcao:
        st.title("EM DESENVOLVIMENTO!!!")

# ==================== Menu lateral ====================
st.sidebar.title("Menu de Navegação")
opcao = st.sidebar.radio("Escolha a página:", ["Projeto Integrado 1", "Projeto Integrado 2", "Projeto Integrado 3"])

dados = None
uploaded_file = st.sidebar.file_uploader("Envie o arquivo JSON", type=["json"])
if uploaded_file:
    dados = json.load(uploaded_file)
    st.sidebar.success("Arquivo carregado com sucesso!")

if opcao == "Projeto Integrado 1":
    try:
        import Projeto_integrado_1
        Projeto_integrado_1.main(opcao, dados)
    except:
        error(opcao)
elif opcao == "Projeto Integrado 2":
    try:
        import Projeto_integrado_2
        Projeto_integrado_2.main(opcao, dados)
    except:
        error(opcao)
elif opcao == "Projeto Integrado 3":
    try:
        import Projeto_integrado_3
        Projeto_integrado_3.main(opcao, dados)
    except:
        error(opcao)