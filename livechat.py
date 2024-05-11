# CRIAÇÃO DE UM LIVE CHAT

# INSTALAR FLET NO CMD -> pip install flet

# IMPORTAR O FLET
import flet as ft

# CRIAR A FUNÇÃO PRINCIPAL DO SISTEMA

# Sempre criar o elemento e posteriormente agregar o elemento a página
# Não esquecer de colocar o parametro do que voce quer que o elemento faça em sua página
def main(pagina):
    titulo = ft.Text("LiveChat")

    
def iniciar_chat(evento):
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= iniciar_chat)

# ELEMENTOS AGREGADOS

# A ordem com que vamos colocar os elementos faz diferença
# pagina.add serve para colocar cada elemento na pagina, ou seja, é um pagina.add para cada elemento
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# RODAR A SISTEMA

# Caso queira rodar a aplicação de uma forma diferente de uma janela por ex. 
# Pode-se colocar um paramentro dentro do (main) que é o "view", ou seja,
# o código ficará assim: (main, view = ...)
# Caso voce queira visualizar na web ficaria assim: (main, view = ft.web_browser)
ft.app(main)