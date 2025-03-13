import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Caminho do ChromeDriver
CHROME_DRIVER_PATH = "C:/Users/SeuUsuário/Downloads/chromedriver.exe"

# Seletor CSS do saldo (substitua pelo correto do site)
SALDO_SELECTOR = ".saldo-atual"

# Função para iniciar o Selenium
def iniciar_selenium():
    chrome_options = Options()
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Função para pegar o saldo da conta
def pegar_saldo(driver):
    saldo_element = driver.find_element(By.CSS_SELECTOR, SALDO_SELECTOR)  
    driver.execute_script("arguments[0].scrollIntoView();", saldo_element)  
    saldo_texto = saldo_element.text.strip()
    
    # Converte saldo para número
    saldo = float(saldo_texto.replace("$", "").replace(",", "").strip())
    return saldo

# Função para monitorar os saldos
def monitorar_saldo(driver1, driver2):
    erro_contador = 0  # Contador de erros

    while True:
        try:
            saldo1 = pegar_saldo(driver1)
            saldo2 = pegar_saldo(driver2)

            # Só imprime os saldos quando houver mudança
            if saldo1 != monitorar_saldo.saldo_antigo1 or saldo2 != monitorar_saldo.saldo_antigo2:
                print(f"Saldo Conta 1: {saldo1} | Saldo Conta 2: {saldo2}")
                monitorar_saldo.saldo_antigo1 = saldo1
                monitorar_saldo.saldo_antigo2 = saldo2

            # Se Conta 1 ficar abaixo de 200, executa a ação A
            if saldo1 < 200:
                print("Conta 1 abaixo de 200! Executando ação A...")
                pyautogui.click(100, 200)  # Ajuste a posição do clique
                pyautogui.write("Recarregar saldo Conta 1")
                pyautogui.press("enter")

            # Se Conta 2 ficar abaixo de 200, executa a ação B
            if saldo2 < 200:
                print("Conta 2 abaixo de 200! Executando ação B...")
                pyautogui.click(300, 400)  # Ajuste a posição do clique
                pyautogui.write("Recarregar saldo Conta 2")
                pyautogui.press("enter")

            erro_contador = 0  # Zera o contador de erros se tudo estiver funcionando

        except Exception as e:
            erro_contador += 1
            if erro_contador % 10 == 0:  # Só exibe erro a cada 10 falhas
                print(f"Erro ao ler saldo ({erro_contador} tentativas falhas): {e}")

        time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente

# Inicializa os saldos antigos para evitar prints desnecessários
monitorar_saldo.saldo_antigo1 = -1
monitorar_saldo.saldo_antigo2 = -1

# Inicia duas janelas do navegador
driver1 = iniciar_selenium()
driver2 = iniciar_selenium()

# Abre a página do jogo em ambas
driver1.get("https://www.exemplo.com/")
driver2.get("https://www.exemplo.com/")

# Aguarda login manual
input("Faça login nas duas contas e pressione Enter para continuar...")

# Começa a monitorar os saldos
monitorar_saldo(driver1, driver2)
