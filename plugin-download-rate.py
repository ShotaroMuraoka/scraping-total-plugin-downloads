import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
load_dotenv(join(dirname(__file__), '.env'))

load_url = os.environ.get("TARGET_URL")
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
links = soup.select(".plugin-info-container > h3 > a")

options = Options()
options.set_headless(True)
driver = webdriver.Chrome(chrome_options=options)


print("Plugin Name | Total Downloads")
for link in links:
    plugin_url = "https:" + link.get("href") + "advanced/"
    driver.get(plugin_url)
    plugin_html = driver.page_source.encode("utf-8")

    plugin_soup = BeautifulSoup(plugin_html, "html.parser")
    plugin_title = plugin_soup.find("h1", class_="plugin-title").string
    table = plugin_soup.select("table#plugin-download-history-stats > tbody > tr")[-1]
    td_data = table.select("td")[-1]

    print(plugin_title + " | " + td_data.get_text())
