import streamlit
import pandas
streamlit.title('My Parents new Healthy Diner')
import requests
import snowflake.connector

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spanish & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌 🥭 Build your Own Fruits Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick soem fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header('Fruityvice fruit Advice!')
import requests
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

streamlit.text(streamlit.secrets["snowflake"])
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select name from pc_rivery_db.public.fruityvice")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.dataframe(my_data_row.name)
#add_my_fruit = my_data_row.set_index(Name)
#fruits_selected = streamlit.multiselect("Pick some fruits:", my_data_row.index,['Banana'])

#streamlit.dataframe(fruits_selected)

#streamlit.header('End')
