import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class Login(unittest.TestCase):
    FORM_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    H2 = (By.XPATH, '//h2')
    LOGHIN_BUTTON = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
    LINK = (By.XPATH, "//a[text()='Elemental Selenium']")
    ERROR_LOGHIN = (By.ID, 'flash')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGHIN_MESSAGE = (By.CLASS_NAME, 'flash succes')
    H4 = (By.XPATH, '//h4[@class="subheader"]')

    def setUp(self):
        self.tema = webdriver.Chrome()
        self.tema.maximize_window()
        self.tema.get('https://the-internet.herokuapp.com/')
        self.tema.find_element(*self.FORM_AUTH).click()
        self.tema.implicitly_wait(7)
    def tearDown(self):
        self.tema.quit()

    def test1_verifica_url(self):
        time.sleep(2)
        actual = self.tema.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        assert actual == expected, f"Error: URL incorect "


    def test2_page_title(self):
        title_page = self.tema.title
        expected_title = 'The Internet'
        self.assertEqual(title_page,expected_title, 'Title incorect')

    def test3_h2(self):
        elem_h2 = self.tema.find_element(*self.H2)
        actual_h2 = elem_h2.text
        expected_h2 = 'Login Page'
        assert actual_h2 == expected_h2, f"Error: h2 incorect "
    def test4_login_button(self):
        actual_login_button= self.tema.find_element(*self.LOGHIN_BUTTON).is_displayed()
        assert actual_login_button, 'Login button is not displayed'
    def test5_href_link(self):
        actual_link = self.tema.find_element(*self.LINK).get_attribute('href')
        expected_link = 'http://elementalselenium.com/'
        assert actual_link == expected_link, f'href link incorect'

    def test6_dispayed_error(self):
        self.tema.find_element(*self.LOGHIN_BUTTON).click()
        time.sleep(2)
        error = self.tema.find_element(*self.ERROR_LOGHIN).is_displayed()
        assert error, 'Error login is not displayed'

    def test7_error_message(self):
        self.tema.find_element(*self.USERNAME).send_keys('Ramona')
        self.tema.find_element(*self.PASSWORD).send_keys('1234')
        self.tema.find_element(*self.LOGHIN_BUTTON).click()
        actual_error = self.tema.find_element(*self.ERROR_LOGHIN).text
        expected_errror = 'Your username is invalid!'
        self.assertTrue(expected_errror in actual_error, 'Error message text is incorrect!')


    def test8_close_error(self):
        self.tema.find_element(*self.LOGHIN_BUTTON).click()
        self.tema.find_element(By.CLASS_NAME, 'close').click()
        try:
            self.tema.find_element(By.CLASS_NAME, 'close')
        except NoSuchElementException:
            print("The text is not visible")

    def test9_text_labels(self):
       label1 = self.tema.find_element(By.XPATH, "//label[text()='Username']").text
       label2 = self.tema.find_element(By.XPATH, "//label[text()='Password']").text
       expected_list = ['Username', 'Password']
       lista_label = [label1, label2]
       assert lista_label == expected_list, f'Label text is incorect'

    def test10_url_contine_secure(self):
        self.tema.find_element(*self.USERNAME).send_keys('tomsmith')
        self.tema.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.tema.find_element(*self.LOGHIN_BUTTON).click()
        url_dupa_logare = self.tema.current_url
        self.assertTrue("secure" in url_dupa_logare, 'Noul url nu contine secure')

        # WebDriverWait(self.tema, 10).until(EC.presence_of_element_located(self.LOGHIN_MESSAGE))
        # message = self.tema.find_element(*self.LOGHIN_MESSAGE).is_displayed()
        # assert message, 'The element is not displayed'
        ## assert self.tema.find_element(*self.LOGHIN_MESSAGE).is_displayed()==True, 'The element is not displayed'

    def test11_verificare_url_dupa_logout(self):
        self.tema.find_element(*self.USERNAME).send_keys('tomsmith')
        self.tema.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.tema.find_element(*self.LOGHIN_BUTTON).click()
        self.tema.find_element(By.XPATH, '//*[@id="content"]/div/a').click()
        url_dupa_logout = self.tema.current_url
        expected_url_logout = 'https://the-internet.herokuapp.com/login'
        assert url_dupa_logout == expected_url_logout, f'Url is incorect'

    def test_12_brute_force_password_haching(self):
        var_parole = self.tema.find_element(*self.H4).text.split()
        url = None
        for password in var_parole:
            self.tema.find_element(*self.USERNAME).send_keys('tomsmith')
            self.tema.find_element(*self.PASSWORD).send_keys(password)
            self.tema.find_element(*self.LOGHIN_BUTTON).click()

            url = self.tema.current_url
            if "secure" in url:
                print(f'Parola secreta este {password}')
                break
            else:
                print("Nu am reusit sa gasesc parola. Continuam cautarea")
        assert "secure" in url, "Eroare: parola nu a fost gasita"













