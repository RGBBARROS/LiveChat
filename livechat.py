# PASSO A PASSO
# Criação do LiveChat By: Roger para usar em Projeto da empresa
# botao de iniciar chat
# DIV para entrar no chat
# Quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

# INSTALAR FLET NO CMD -> pip install flet
# IMPORTAR FLET AS FT
import flet as ft

def main(pagina):
    texto = ft.Text("LiveChat By: Roger")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu cargo.seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]

# ADICIONAR MSG AO CHAT
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        

# LIMPAR O CAMPO MSG
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
# adicionar o chat
        pagina.add(chat)
# fechar o popup
        popup.open = False
# remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
# criar o campo de mensagem do usuario
# criar o botao de enviar mensagem do usuario
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao LiveChat By: Roger"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)


# RODAR A SISTEMA

# Caso queira rodar a aplicação de uma forma diferente de uma janela por ex. 
# Pode-se colocar um paramentro dentro do (main) que é o "view", ou seja,
# o código ficará assim: (main, view = ...)
# Caso voce queira visualizar na web ficaria assim: ft.app(main, view=ft.WEB_BROWSER)
# Ou, ft.app(main) = para rodar como uma aplicação
# proximo passo é REALIZAR  o DEPLOY
