import pandas as pd
colname=['ID','SecType','Date','Time','Ask','Ask volume','Bid','Bid volume','Ask time','Day high ask','Close','Currency','Days high ask time','Days high','ISIN','Auction price','Days low ask','Days low','Days low ask time','Open','Nominal value','Last','Last volume','Trading time','Total volume','Mid price','Trading date','Profit','Current price','Related indices','Day high bid time',' Day low bid time','Open Time', 'Last trade time','Close Time', 'Day high Time', 'Day low Time','Bid time','Auction Time']
def main(): 
    data=pd.read_csv(filepath_or_buffer="../../../Downloads/out600_combined+header.csv",header=0,low_memory=False)
    print(data['ID'])
    data['Date'] = data['Date'].astype(str)
    data['Time'] = data['Time'].astype(str)
    print(data)
    data2=data.sort_values(by=['Date','Time'])
    print(data2)
    data2.to_csv("FileDataOrdered.csv",index=False,encoding='utf-8')
if __name__ == '__main__':
    main()