from pytrends.request import TrendReq
import pandas as pd
import time
startTime = time.time()
pytrend = TrendReq(hl='en-GB', tz=360)

colnames = ["advertising","ai","art","business service","cannabis","charity","communication","computing","crowdfunding","cybersecurity","debit cards","deflationary", "eCommerce", "education","energy","entertainment","exchange","fan tokens","filesharing","gambling","gaming","governance","healthcare","identity","interest earning","insurance","iot","lending","marketplace","media","prediction","real estate","sports","storage","transportation","travel","virtual reality"]
df = pd.DataFrame([], columns = colnames)
dataset = []

for x in colnames:
    pytrend.build_payload([x,'bitcoin'],cat=0,timeframe='2021-01-01 2021-12-25',geo='GB')
    data = pytrend.interest_over_time()
     
    if not data.empty:
        data = data.drop(labels=['isPartial'],axis='columns')
        dataset.append(data[x])

result = pd.concat(dataset, axis=1)

# grab the top 5 sector
mean_list = result.mean()
mean_list.nlargest(5)

