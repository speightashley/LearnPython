input_filename = 'country_info.txt'
countries = {}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        countries[country.casefold()] = country_dict


country_choice = input("What country do you want to know? ").casefold()

while True:
    if country_choice in countries:
        print(countries[country_choice]['capital'])
    else:
        print("that's not in my list")
