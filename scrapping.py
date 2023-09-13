import bs4
import time
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

scrapped_data = []

def scrap():
    soup = BeautifulSoup()

    bright_star_table = soup.find("table",attrs={"class" , "wikitable"})
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = table_rows.find_all('td')
        print(table_cols)

        temp_list = []

        for col_data in table_rows:
            data = col_data.text.strip()
            print(data)

            temp_list.append(data)
    scrapped_data.append(temp_list)

    #Save Data
    stars_data = []

    for i in range(0,len(scrapped_data)):
        star_names = scrapped_data[i][1]
        distance = scrapped_data[i][3]
        mass = scrapped_data[i][5]
        radius = scrapped_data[i][7]
        lum = scrapped_data[i][9]

        required_data = [star_names , distance , mass , radius , lum]
        stars_data.append(required_data)
    
    headers = ["star_names", "distance" , "mass" , "radius" , "luminosity"]
    star_df = pd.dataframe(stars_data , columns = headers)
    star_df.to_csv('scrapped_data.csv' ,index = True  , index_label = id)
    
scrap()