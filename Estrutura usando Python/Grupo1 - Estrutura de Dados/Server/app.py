import streamlit as st
import json

def error(e):
    st.error(f"Erro ao executar: {e}")

# ==================== Menu lateral ====================
st.sidebar.title("Menu de Navegação")
opcao = st.sidebar.radio("Escolha a página:", ["Projeto Integrado 1", "Projeto Integrado 2", "APP_Hotel_Reservations_Completo", "Projeto Final"])

dados = None
uploaded_file = st.sidebar.file_uploader("Envie o arquivo JSON", type=["json"])
if uploaded_file:
    dados = json.load(uploaded_file)
    st.sidebar.success("Arquivo carregado com sucesso!")

if opcao == "Projeto Integrado 1":
    try:
        import Projeto_integrado_1
        Projeto_integrado_1.main(opcao, dados)
    except Exception as e:
        error(e)
elif opcao == "Projeto Integrado 2":
    try:
        import Projeto_integrado_2
        Projeto_integrado_2.main(opcao, dados)
    except Exception as e:
        error(e)
elif opcao == "APP_Hotel_Reservations_Completo":
    try:
        import APP_Hotel_Reservations_Completo
        APP_Hotel_Reservations_Completo.main(opcao, dados)
    except Exception as e:
        error(e)
elif opcao == "Projeto Final":
    try:
        import Projeto_Final
        Projeto_Final.main(opcao, dados)
    except Exception as e:
        error(e)