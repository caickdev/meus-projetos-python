from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações opcionais (headless = sem abrir janela visível, útil para automações reais)
options = Options()
# options.add_argument("--headless")  # Descomente para rodar sem janela (mais rápido)

# Usa webdriver-manager para baixar ChromeDriver automaticamente
service = Service(ChromeDriverManager().install())

# Inicia o navegador
driver = webdriver.Chrome(service=service, options=options)

try:
    # Abre o Google
    driver.get("https://www.google.com")
    print("Página aberta:", driver.title)

    # Encontra o campo de busca pelo name="q"
    campo_busca = driver.find_element(By.NAME, "q")

    # Preenche o campo
    campo_busca.send_keys("Python Selenium tutorial")

    # Simula Enter ou clica no botão de busca
    campo_busca.send_keys(Keys.ENTER)
    # Alternativa: driver.find_element(By.NAME, "btnK").click()  # Botão "Pesquisa Google"

    time.sleep(5)  # Espera 5 segundos para ver o resultado (remova em produção)

    print("Busca realizada com sucesso!")

finally:
    # Fecha o navegador sempre (boa prática)
    driver.quit()