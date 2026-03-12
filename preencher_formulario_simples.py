from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Descomente para modo invisível

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

    # Muda para o iframe do formulário (importante no w3schools)
    driver.switch_to.frame("iframeResult")

    # Preenche campos
    primeiro_nome = driver.find_element(By.ID, "fname")
    primeiro_nome.clear()
    primeiro_nome.send_keys("Caick")

    sobrenome = driver.find_element(By.ID, "lname")
    sobrenome.clear()
    sobrenome.send_keys("Vieira")

    # Submete o formulário
    botao_submit = driver.find_element(By.XPATH, "//input[@value='Submit']")
    botao_submit.click()

    time.sleep(3)  # Espera ver o resultado

    print("Formulário preenchido e submetido!")

finally:
    driver.quit()