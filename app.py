import requests

class SecEdgar:
    def __init__(self, fileUrl):
        self.fileUrl = fileUrl
        self.nameDict = {}
        self.tickerDict = {}

        headers = {'user-agent': 'Vanderbilt sean.d.onamade@vanderbilt.edu'}
        r = requests.get(self.fileUrl, headers=headers)

        self.filejson = r.json()

        for entry in self.filejson.values():
            self.nameDict[entry['title']] = (entry['ticker'], entry['cik_str'])
            self.tickerDict[entry['ticker']] = (entry['title'], entry['cik_str'])
        # print(r.text)
        # print(self.filejson)
        

    def name_to_cik(self, title):
        # for entry in self.filejson.values():
        #     if entry['title'] == title:
        #         return (entry['title'], entry['cik_str'], entry['ticker'])
        # return "Entry not found"
        return self.nameDict[title]
            
    def ticker_to_cik(self, ticker):
        # for entry in self.filejson.values():
        #     if entry['ticker'] == ticker:
        #         return (entry['title'], entry['cik_str'], entry['ticker'])
        # return "Entry not found"
        return self.tickerDict[ticker]

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')
print(se.name_to_cik("Apple Inc."))
print(se.ticker_to_cik("GOOGL"))