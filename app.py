import requests
from bs4 import BeautifulSoup

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
        return self.nameDict.get(title, "Entry Not Found")
            
    def ticker_to_cik(self, ticker):
        # for entry in self.filejson.values():
        #     if entry['ticker'] == ticker:
        #         return (entry['title'], entry['cik_str'], entry['ticker'])
        # return "Entry not found"
        return self.tickerDict.get(ticker, "Entry Not Found")
    
class SecEdgar2:
    def __init__(self, fileUrl):
        self.fileUrl = fileUrl

        headers = {'user-agent': 'Vanderbilt sean.d.onamade@vanderbilt.edu'}
        try:
            self.p = requests.get(self.fileUrl, headers=headers)
            self.filejson = self.p.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {self.fileUrl}: {e}")
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON response.")
        
        # print(self.p.text)

    def annual_filing(self, cik, year):
        if not self.filejson:
            print("No valid JSON data available.")
            return
        filing_dates = self.filejson['filings']['recent']['filingDate']
        primaryDocDescs = self.filejson['filings']['recent']['primaryDocDescription']
        counter = 0
        while counter < len(primaryDocDescs):
            if str(year) in filing_dates[counter] and ("10-K" in primaryDocDescs[counter]):
                break
            counter += 1
        if counter >= len(filing_dates) or counter >= len(primaryDocDescs):
            print(f"No filings for the year {year}")
            return
        accession = self.filejson['filings']['recent']['accessionNumber'][counter].replace('-', '')
        primaryDoc = self.filejson['filings']['recent']['primaryDocument'][counter]
        coolStr = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{primaryDoc}"
        print(f"Link for submission for {self.filejson['name']}: \n")

        headers = {'user-agent': 'Vanderbilt sean.d.onamade@vanderbilt.edu'}
        r = requests.get(coolStr, headers=headers)
        if r.status_code == 200:
            try:
                r.json()
            except:
                print("Received non-JSON response for document.")
                soup = BeautifulSoup(r.text, 'html.parser')  # Parse the HTML
                pretty_html = soup.prettify()  # Format it nicely
                print(pretty_html) 
        else:
            print("Error fetching doc")

        print("Page accessible at: ")
        return coolStr
    

    def quarterly_filing(self, cik, year, quarter):
        if not self.filejson:
            print("No valid JSON data available.")
            return
        filing_dates = self.filejson['filings']['recent']['filingDate']
        quarters = {
            1: (f"{year}-01-01", f"{year}-03-31"),
            2: (f"{year}-04-01", f"{year}-06-30"),
            3: (f"{year}-07-01", f"{year}-09-30"),
            4: (f"{year}-10-01", f"{year}-12-31"),
        }
        if quarter not in quarters:
            print("Invalid quarter. Enter one between 1 and 4.")
            return
        start_date, end_date = quarters[quarter]
        primaryDocDescs = self.filejson['filings']['recent']['primaryDocDescription']

        
        counter = 0
        while counter < len(filing_dates):
            if str(year) in filing_dates[counter] and ("10-Q" in primaryDocDescs[counter]):
                if start_date <= filing_dates[counter] <= end_date:
                    break
            counter += 1
        if counter >= len(filing_dates):
            print(f"No filings for the year {year}")
            return
            # handle error here later
        
        accession = self.filejson['filings']['recent']['accessionNumber'][counter].replace('-', '')
        primaryDoc = self.filejson['filings']['recent']['primaryDocument'][counter]
        coolStr = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{primaryDoc}"
        print(f"Link for submission for {self.filejson['name']}: \n")

        headers = {'user-agent': 'Vanderbilt sean.d.onamade@vanderbilt.edu'}
        r = requests.get(coolStr, headers=headers)
        if r.status_code == 200:
            try:
                r.json()
            except:
                print("Received non-JSON response for document.")
                soup = BeautifulSoup(r.text, 'html.parser')  # Parse the HTML
                pretty_html = soup.prettify()  # Format it nicely
                print(pretty_html) 
        else:
            print("Error fetching doc")

        print("Page accessible at: ")
        return coolStr
        

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')
print(se.name_to_cik("Apple Inc."))
print(se.ticker_to_cik("GOOGL"))
while True:
    print("\nTicker/Name Search")
    x = input("Put in a name or ticker (case-sensitive), or enter q to quit: \n")
    if x == "q": 
        break
    else:
        y = se.name_to_cik(x)
        if y == "Entry Not Found":
            y = se.ticker_to_cik(x)
        print(f"\nInfo on {x}: {y}")

# cik_num = input("\nInput your CIK Number: ")
# # 320193
# cik_str = str(cik_num).zfill(10)
# newFunc = f"https://data.sec.gov/submissions/CIK{cik_str}.json" # note this 0000 method doesn't work for longer numbers like Google's 1652044. Find a way to fix this.
# se2 = SecEdgar2(newFunc)

# print(se2.annual_filing(cik_num, 2023))
# print(se2.quarterly_filing(cik_num, 2023, 3))
while True:
    print("\nFiling Doc Search:")
    cik_num = input("Put in a ticker, or enter q to quit: \n")
    if cik_num == "q": 
        break
    else:
        cik_str = str(cik_num).zfill(10)
        newFunc = f"https://data.sec.gov/submissions/CIK{cik_str}.json" # note this 0000 method doesn't work for longer numbers like Google's 1652044. Find a way to fix this.
        se2 = SecEdgar2(newFunc)
        choice = input("\nPut in 1 for annual, 2 for quarters: \n")
        if choice == "1":
            choice2 = input("\nChoose a year: ")
            print(se2.annual_filing(cik_num, int(choice2)))
        elif choice == "2":
            choice2 = input("\nChoose a year: ")
            choice3 = input("Choose a quarter between 1 and 4: ")
            print(se2.quarterly_filing(cik_num, int(choice2), int(choice3)))
        break

