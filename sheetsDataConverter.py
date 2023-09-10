def sheetData():
    # Read the sheets_data.txt file and convert it into a Python dictionary
    sheets_data = {}
    with open('sheetsData.txt', 'r') as file:
        for line in file:
            company, sheet_type, price_str = line.strip().split(',')
            if price_str == 'None':
                price = None
            else:
                price = int(price_str)
            
            if company not in sheets_data:
                sheets_data[company] = {}
            
            sheets_data[company][sheet_type] = price

    # Print the resulting dictionary
    return dict(sheets_data)