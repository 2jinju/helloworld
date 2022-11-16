import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.header('We are cooks! :cooking::memo:')
st.write('made by kyudeok and jinju :heart:')
st.write('*From july 31st, 2022*')

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})
st.write(df)

st.write('Below is a DataFrame:',df, 'Above is a DataFrame.')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])

df2

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y='b', size='c', color='b',tooltip=['a','b','c'])
st.write(c)