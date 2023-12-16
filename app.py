import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from PIL import Image
st.set_page_config(layout='wide')
df = pd.read_csv('data.csv')
tab1, tab2, tab3 = st.tabs(['Home', 'Statistical Analysis', 'Moving Average Analysis'])

with tab1:
	st.header("Stock Market Analysis")

	exp = st.expander("Introduction") 
	exp.write("Hi, welcome to this webiste! It is made by a Grade 11 Student who was interested in understanding more about stocks and understanding about stock trends.") 
## i don't know how to add more lines of text because if I copy-paste the line above - won't it just overwrite on what is already written 
	
	img = Image.open('stocks.jpg')
	
	st.subheader("What are stocks?") 
	col1, col2 = st.columns(2, gap = "small") 
	col1.image(img)
	col2.write("Stocks, also known as shares or equities, represent ownership in a company. When you purchase stocks, you become a shareholder and own a portion of the company. Companies issue stocks to raise capital for various purposes, such as expansion, research, and development.")
	col2.write("The terminology used for stocks can often sound like a new language. Therefore, if you are new to stocks, below is a list of 15 key terms and concepts I found useful to know when learning more about stocks")
	col2.write("Equity (in the stock market) refers to the amount of shares owned by a company. As an investor, when you buy the shares of a company, you buy an equivalent degree of ownership in that company. The stock market is where these company shares (equity) are bought and sold from one investor to another. The word ‘stock’ is synonymous with the word 'equity.")
with tab2:
	cmp = st.selectbox('Select the company',('Apple','Starbucks','Microsoft','Cisco','Qualcomm','Meta','Amazon','Tesla','Netflix','Advanced Micro Devices'),key='st1')
	data = df[df['Company'] == cmp]
	st.subheader(cmp+' Volume trend')
	d2 = data.iloc[:,[2,4]]
	st.bar_chart(d2,x='Date',y='Volume',height=500,width=500,color=np.random.choice(['#ffa200','#00ffbf','#00d5ff','#ff0066','#f54842','#adf542']))
	col = st.columns([0.4,0.6])
	d1 = data.iloc[:,3].values
	fig = px.box(d1)
	col[0].subheader('Statitical Analysis of Stock Price')
	col[1].plotly_chart(fig)
	st.subheader('Co-relation Matrix')
	temp_corr_df = df[['Company', 'Close/Last', 'Date']]
	stocks = {}
	for company in df['Company'].unique():
        	stocks[company] = df[df['Company']==company]['Close/Last'].values.tolist()
	corr_df = pd.DataFrame(stocks,index=temp_corr_df['Date'].unique())
	corr_df = corr_df.corr(method='pearson')
	fig, ax = plt.subplots(figsize=(5,3))
	sns.heatmap(corr_df, annot=True, mask=np.tril(corr_df)==0,ax=ax)
	st.pyplot(fig)

with tab3:
	st.header("DMA Analysis")
	col1, col2 = st.columns(2)
	with col1:
		company = st.selectbox('Select the company',('Apple','Starbucks','Microsoft','Cisco','Qualcomm','Meta','Amazon','Tesla','Netflix','Advanced Micro Devices'),key='st2')
	with col2:
		x = st.slider('Select the startings days',0,2316,1)
		y = st.slider('Select the end days range',x+1,2516,1)
		if y<x or y-x<200:
			y = x+230
		
	AAPL = df[df['Company'] == company]
	AAPL = AAPL.iloc[:,2:]
	AAPL = AAPL.iloc[:,1].values
	AAPL = pd.DataFrame(AAPL,columns=['Close/Last'])
	aapl_dma = AAPL.loc[x:y,'Close/Last'].to_frame()
	aapl_dma['SMA50'] = aapl_dma['Close/Last'].rolling(50).mean()
	aapl_dma['SMA200'] = aapl_dma['Close/Last'].rolling(200).mean()
	aapl_dma['EWA50'] = aapl_dma['Close/Last'].ewm(span=50).mean()
	aapl_dma['EWA200'] = aapl_dma['Close/Last'].ewm(span=200).mean()
	aapl_dma.dropna(inplace=True)
	st.line_chart(aapl_dma,height=600)
