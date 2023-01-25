# x = 10
# 'x: ', x
import pandas as pd
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
import streamlit as st

df = pd.read_html("https://www.data.jma.go.jp/obd/stats/etrn/view/10min_s1.php?prec_no=51&block_no=47636&year=2023&month=1&day=23&view=", index_col=0)
df = df[0]
st.write(df)
