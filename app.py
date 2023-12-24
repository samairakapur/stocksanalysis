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

	st.subheader("Introduction") 
	container = st.container(border=True)
	container.write("Hi, welcome to this website! It is written by a Grade 11 student who was interested in learnig more about stocks!")
	
	img = Image.open('stocks.jpeg')
	
	st.subheader("What are stocks?") 
	col1, col2 = st.columns(2, gap = "small") 
	col1.image(img)
	col2.write("Stocks, also known as shares or equities, represent ownership in a company. When you purchase stocks, you become a shareholder and own a portion of the company. Companies issue stocks to raise capital for various purposes, such as expansion, research, and development.")
	col2.write("The terminology used for stocks can often sound like a new language. Therefore, if you are new to stocks, below is a list of 10 key terms and concepts I found useful to know when learning more about stocks")

	

	with st.expander("Stocks Terminology"):
		img2 = Image.open('keyterms.jpg')
		st.image(img2)
		st.write("1. Equity") 
		st.write("Equity (in the stock market) refers to the amount of shares owned by a company. As an investor, when you buy the shares of a company, you buy an equivalent degree of ownership in that company. The stock market is where these company shares (equity) are bought and sold from one investor to another. The word ‘stock’ is synonymous with the word 'equity.")
		st.write("2. Bull Market / Bear Market")
		st.write("These two terms are indicators of the current trend that the stock market is experiencing at a given time. The bull market refers to a period in which the prices of stocks are increasing and therefore, the market is on an upward trend. A bear market refers to a period in which the prices of stocks are falling and therefore, the market is on a downward")
		st.write("3. Bid / Ask")
		st.write("The ask price or an offer refers to the lowest amount of money that the seller of a stock is willing to accept for a share of that stock whilst a bid refers to the highest amount of money that a potential buyer for a stock is willing to pay for a share of that stock. If there are multiple buyers for a stock, a bid taken between buyers ends when one buyer places a bid that the other buyers cannot or do not wish to match.")
		st.write("4. Exchange")
		st.write("An exchange refers to a place or an electronic market where various securities are traded. i.e. one of the many stock exchanges in the country or worldwide where shares of stocks are bought and sold.")
		st.write("5. Volatility") 
		st.write("Volatility refers to the rate of price fluctuations of a share. A highly volatile stock experiences daily up and down movements in its price. Some traders profit off the risks involved in highly volatile stocks, while others prefer investing in less volatile stocks for the long run.")
		st.write("6. Blue-Chip Stocks")
		st.write("Stocks of large, well-established, and financially stable companies with a history of reliable performance.")
		st.write("7. Price to Earning (P/E) ratio")
		st.write("A valuation of companies last traded share price to its latest reported 12 months earnings per share. For example, if the last traded share price of any X company is $40 and earnings over a last 12 months per share is $20 then the P/E ratio of that X company is $20 (40/2)")
		st.write("8. Price to Book (P/B) ratio")
		st.write("The Price-to-Book (P/B) ratio is a financial metric used to evaluate a company's market value relative to its book value. It is calculated by dividing the market price per share by the book value per share. The P/B ratio provides insights into how the market values a company in relation to its accounting book value.")
		st.write("9. Divident")
		st.write("A portion of the company’s earnings decided to pay to its shareholders in return for their investments. It is usually declared as a percentage of current share price or some specified dollar value, usually decided by the board of directors of the company.")
		st.write("10. Mid-Cap")
		st.write("Mid-cap, short for ‘mid-capitalization,’ refers to companies with a market capitalization between that of large-cap (large capitalization) and small-cap (small capitalization) companies. Market capitalization is calculated by multiplying the current stock price by the total number of outstanding shares.")

	img1 = Image.open('stockmarket.jpg')
	img3 = Image.open('stockm.jpg')
	
	st.subheader("What is Stock Market and Stock Market Analysis?")
	col3, col4 = st.columns(2, gap = "small") 
	col4.image(img1)
	col3.write(" The term stock market refers to several exchanges between buyers and sellers in which the shares of publicly held companies are bought and sold. The stock market consists of components of a free-market economy because they enable democratized access to investor trading and exchange of capital, whilst also enabling the creation of efficient price discovery and efficient dealing.")
	col3.write("Stock markets provide a secure and regulated environment where market participants can transact in shares and other eligible financial instruments with confidence, with zero to low operational risk. Operating under the defined rules as stated by the regulator, the stock markets act as primary markets and secondary markets.")
	col3.write("Primary market is where stocks are issued and sold for the first time, typically through processes like initial public offerings (IPOs). Companies use the primary market to raise capital by selling shares directly to investors.")
	
	col4.image(img3)
	
	col3.write("Secondary market is where existing stocks, previously issued in the primary market, are bought and sold among investors. It provides a platform for the trading of stocks and other financial instruments after their initial issuance.")
	col3.write("A company divides itself into several shares and sells some of those shares to the public at a price per share. To facilitate this process, a company needs a marketplace where these shares can be sold and this is achieved by the stock market. Investors will own company shares in the expectation that share value will rise or that they will receive dividend payments or both.")
	
	col3.write("Stock analysis is a method for investors and traders to make buying and selling decisions. By studying and evaluating past and current data, investors and traders attempt to gain an edge in the markets by making informed decisions.")
	col3.write("The notion of stock analysis relies on the assumption that available market information can be used to determine the intrinsic value of a stock, especially by leveraging the historical information of the stock")
	col3.write("the types of stock analysis that exist range from:")
	col3.write(" - fundamental analysis")
	col3.write(" - technical analysis")
	col3.write(" - quantitave analysis") 
	col3.write("Each analysis technique has its benefits and limitations") 

	img4 = Image.open('topstocks.jpeg')
	img5 = Image.open('tableinfo.jpg')
	img6 = Image.open('bigstocks.jpg')
	
	st.subheader("Top Indices and Stock Markets in the world") 
	col5, col6 = st.columns(2, gap = "small") 
	col5.image(img4)
	col6.image(img6)

	st.image(img5)
	container1 = st.container(border=True)
	container1.write("Today, there are roughly 80 major stock exchanges worth a combined $110.2 trillion in value. The world’s top two exchanges, the New York Stock Exchange (NYSE) and the Nasdaq, command 42.4% of global market capitalisation.")
	container1.write("The visualisation above shows the largest stock exchanges in the world, with data from the World Federation of Exchanges (WFE).")
	container1.write(" The top seven stocks in the world are known as the 'Magnificent Seven' (shown in the visual above) are megacap companies focused and capitalizing on tech growth trends including AI, cloud computing, and cutting-edge hardware and software.")
	container1.write("The table above ranks the 'Mega Comapnies' by their market capitalization on November 6, 2023, alongside their 5-year stock performance")
	container1.write("Imagine if you had just invested only a thousand dollars in Tesla 5 years ago (in 2018), the value of the investment would be close to ten thousand dollars today!") 

	st.subheader("Why should you start investing in stocks?")
	col7, col8 = st.columns(2, gap = "small") 
	col7.write("3 Grand Benefits of Investing in Stocks Include:")
	col7.write("1. Ability to achieve financial goals") 
	col7.write("Investing early allows individual's to harness the power of compounding Compounding refers to the snowball effect where your investment returns generate additional returns over time. The earlier you start, the more time your money has to compound, potentially leading to significant long-term gains. Therefore, investing early is a key trategy for achieving financial goals such as buying a home, funding education, or enjoying a comfortable retirement. The growth potential of investments can assist in reaching these milestones more effectively than relying solely on savings.") 
	col7.write("2. Ability to protect family from inflation")
	col7.write("Stock market's returns often significantly outpace the rate of inflation. For example, the long-term inflation rate has run about 3.1% annually since 1913. That compares to a double-digit annual return from stocks. Stocks have been a good way to hedge against inflation.")
	col7.write("3. Earn a passive income") 
	col7.write("Many companies pay dividends, or a portion of their profits, to investors. The majority make quarterly dividend payments, although some companies pay monthly dividends. Dividend income can help supplement an investor's paycheck or retirement income.")
	
	col8.write("Risks of investing in stock that you should keep at the back of your mind")
	col8.write("1. Lack of guarenteed returns") 
	col8.write("Unlike savings accounts or certain fixed-income investments, the returns on many investments are not guaranteed. Market conditions and the performance of individual assets can vary, leading to uncertainty in returns.")
	col8.write("2. Market Volatility") 
	col8.write("Stock prices can be highly volatile, experiencing frequent and sometimes unpredictable fluctuations. This volatility is influenced by various factors such as economic conditions, geopolitical events, and investor sentiment. Rapid and unpredictable changes in stock prices can lead to short-term losses and make it challenging for investors to accurately time their trades.")
	col8.write("3. Research involvement") 
	col8.write("Successful investing often requires a good understanding of financial markets, economic factors, and individual securities. Keeping up with research and staying informed about market trends can be time-consuming and challenging for some investors.")

	st.subheader("Useful resources to gain better understanding on stocks + what I learnt") 
	st.markdown("[![Click me](app/static/medium.png)](https://medium.com/@asady/how-to-analyze-stocks-an-introductory-guide-ed9266354c76)")
	
	st.subheader("About Me")
	img7 = Image.open('aboutme.jpg')
	col9, col10 = st.columns(2, gap = "small") 
	col10.image(img7)
	col9.write("this is where I will write information about myself")

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
