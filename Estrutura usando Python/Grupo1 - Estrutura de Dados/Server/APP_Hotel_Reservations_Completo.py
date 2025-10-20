import streamlit as st
import json
from collections import deque

def main(opcao, dadosJson):
  if opcao == "APP_Hotel_Reservations_Completo":
    st.set_page_config(page_title="Hotel_Reservations - App")

    st.title("Aplicação Hotel Reservations")

    st.caption("Desenvolvimento apenas da Interface")

    menu = st.radio("Navegação",
                                ["1) Exibir dados",
                                "2) Carregar reservas confirmadas (FILA)",
                                "3) Processar 5 primeiras reservas (PILHA)"])

    if "dados" not in st.session_state:
      st.session_state.dados = []
    if "tamanho" not in st.session_state:
      st.session_state.tamanho = 0

    def carrega_json(file):
      conteudo = file.read().decode("utf-8")
      data = json.loads(conteudo)
      return data

    st.caption("Controle de visualização")
    st.session_state.tamanho = st.slider("n (quantidade)",0,500,250)

    if menu.startswith("1"):
      col1, col2 = st.columns(2)
      with col1:
        if st.button("Salvar na sessão",
                  use_container_width=True, disabled=False):
          reservas = dadosJson
          if reservas is not None:
              st.session_state.dados = reservas
              st.success(f"{len(reservas)} resgistros carregados na sessão!!")
      with col2:
        if st.button("Limpar a sessão",
                  use_container_width=True, disabled=False):
          st.session_state.dados = []
          st.info("Dados removidos da sessão!!")

      st.markdown("#### Prévia dos dados carregados!")
      st.caption(f"Exibindo {st.session_state.tamanho} registros...")
      st.json(st.session_state.dados[:st.session_state.tamanho])
    elif menu.startswith("2"):
      if not st.session_state.dados:
        st.warning("Nenhum dado carregado na sessão!!")
      else:
        st.subheader(f"Exibir os {st.session_state.tamanho} registros")
        st.json(st.session_state.dados[:st.session_state.tamanho])
