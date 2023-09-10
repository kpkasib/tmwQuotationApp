from sheetsDataConverter import sheetData

class app():

        
    def sheetPrice():

        sheetsData = sheetData() #importing sheets data

        companiesNames = sheetsData.keys() #accessing for companies name in data

        print(f"\nChoose Your Company\n")

        for i, companyName in enumerate(companiesNames, start=1):
            print(f"{i}. {companyName}")

        companyChoice = int(input(f"\nChoose from 1 to {len(companiesNames)}: "))

        selectedCompany = list(companiesNames)[companyChoice - 1]
        print(f"\nYou Have selected: {selectedCompany}\n")

        sheetsTypes = sheetsData.get(selectedCompany,{})
        
        for i, (type, price) in enumerate(sheetsTypes.items(), start=1):
            print(f"{i}. {type}: {price}.rs")
        
        sheetChoice = int(input(f"\nChoose from 1 to {len(sheetsTypes)}: "))

        selectedSheet = list(sheetsTypes.keys())[sheetChoice - 1]

        print(f"\nYou Have selected: {selectedSheet}\n")
        
        price = int(sheetsTypes[selectedSheet])

        return price, selectedSheet
    

    def sqftestimator():

        length = int(input(f"\nWall Lenght in ft: "))
        height = int(input(f"\nWall Height in ft: "))

        sqft = length*height

        print(f"\nTotal sqft of {length}ft and {height}ft is {sqft}sqft")

        return sqft
    
    







d = app

sqft = app.sqftestimator()

print(sqft)