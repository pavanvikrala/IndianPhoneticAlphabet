import pandas as pd
import streamlit as st

img_url = 'https://res.cloudinary.com/df7cbq3qu/image/upload/v1689087891/800px-Flag_of_India.svg_fqg6aw.png'
page_config = {"page_title": 'Indian Alphabets', "page_icon": img_url, "layout": "wide"}
st.set_page_config(**page_config)

st.title("Welcome to Indian Phonetic Alphabet ")
st.header("Inspired by NATO phonetic alphabet")

if st.checkbox("Click me for more info"):
    st.info("This is a Spelling Alphabet, a set of words used instead of letters "
            "in oral communication i.e., over the phone")

# Create a dataframe from the csv file
df = pd.read_csv("Indian_phonetic_alphabet.csv")

# Create a dict which contains alphabets as keys and respective words as values
data = {value.letter: value.code for index, value in df.iterrows()}


if st.text_input("Hello...let's begin introducing yourself. What's your name?"):
    user_input = st.text_input("Now enter a word⤵️ which you would like to spell out its letters to someone: ").upper()
    if user_input:
        try:
            word_list = [data[letter] for letter in user_input]
        except KeyError:
            st.error("Sorry, provide only letters")
        else:
            st.info(word_list)
            st.success("Hope this helps😊")
