from bs4 import BeautifulSoup
import requests
import pandas as pd

#url = input("Please insert the link of the web page: ")
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

#cleans up all the unnecessary html parts 
#soup is gonna show all
soup = BeautifulSoup(page.text, 'html.parser')

#table is only first  due to index 0
table = soup.find_all("table")[0]

#because titles have th tags in this website 
world_titles = table.find_all("th")

#column data
column_data = table.find_all("tr")

world_table_titles = [title.text.strip() for title in world_titles]

#inserting titles into data frame by pandas 
df = pd.DataFrame(columns = world_table_titles)

for row in column_data[1:]:
    #td is for specific data within columns
    row_data = row.find_all("td")
    #strip cleans it 
    individual_row_data = [data.text.strip() for data in row_data]
    #finds the length of the dataframe
    length = len(df)

    df.loc[length] = individual_row_data

#index false to not show index number
df.to_csv(r'C:\Users\HP\OneDrive\Desktop\SelfProjects\ScraperOutput\Companies.csv', index = False)
