import streamlit as st
import pandas as pd

# ESL Tip: Students can change the title to their native language!
st.title("📊 My Data App") 

# 1. Create a tiny dataset using emojis
data = {
    "Name": ["Alex", "Maria", "Lin", "Ken"],
    "Score": [85, 92, 78, 88] # Students change these numbers
}

df = pd.DataFrame(data)

# 2. Display the math calculation automatically
average_score = df["Score"].mean()
st.metric(label="Average Class Score", value=average_score)

# 3. Create a visual chart
st.bar_chart(df, x="Name", y="Score")
