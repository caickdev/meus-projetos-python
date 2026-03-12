import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Carrega lista de pessoas de um CSV (crie um arquivo 'cadastros.csv' com colunas: Nome, Sobrenome, Email)
df = pd.read_csv('cadastros.csv')  # Exemplo de CSV: Nome,Sobrenome,Email

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    for index, row in df.iterrows():
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")
        driver.switch_to.frame("iframeResult")

        driver.find_element(By.ID, "fname").clear()
        driver.find_element(By.ID, "fname").send_keys(row['Nome'])

        driver.find_element(By.ID, "lname").clear()
        driver.find_element(By.ID, "lname").send_keys(row['Sobrenome'])

        # Se o formulário tiver e-mail, adicione aqui
        # driver.find_element(By.ID, "email").send_keys(row['Email'])

        driver.find_element(By.XPATH, "//input[@value='Submit']").click()
        time.sleep(3)  # Espera ver/submeter

        print(f"Cadastro {index+1} realizado: {row['Nome']} {row['Sobrenome']}")

finally:
    driver.quit()