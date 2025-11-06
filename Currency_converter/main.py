EXCHANGE_RATES = {
    'IDR': 16500.0,
    'EUR': 0.85,
    'USD': 1.0,
    'JPY': 147.87,
    'MYR': 4.201
}

history_converter = []
continue_user = True


def currency_converter(amount, source, target):
    if source_currency not in EXCHANGE_RATES:
        return None
    convert_to_usd = amount / EXCHANGE_RATES[source]
    convert_usd_to_target_currency = convert_to_usd * EXCHANGE_RATES[target]
    return convert_usd_to_target_currency


while continue_user == True:
    while True:
        try:
            amount = float(input('Enter the amount: '))
            break
        except:
            print('Input just number!')
            continue

    while True:
        source_currency = input(
            f'Source currency ({"/".join(EXCHANGE_RATES.keys())}): ').upper()
        if source_currency in EXCHANGE_RATES:
            break
        else:
            print('Invalid Input! Please chocie from the available currency')

    while True:
        target_currency = input(
            f'Source currency ({"/".join(EXCHANGE_RATES.keys())}): ').upper()
        if target_currency in EXCHANGE_RATES:
            break
        else:
            print('Invalid Input! Please chocie from the available currency')


    print(f'{amount} {source_currency} is equal to: {currency_converter(amount,source_currency,target_currency)} {target_currency}')

    result_for_history = f'{amount} {source_currency} --> {currency_converter(amount, source_currency, target_currency)} {target_currency}'
    history_converter.append(result_for_history)

    while True:
        user_continue = input('Convert another?(y/n): ').lower()
        if user_continue == 'n':
            continue_user = False
            break
        elif user_continue == 'y':
            break
        else:
            print('Input invalid! Please enter y or n')


print('-- Converter History --')    
for i, items in enumerate(history_converter):
    print(f'{i + 1}. {items}')
print('-----------------------')
print('Thaks for using this converter')
