import unittest  #importando la libreria unittest para tener los resultados de los casos
from selenium import webdriver  #importando la libreria selenium para pruebas automatizadas
from selenium.webdriver.common.by import By
import time

class ClickSendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()  
        driver.get("https://qa-challenge.codesubmit.io/")

    def test1(self):

        nombre = driver.find_element_by_id("user-name")           #una vez en la pagina busco el elemento por id.
        if nombre is not None:
            nombre.send_keys("locked_out_user")                   #este usuario segun el requerimiento debe dar mensaje de usuario bloqueado

        contrasena = driver.find_element_by_name("password")  #busco el elemnto del password
        if contrasena is not None:
            contrasena.send_keys("secret_sauce")

        login = driver.find_element_by_id("login-button")             #luego envio el request dando click al boton login
        if login is not None:
            login.click()
        time.sleep(5)

                                

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()
