import requests

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("The amount must be greater than 0")
            else:
                return value
        except ValueError:
            print("The amount must be a numeric value!")

def main():
    init_currency = input("Enter an initial currency: ").upper()
    target_currency = input("Enter a target currency: ").upper()

    amount = get_float_input("Enter the amount: ")

    url = f"https://api.apilayer.com/currency_data/convert?to={target_currency}&from={init_currency}&amount={amount}"

    headers = {
        "apikey": "9Uag7Qne6b6SBJofYI2NrjugZ0R4yiF8"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Sorry, there was a problem: {e}")
        return

    result = response.json()
    print(f"{amount} {init_currency} = {result['result']} {target_currency}")

if __name__ == "__main__":
    main()
