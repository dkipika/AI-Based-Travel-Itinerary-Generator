'''
AI-BasedTravel_ItineraryGenerator.py
AI-Based Travel Itinerary Generator
Develop a Streamlit app where users input their travel destination and duration.
Use Gemini API to generate a complete travel itinerary (places to visit, food recommendations, and activities).
'''

import streamlit as st
import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Api Key not found :( ")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

st.header("AI Based Travel Itinerary Generator")

destination = st.text_input("Enter Your Travel Destination Here")
duration = st.text_input("Enter Your duration of the stay")
submit = st.button("Generate Travel Plan")

if submit:
    if destination and duration:
        response = model.generate_content(f"generate a complete travel itinerary (places to visit, food recommendations, and activities) According to destination = {destination} and duration of the stay = {duration} . It should be day by day and easy to undersatandable")
        st.write(response.text)

