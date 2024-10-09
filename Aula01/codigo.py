# pylint: disable=import-error
# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip3 install pyautogui
import time
import pandas as pd
import pyautogui

# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C)

# comando para realizar uma pausa durante um comando
pyautogui.PAUSE = 0.5

# abrir um navegador
# apertar a tecla command (MacOS)
# pyautogui.press('command')

# combinar as teclas para abrir a janela de pesquisa
# pyautogui.hotkey('command','space')
pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
pyautogui.write('Arc')
pyautogui.press('return')

pyautogui.keyDown('command')
pyautogui.press('t')
pyautogui.keyUp('command')


# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('return')

# Passo 2: Fazer Login
# dando uma pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=2186, y=177)
pyautogui.write('brunnomanduca@test.com')

# passando para o proximo campo
pyautogui.press('tab')
pyautogui.write('minha_senha')

#apertando no botão de login
pyautogui.click(x=2486, y=357)

time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')
# print(tabela)


# Passo 4: Cadastrar 1 produto +
# Passo 5: Repetir o processo de cadastro até acabar os produtos

# para cada linha da minha tabela
for linha in tabela.index:
    # selecionar o 1 campo do form
    pyautogui.click(x=2185,y=45)

    # codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # preço unitario
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    # custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    # obs
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs)) 
    pyautogui.press('tab')
    pyautogui.press('return')
    pyautogui.scroll(5000)
