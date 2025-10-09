import json
from collections import deque
import streamlit as st

# ==================== "Front" ====================
def main(opcao, dados):
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
          if dados:
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

# ==================== Exercício 1 — Lista ====================
def carregar_reservas(dados: str) -> list[dict]:
    """Carrega o JSON em uma lista de dicionários e retorna o catálogo de reservas."""
    # implementar leitura do arquivo JSON

    espera = deque()
    for r in dados:
        ano = r.get("arrival_year")
        mes = r.get("arrival_month")
        dia = r.get("arrival_day")
        r["arrival_tuble"] = (ano, mes, dia)
        espera.append(r)
    return espera

# ==================== Exercício 2 — Fila ====================
def montar_fila(reservas: list[dict], ano: int, mes: int, dia: int, estrutura="deque"):
    """Monta a fila de check-in com base nas reservas do dia (Not_Canceled).
       estrutura pode ser 'queue' ou 'deque'."""
    # implementar criação da fila
    reservas_do_dia = deque()
    for r in reservas:
      if (r.get("arrival_year") == ano and
            r.get("arrival_month") == mes and
            r.get("arrival_date") == dia and
            r.get("booking_status") == "Not_Canceled"):
            reservas_do_dia.append(r) #FIFO
    return reservas_do_dia

# ==================== Exercício 3 — Pilha (Undo) ====================
def registrar_acao(pilha: list, reserva: dict):
    """Adiciona na pilha o check-in realizado."""
    # implementar push na pilha
    if reserva is None:
        st.write("> nada a registrar")
        return
    pilha.append(reserva)  # push (topo à direita)
    st.write(f"> push OK (checkin tamanho={len(pilha)})")

def desfazer_acao(pilha: list) -> dict:
    """Remove o último check-in da pilha e retorna a reserva desfeita."""
    # implementar pop da pilha
    if not pilha:
        st.write("> pilha vazia")
        return None
    r = pilha.pop()
    st.write(f"> pop OK (checkin tamanho={len(pilha)})")
    return r

# ====================
# Exercício 4 — Interação Fila ↔ Pilha
#   - 'chamar_proximo': move FIFO -> LIFO   (reservas_do_dia -> checkin)
#   - 'devolver_para_fila': desfaz LIFO -> FIFO (checkin -> reservas_do_dia no INÍCIO)
# ====================
def chamar_proximo(reservas_do_dia: "deque[dict]", checkin: "deque[dict]") -> dict:
    """Atende o próximo da FILA (FIFO) e registra na PILHA (LIFO)."""
    if not reservas_do_dia:
        st.write("> fila do dia vazia")
        return None
    r = reservas_do_dia.popleft()     # FIFO
    registrar_acao(checkin, r)        # LIFO (push)
    st.write(f"> check-in realizado: {r.get('Booking_ID')}")
    return r

def devolver_para_fila(checkin: "deque[dict]", reservas_do_dia: "deque[dict]"):
    """
    Desfaz o último check-in: tira da PILHA (pop) e coloca
    no INÍCIO da FILA do dia (appendleft), garantindo prioridade.
    """
    r = desfazer_acao(checkin)        # LIFO (pop)
    if r is None:
        return
    reservas_do_dia.appendleft(r)     # volta pro começo da FILA (FIFO)
    st.write(f"> devolvido à fila do dia (início): {r.get('Booking_ID')}")

# ==================== Exercício 5 — Relatório Integrado ====================
def gerar_relatorio(reservas: list[dict], fila, pilha: list, escolha: int):
    """Gera relatório com dados da lista, fila e pilha.
       escolha define a métrica extra a ser exibida:
       1 = média preço por quarto
       2 = top 3 tipos de quarto
       3 = taxa de cancelamento"""
    # implementar relatório
    st.write("\n=== RELATÓRIO INTEGRADO ===")
    st.write(f"- Total na LISTA (reservas): {len(reservas)}")
    st.write(f"- Tamanho da FILA: {len(fila) if fila is not None else 0}")
    st.write(f"- Tamanho da PILHA: {len(pilha)}")

    if escolha == 1:
        valores = []
        for r in reservas:
            v = r.get("avg_price_per_room")
            if isinstance(v, (int, float)):
                valores.append(float(v))
            else:
                try:
                    valores.append(float(v))
                except:
                    pass
        if valores:
            media = sum(valores) / len(valores)
            st.write(f"- (1) Média preço por quarto: {media:.2f}")
        else:
            st.write("- (1) Sem valores para média.")

    elif escolha == 2:
        cont = {}
        for r in reservas:
            rt = r.get("room_type_reserved")
            if rt:
                cont[rt] = cont.get(rt, 0) + 1
        top = sorted(cont.items(), key=lambda x: x[1], reverse=True)[:3]
        st.write("- (2) Top 3 tipos de quarto:")
        if top:
            for i, (rt, c) in enumerate(top, 1):
                st.write(f"  {i}. {rt}: {c}")
        else:
            st.write("  sem dados.")

    elif escolha == 3:
        cancel = sum(1 for r in reservas if r.get("booking_status") == "Canceled")
        ok     = sum(1 for r in reservas if r.get("booking_status") == "Not_Canceled")
        tot = cancel + ok
        if tot:
            tx = 100.0 * cancel / tot
            st.write(f"- (3) Taxa de cancelamento: {tx:.2f}% (Canceladas={cancel}, Não canceladas={ok})")
        else:
            st.write("- (3) Sem status suficientes.")
    else:
        st.write("- Escolha inválida (1/2/3).")

    if fila:
        preview = [r.get("Booking_ID") for r in list(fila)[:5]]
        st.write(f"- Próximos na fila (até 5): {preview}")
