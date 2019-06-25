from selenium import webdriver
# browser = webdriver.Chrome("C:\Users\Le Thanh Tuan\Desktop\chromedriver_win32\chromedriver.exe")
browser = webdriver.Firefox("C:\Users\Le Thanh Tuan\Desktop\geckodriver-v0.24.0-win64\geckodriver.exe") #webdriver path executable
# userName = raw_input("Email: ")
# passWord = raw_input("passWord: ")
browser.get('https://www.facebook.com/')
emailLogin = browser.find_element_by_id('yourEmail') 
# emailLogin.send_keys(userName)
passLogin = browser.find_element_by_id('yourPass')
# passLogin.send_keys(passWord)
emailLogin.send_keys("email")
passLogin.send_keys("pass") 
passLogin.submit()
