from selenium import webdriver
from datetime import datetime

# author victor hausen

def get_multiple_channels(driver, urls):
    lista = []
    for url in urls:
        lista.append(get_channel_base(driver, url))
    driver.close()
    return(lista)
def get_channel(driver, url):
    data = get_channel_base(driver, url)
    driver.close()
    return(data)

def get_channel_base(driver, url):
    print(url)
    driver.get(url+"/about")

    # nome do canal
    name = driver.find_element_by_css_selector("#channel-title")
    name = name.text
    print(name)

    # numero de inscritos
    subscribers_count = driver.find_element_by_css_selector("#subscriber-count")
    subscribers_count = "".join(char for char in subscribers_count.text if char.isdigit())
    print(subscribers_count)

    # criacao do canal
    joined_at = driver.find_element_by_css_selector("#right-column > yt-formatted-string:nth-child(2)")
    joined_at = datetime.strptime(joined_at.text, "Joined %b %d, %Y")
    joined_at = datetime.strftime(joined_at, "%d/%m/%Y")
    print(joined_at)

    # numero de visualizações
    views_count = driver.find_element_by_css_selector("#right-column > yt-formatted-string:nth-child(3)")
    views_count = "".join(char for char in views_count.text if char.isdigit())
    print(views_count)

    # descricao
    description = driver.find_element_by_css_selector("#description")
    description = description.text
    print(description)

    result = {
    "url":url,
    "name":name,
    "subscribers_count":subscribers_count,
    "joined_at":joined_at,
    "views_count":views_count,
    "description":description,
    "scraped_at": datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:S")
    }

    return(result)