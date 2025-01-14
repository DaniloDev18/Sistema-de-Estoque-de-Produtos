import pyautogui as py_ag
import time
import pandas as pd

# Define uma pausa padrão entre os comandos para evitar erros
py_ag.PAUSE = 1

caminho_csv = 'produtos.csv'
dados = pd.read_csv(caminho_csv)

# Acessa o navegador e insere o link de login
py_ag.press("win", interval=0.3) # Para meu Windows
py_ag.write("chrome", interval=0.2)
py_ag.press("enter")

#py_ag.click(x=775, y=932)  # Para meu mac abrir o chrome na dock
# Eu poderia usarlizar um hotkey e add o cmmd e espaço p abrir a aba de pesquisa e abrir por la, 
# mas achei mais facil por posição do mouse, msm n funcionando p td mac

py_ag.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py_ag.press("enter")

# Aguarda o site carregar
time.sleep(2)

# Realiza o login
py_ag.press("tab")  # "Clica" no campo de login
py_ag.press("down", presses=3, interval=0.1)
py_ag.press("enter")

py_ag.press("tab")
py_ag.write("123456789") 
py_ag.press("enter")  # Clica no botão de login

time.sleep(2)

# Itera pelos dados do CSV e preenche os campos do formulário
for linha in dados.index:
    # Clique no campo de código do produto e insere o valor
    codigo = dados.loc[linha, "codigo"]
    py_ag.press("tab")  
    py_ag.write(str(codigo), interval=0.1)
    
    marca = dados.loc[linha, "marca"]
    py_ag.press("tab")
    py_ag.write(str(marca), interval=0.1)
    
    tipo = dados.loc[linha, "tipo"]
    py_ag.press("tab")
    py_ag.write(str(tipo), interval=0.1)
    
    categoria = dados.loc[linha, "categoria"]
    py_ag.press("tab")
    py_ag.write(str(categoria), interval=0.1)
    
    preco_unitario = dados.loc[linha, "preco_unitario"]
    py_ag.press("tab")
    py_ag.write(str(preco_unitario), interval=0.1)
    
    custo = dados.loc[linha, "custo"]
    py_ag.press("tab")
    py_ag.write(str(custo), interval=0.1)
    
    obs = dados.loc[linha, "obs"]
    py_ag.press("tab")
    py_ag.write(str(obs), interval=0.1)
    
    # Aguarde um pouco antes de passar para o próximo produto
    time.sleep(1)
    
    # Simula o envio ou navegação para o próximo produto
    py_ag.press("enter")  
    
    for _ in range(7):
        py_ag.hotkey("shift", "tab")
