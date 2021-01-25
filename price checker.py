from selenium import webdriver
import io

firefox = webdriver.FirefoxOptions()
firefox.set_headless()
browser = webdriver.Firefox(firefox_options=firefox)
browser.get('https://www.amazon.in/Renewed-ASUS-Graphics-Windows-FA506IH-BQ180T/dp/B08LK3QKMM/ref=sr_1_3?dchild=1&keywords=asus+tuf+a15&qid=1611538573&sr=8-3')
code = browser.page_source

with io.open('temp.txt', "w", encoding ="utf-8") as file:
    file.write(code)
    file.close()

with io.open('temp.txt', "r", encoding = "utf-8") as file:
    for everyline in file:
        line=str(everyline)
        if 'a-size-medium a-color-price priceBlockBuyingPriceString' in line:
            line1 = line.rsplit('</',1)[0]
            line2 = line1.rsplit(';',1)[1]
            print(line2)