import streamlit
import pandas
import requests
from urllib.error import URLError

streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 omega 3 & bluberry otameal')
streamlit.text('🥗 kale,spinach & rocket smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')               
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(my_fruit_list)
#create function
def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
return fruityvice_normalized
   
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
streamlit.error("please select a fruit to get information.")
else:
 back_from_function=get_fruityvice_data(this_fruit_choice)
streamlit.dataframe( back_from_function)
except URLError as e: 
streamlit.error()
  
  
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)
streamlit.stop()
#import snowflake.connector
streamlit.header("the_fruit_load_list_contain:")
def get_fruit_load_list():
 
with my_cnx.cursor()as my_cur:
my_cur.execute("SELECT*from fruit_load_list")
 return my_cur.fetchall()
if streamlit.button('get_fruit_load_list'):
 my cnx=snowflake.connector.connect(**streamlite.secrets["snowflake"])
my_data_rows=get_fruit_load_list()
streamlit.dataframe(my_data_rows)

add_my_fruit=streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ',add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

import snowflake.connector


