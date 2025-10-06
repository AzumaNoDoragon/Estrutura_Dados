import streamlit as st

# Menu lateral
st.sidebar.title("Menu de Navegação")
opcao = st.sidebar.radio("Escolha a página:", ["Início", "Análise", "Sobre"])

# Página central
st.title("Minha Aplicação Streamlit")

if opcao == "Início":
    st.subheader("Página inicial")
    st.write("Bem-vindo à aplicação!")
elif opcao == "Análise":
    st.subheader("Área de análise")
    valor = st.slider("Selecione um valor", 0, 100, 50)
    st.write("Valor escolhido:", valor)
elif opcao == "Sobre":
    st.subheader("Sobre")
    st.text_area("Deixe seu comentário")