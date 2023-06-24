import pandas as pd
import streamlit as st
from PIL import Image


df = pd.read_csv("data2.csv", sep=",")
col1,col2,col3=st.columns([25,25,25])
with col1:
    for index , row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["Description"])
        st.image("images/"+row["image"])

with col2:
        for index , row in df[2:4].iterrows():
            st.header(row["title"])
            st.write(row["Description"])
            st.image("images/"+row["image"])
with col3:
        for index, row in df[4:].iterrows():
            st.header(row["title"])
            st.write(row["Description"])
            st.image("images/" + row["image"])

