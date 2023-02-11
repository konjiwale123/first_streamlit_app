import streamlit
streamlit.title('my parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 omega 3 & bluberry otameal')
streamlit.text('🥗 kale,spinach & rocket smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')               
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
