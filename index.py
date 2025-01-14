import pyautogui as py_ag
import time
import pandas as pd

# Define uma pausa padrão entre os comandos para evitar erros
py_ag.PAUSE = 1

# Carrega o arquivo CSV
caminho_csv = 'produtos.csv'
dados = pd.read_csv(caminho_csv)

# Acessa o navegador e insere o link de login
py_ag.press("win", interval=0.3) # Para meu Windows
py_ag.write("chrome", interval=0.2)
py_ag.press("enter")

py_ag.click(x=775, y=932)  # Para meu mac

py_ag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py_ag.press("enter")

# Aguarda o site carregar
time.sleep(2)

# Realiza o login
py_ag.press("tab")  # Clique no campo de login
py_ag.press("down", presses=3, interval=0.1)
py_ag.press("enter")

py_ag.press("tab")
py_ag.write("123456789")  # Digite a senha correta aqui
py_ag.click(x=760, y=605)  # Clique no botão de login

time.sleep(2)

# Itera pelos dados do CSV e preenche os campos do formulário
for _, linha in dados.iterrows():
    # Clique no campo de código do produto e insere o valor
    py_ag.press("tab")  # Ajuste as coordenadas conforme necessário
    py_ag.write(str(linha['codigo']), interval=0.1)  # Intervalo entre cada caractere
    
    
    py_ag.press("tab")
    py_ag.write(str(linha['marca']), interval=0.1)
    
    
    py_ag.press("tab")
    py_ag.write(str(linha['tipo']), interval=0.1)
    
    
    py_ag.press("tab")
    py_ag.write(str(linha['categoria']), interval=0.1)
    
    
    py_ag.press("tab")
    py_ag.write(str(linha['preco_unitario']), interval=0.1)
    
    
    py_ag.press("tab")
    py_ag.write(str(linha['custo']), interval=0.1)
    
    
    py_ag.press("tab")
    py_ag.write(str(linha['observacao']), interval=0.1)
    
    # Aguarde um pouco antes de passar para o próximo produto
    time.sleep(3)
    
    # Simula o envio ou navegação para o próximo produto
    py_ag.press("enter")  # Ajuste conforme o comportamento do sistema
