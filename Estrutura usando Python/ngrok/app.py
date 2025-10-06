import streamlit as st
from collections import deque
import json
from Projeto_Integrado1 import carregar_reservas, montar_fila, chamar_proximo, devolver_para_fila, gerar_relatorio

# ==================== Menu lateral ====================
st.sidebar.title("Menu de Navegação")
opcao = st.sidebar.radio("Escolha a página:", ["Projeto Integrado 1", "Em desenvolvimento"])

uploaded_file = st.sidebar.file_uploader("Envie o arquivo JSON", type=["json"])
if uploaded_file:
    dados = json.load(uploaded_file)
    st.sidebar.success("Arquivo carregado com sucesso!")

# ==================== Projeto integrado 1 ====================
if opcao == "Projeto Integrado 1":
    st.title("Projeto Integrado 1")

    # Inicializa estruturas persistentes
    for key in ["espera", "fila", "pilha"]:
        if key not in st.session_state:
            st.session_state[key] = deque()

    opcAcao = {
        "Carregar base na ESPERA (deque viva)": "carregar",
        "Montar FILA do dia (reservas não canceladas)": "fila",
        "Fazer check-in (mover FILA -> PILHA)": "checkin",
        "Desfazer último check-in (mover PILHA -> FILA, início)": "desfazer",
        "Relatório integrado (1/2/3)": "relatorio"
    }

    acao = st.radio("Escolha a ação:", list(opcAcao.keys()))
    st.subheader("Resultados:")
    acaoVer = opcAcao[acao]

    # ==================== Ações ====================
    if acaoVer == "carregar":
        if uploaded_file:
            st.session_state.espera = carregar_reservas(dados)
            st.write("Base carregada na ESPERA:", len(list(st.session_state.espera)))
        else:
            st.warning("Envie o arquivo JSON primeiro.")

    elif acaoVer == "fila":
        if st.session_state.espera:
            ano = st.number_input("Ano:", min_value=2000, max_value=2100, value=2025)
            mes = st.number_input("Mês:", min_value=1, max_value=12, value=10)
            dia = st.number_input("Dia:", min_value=1, max_value=31, value=6)
            st.session_state.fila = montar_fila(st.session_state.espera, ano, mes, dia)
            st.write("Quantidade:", len(st.session_state.fila))
            st.write("Fila do dia (não canceladas):", list(st.session_state.fila))
        else:
            st.warning("Carregue a base na ESPERA antes de montar a FILA.")

    elif acaoVer == "checkin":
        if st.session_state.fila:
            if st.button("Fazer check-in do próximo"):
                item = chamar_proximo(st.session_state.fila, st.session_state.pilha)
                st.write("Check-in realizado:")
                st.write(item)
            st.write("Fila atualizada:", list(st.session_state.fila))  
        else:
            st.warning("A fila está vazia. Carregue ou monte a fila primeiro.")
            st.write("Pilha Atual:", list(st.session_state.pilha))

    elif acaoVer == "desfazer":
        if st.session_state.pilha:
            if st.button("Desfazer último check-in"):
                devolver_para_fila(st.session_state.pilha, st.session_state.fila)
                st.write("Check-in desfeito.")
            st.write("Fila atualizada:", list(st.session_state.fila))
            st.write("Pilha atualizada:", list(st.session_state.pilha))
        else:
            st.warning("Nenhum check-in para desfazer.")

    elif acaoVer == "relatorio":
       escolha = st.number_input("Escolha métrica extra (1 = média preço, 2 = top 3 quartos, 3 = taxa cancelamento):", min_value=1, max_value=3, value=1)
       gerar_relatorio(list(st.session_state.espera), st.session_state.fila, list(st.session_state.pilha), escolha)

# ==================== Página em desenvolvimento ====================
elif opcao == "Em desenvolvimento":
    st.subheader("Em desenvolvimento")
    valor = st.slider("Em desenvolvimento", 0, 100, 50)
    st.write("Em desenvolvimento", valor)