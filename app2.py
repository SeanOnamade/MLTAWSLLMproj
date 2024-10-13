import requests
from bs4 import BeautifulSoup
import boto3
import json
from datetime import datetime

class SecEdgar:
    def __init__(self, bucket_name, file_key):
        self.nameDict = {}
        self.tickerDict = {}

        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        self.filejson = json.loads(response['Body'].read())

        for entry in self.filejson.values():
            self.nameDict[entry['title']] = (entry['ticker'], entry['cik_str'])
            self.tickerDict[entry['ticker']] = (entry['title'], entry['cik_str'])

    def name_to_cik(self, title):
        return self.nameDict.get(title, "Entry Not Found")

    def ticker_to_cik(self, ticker):
        return self.tickerDict.get(ticker, "Entry Not Found")

    
import requests
from bs4 import BeautifulSoup

class SecEdgar2:
    def __init__(self, cik):
        self.cik = str(cik).zfill(10)
        self.base_url = f"https://data.sec.gov/submissions/CIK{self.cik}.json"
        self.headers = {'User-Agent': 'Vanderbilt sean.d.onamade@vanderbilt.edu'}
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        try:
            response = self.session.get(self.base_url)
            response.raise_for_status()
            self.company_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {self.base_url}: {e}")
            self.company_data = None

    def annual_filing(self, year):
        if not self.company_data:
            print("No valid JSON data available.")
            return None

        filings = self.company_data.get('filings', {}).get('recent', {})
        filing_dates = filings.get('filingDate', [])
        doc_descriptions = filings.get('form', [])
        accession_numbers = filings.get('accessionNumber', [])
        primary_documents = filings.get('primaryDocument', [])

        for i in range(len(filing_dates)):
            if str(year) in filing_dates[i] and doc_descriptions[i] == '10-K':
                accession = accession_numbers[i].replace('-', '')
                primary_doc = primary_documents[i]
                document_url = f"https://www.sec.gov/Archives/edgar/data/{int(self.cik)}/{accession}/{primary_doc}"
                return document_url

        print(f"No annual filings found for the year {year}.")
        return None

    def quarterly_filing(self, year, quarter):
        if not self.company_data:
            print("No valid JSON data available.")
            return None

        filings = self.company_data.get('filings', {}).get('recent', {})
        filing_dates = filings.get('filingDate', [])
        doc_descriptions = filings.get('form', [])
        accession_numbers = filings.get('accessionNumber', [])
        primary_documents = filings.get('primaryDocument', [])

        # Define quarter ranges
        quarters = {
            1: ('01-01', '03-31'),
            2: ('04-01', '06-30'),
            3: ('07-01', '09-30'),
            4: ('10-01', '12-31'),
        }

        if quarter not in quarters:
            print("Invalid quarter. Must be an integer between 1 and 4.")
            return None

        start_date = f"{year}-{quarters[quarter][0]}"
        end_date = f"{year}-{quarters[quarter][1]}"

        for i in range(len(filing_dates)):
            filing_date = filing_dates[i]
            if start_date <= filing_date <= end_date and doc_descriptions[i] == '10-Q':
                accession = accession_numbers[i].replace('-', '')
                primary_doc = primary_documents[i]
                document_url = f"https://www.sec.gov/Archives/edgar/data/{int(self.cik)}/{accession}/{primary_doc}"
                return document_url

        print(f"No quarterly filings found for Q{quarter} {year}.")
        return None

        

# se = SecEdgar('https://www.sec.gov/files/company_tickers.json')
# print(se.name_to_cik("Apple Inc."))
# print(se.ticker_to_cik("GOOGL"))
# while True:
#     print("\nTicker/Name Search")
#     x = input("Put in a name or ticker (case-sensitive), or enter q to quit: \n")
#     if x == "q": 
#         break
#     else:
#         y = se.name_to_cik(x)
#         if y == "Entry Not Found":
#             y = se.ticker_to_cik(x)
#         print(f"\nInfo on {x}: {y}")

# cik_num = input("\nInput your CIK Number: ")
# # 320193
# cik_str = str(cik_num).zfill(10)
# newFunc = f"https://data.sec.gov/submissions/CIK{cik_str}.json" # note this 0000 method doesn't work for longer numbers like Google's 1652044. Find a way to fix this.
# se2 = SecEdgar2(newFunc)

# print(se2.annual_filing(cik_num, 2023))
# print(se2.quarterly_filing(cik_num, 2023, 3))
# while True:
#     print("\nFiling Doc Search:")
#     cik_num = input("Put in a ticker, or enter q to quit: \n")
#     if cik_num == "q": 
#         break
#     else:
#         cik_str = str(cik_num).zfill(10)
#         newFunc = f"https://data.sec.gov/submissions/CIK{cik_str}.json" # note this 0000 method doesn't work for longer numbers like Google's 1652044. Find a way to fix this.
#         se2 = SecEdgar2(newFunc)
#         choice = input("\nPut in 1 for annual, 2 for quarters: \n")
#         if choice == "1":
#             choice2 = input("\nChoose a year: ")
#             print(se2.annual_filing(cik_num, int(choice2)))
#         elif choice == "2":
#             choice2 = input("\nChoose a year: ")
#             choice3 = input("Choose a quarter between 1 and 4: ")
#             print(se2.quarterly_filing(cik_num, int(choice2), int(choice3)))
#         break

