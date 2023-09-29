
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](https://www.hashtagtreinamentos.com/curso-python)")


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")
#1111111111111
import flet as ft

def main(pagina):
    texto = ft.Text("Chat")
#111111111111111111111111111

#6666666666666666666666666666666666
    chat = ft.Column()
#666666666666666666666666666666666666

#444444444444444444444444
    nome_usuario = ft.TextField(label="Escreva seu nome")
#44444444444444444444444444444

#777777777777777777777777777777777777777

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(campo_mensagem.value)
        campo_mensagem.value = ""

        pagina.update()

#88888888888888888888888888888888888888888


#55555555555555555555555555555555
    campo_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
       
#6666666666666666666666666666666666
        pagina.add(chat)
#666666666666666666666666666666666

#55555555555555555555555555555555555555
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))

        pagina.update()
#555555555555555555555555555555555



#33333333333333333333333333
    popup = ft.AlertDialog(
#33333333333333333333333333

#444444444444444444444444444444444        
        open=False,
        modal=True,
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
#44444444444444444444444444444444444444
    )
#3333333333333333333333333333333333
    def entra_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
#333333333333333333333333333333333

#2222222222222222222222
    botao_iniciar = ft.ElevatedButton("Iniciar", on_click=entra_chat)
#222222222222222222222222222

#1111111111111111111111
    pagina.add(texto)
    pagina.add(botao_iniciar)
    

ft.app(target=main, view=ft.WEB_BROWSER)
#view=web
#1111111111111111111111111111
















