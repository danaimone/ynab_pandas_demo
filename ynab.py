import requests
import argparse
import pandas as pd
import json

parser = argparse.ArgumentParser("A simple demo of YNAB API and Pandas")
parser.add_argument("token", help="Your personal YNAB API token")
args = parser.parse_args()
token = args.token

session = requests.Session()
header = {'Authorization': f'Bearer {token}'}
session.headers.update(header)

# Figuring out your budget ID
response = session.get(f'https://api.youneedabudget.com/v1/budgets/')
data = response.json()
print(data)
budget = data["data"]["budgets"][0]
budget_id = budget.get("id")

# Get all your transactions in your budget
response = session.get(
    f'https://api.youneedabudget.com/v1/budgets/{budget_id}/transactions/').json()

df = pd.json_normalize(response["data"]["transactions"])
print(df)
