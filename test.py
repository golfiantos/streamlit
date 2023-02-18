import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    layout='wide'
)


st.title('Judul')
st.header('Header')
st.write('hellooo')

code1 = """
import streamlit as st
import pandas as pd

a = [1,2,3,4]


#list
"""


df = pd.read_csv('http://code.s3.yandex.net/datasets/vehicles_us.csv')
df['cylinders'].fillna(0,inplace=True)
df['cylinders'] = df['cylinders'].astype(int)

st.code(code1, language='python')

 

col1,col2 = st.columns(2)

with col1:
    fig = px.box(df['cylinders'])
    st.plotly_chart(fig)

with col2:
    fig = px.histogram(df['cylinders'])
    st.plotly_chart(fig)




