import streamlit
import pandas
streamlit.title(' My Parents Now Healthy Diner')

streamlit.header(' Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv ( "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Mettiamo un elenco di raccolta qui in modo che possano raccogliere i frutti che vogliono includere 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe ( my_fruit_list )  # visualizza l'elenco di raccolta







