from selenium import webdriver
from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)
        try:
            more_options = self.driver.find_element_by_xpath("//button[contains(text(), 'More Options')]")
            more_options.click()
        except:
            sleep(1)
        fb_btn = self.driver.find_element_by_xpath("//span[contains(text(), 'Log in with Facebook')]")
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        sleep(5)

        self.driver.switch_to_window(base_window)
        sleep(2)
        popup_1 = self.driver.find_element_by_xpath("//span[contains(text(), 'Allow')]")
        popup_1.click()
        sleep(2)
        popup_2 = self.driver.find_element_by_xpath("//span[contains(text(), 'Enable')]")
        popup_2.click()
        sleep(2)
        popup_3 = self.driver.find_element_by_xpath("//span[contains(text(), 'I Accept')]")
        popup_3.click()
        sleep(2)
        popup_4 = self.driver.find_element_by_xpath("//span[contains(text(), 'No Thanks')]")
        popup_4.click()

    def like(self):
        like_btn = self.driver.find_elements_by_xpath('//button[contains(@aria-label, "Like")]')[1]
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//button[contains(@aria-label, "Nope")]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_5 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_5.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()
