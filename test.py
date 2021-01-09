import streamlit as st
import requests
import pandas as pd
import numpy as np
import time
import datetime

st.title ("Download your History Price")
@st.cache
def get_history_report(code, date_start, now):
    # periode1 on timestamp
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{code}.JK?period1={date_start}&period2={now}&interval=1d&events=history&includeAdjustedClose=true'
    alpha = requests.get(url)
    tab=[]
    for a in alpha.text.split('\n')[1:]:
        tab.append({
        'Date':a.split(',')[0],
        'Open':a.split(',')[1],
        'High':a.split(',')[2],
        'Low':a.split(',')[3],
        'Close':a.split(',')[4]
        })
    return pd.DataFrame(tab)
data = st.text_input("input your stock")
if not data:
    st.error("Insert your stocks first")
try:
    date_start = st.text_input("startDate ex. 2020-01-01")
    date_start = int(time.mktime(datetime.datetime.strptime(f'{date_start}', "%Y-%m-%d").timetuple()))
    now = int(time.mktime(datetime.datetime.now().timetuple()))
    df = get_history_report(data, str(date_start), str(now))
    # build chart
#    chart = df['date']
    st.write("### Historical data", get_history_report(data, str(date_start), str(now)))
    df = df.set_index('Date')
    st.line_chart(df['Close'])
except:
    st.error("Please insert date")
    pass



