# Input ID number in Czech Republic
# write ouf corect/incorect ID


# MONTHS 30 DAYS
months_30 = [4, 6, 9, 11]

# MONTHS 31 DAYS
months_31 = [1, 3, 5, 7, 8, 10, 12]

# YEARS
years = list(range(86, 100)) + list(range(00, 23))
only_numbers = []

while True:

    ID = list(input('Napiš rodné číslo: '))

    if ID[6] != "/":
        print("chybí lomítko nebo je špatný počet čísel")
        continue

    for number in ID:
        if number.isdigit():
            only_numbers.append(number)

    if not len(only_numbers) == 10:
        print("zadané číslo nemá odpovídající počet znaků")
        only_numbers.clear()
        continue

    modulo_eleven = int(''.join(only_numbers))
    year_ID = int(''.join(only_numbers[:2]))
    month_ID = int(''.join(only_numbers[2:4]))
    day_ID = int(''.join(only_numbers[4:6]))
    end = int(''.join(only_numbers[6:]))

    if end > 6000:
        print('rč je nevalidní')
        only_numbers.clear()
        continue

    if ((modulo_eleven) % 11 == 0) and year_ID in years:
        if month_ID > 50:
            month_ID_all = month_ID - 50
            if month_ID_all == 2 and day_ID <= 29:
                print('Zadané rodné číslo je v pořádku')
                quit()
            elif (month_ID_all in months_30) and day_ID <= 30:
                print('Zadané rodné číslo je v pořádku')
                quit()
            elif (month_ID_all in months_31) and day_ID <= 31:
                print('Zadané rodné číslo je v pořádku')
                quit()
            else:
                print('Rodné číslo je nevalidní')
                break
