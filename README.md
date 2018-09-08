# YTscraper
An implementation for scraping channel information from Youtube Channels powered by Selenium.

There are two main functions. get_channel() and get_multiple_channels().

First of all, you need to create a Selenium driver and use one of the functions I mentionated e.g.:

from selenium import webdriver
import YTscraper

driver = webdriver.Chrome("chromedriver")

data = YTscraper.get_channel(driver, my_youtube_url)

The returned value is going to be a dictionary(or a list of dictionaries for get_multiple_channels()) with the following values:
url: the one you've sent
name: the channel name
subscribers_count: the number of subscribers the channel has in the given date
joined_at: the date when the channel was created
views_count: the number of views the channel has in the given date
description: the channel description
scraped_at: a datetime string describing when the scraping took place

Hope you like it. For any doubt use the comments section.
