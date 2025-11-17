import streamlit as st
import json

def error(e) -> str:
    """Função utilitária para exibir mensagens de erro no app"""
    st.error(f"Erro ao executar: {e}")

st.sidebar.title("Menu de Navegação")
opcao = st.sidebar.radio("Escolha a página:", ["Projeto Integrado 1", "Projeto Integrado 2", "APP_Hotel_Reservations_Completo", "Projeto Final"])

dados = None
uploaded_file = st.sidebar.file_uploader("Envie o arquivo JSON", type=["json"])
if uploaded_file:
    dados = json.load(uploaded_file)
    st.sidebar.success("Arquivo carregado com sucesso!")

# Cada opção importa e executa um módulo diferente.
# A função 'main()' de cada módulo recebe a opção e os dados carregados.
if opcao == "Projeto Integrado 1":
    try:
        import Projeto.Projeto_integrado_1
        Projeto.Projeto_integrado_1.main(opcao, dados)
    except Exception as e:
        error(e)
elif opcao == "Projeto Integrado 2":
    try:
        import Projeto.Projeto_integrado_2
        Projeto.Projeto_integrado_2.main(opcao, dados)
    except Exception as e:
        error(e)
elif opcao == "APP_Hotel_Reservations_Completo":
    try:
        import Projeto.APP_Hotel_Reservations_Completo
        Projeto.APP_Hotel_Reservations_Completo.main(opcao, dados)
    except Exception as e:
        error(e)
elif opcao == "Projeto Final":
    try:
        import Projeto.Projeto_Final
        Projeto.Projeto_Final.main(opcao, dados)
    except Exception as e:
        error(e)