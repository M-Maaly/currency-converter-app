import requests

init_currency = input("Enter an initial currency: ").upper()
target_currency = input("Enter a target currency: ").upper()

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a numeric value!")
        continue

    if amount == 0:
        print("The amount must be greater than 0")
        continue
    else:
        break


url = ("https://api.apilayer.com/currency_data/convert?to="
    + target_currency + "&from=" + init_currency + "&amount=" + str(amount))

payload = {}
headers= {
  "apikey": "9Uag7Qne6b6SBJofYI2NrjugZ0R4yiF8"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if status_code != 200:
    print("Sorry, there was a problem. please try again later.")
    quit()

result = response.json()

print(f"{amount} {init_currency} = {result['result']} {target_currency}")