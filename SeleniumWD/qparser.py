from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('https://proghub.ru/')
    #btn_elem = driver.find_element_by_class_name('ytp-play-button')
    #btm_elem.click()
    titleh1 = driver.find_element_by_tag_name('h1')
    print(titleh1.text)


if __name__ == '__main__':
    main()
