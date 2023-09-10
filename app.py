from sheetsDataConverter import sheetData

class app():

    def sheetChooser():

        sheetsData = sheetData() #sheet data dictionary
        companyNames = sheetsData.keys() #

        print(type(companyNames))
        print(companyNames)

        print("What is your Company")

        i = 1

        for companyName in companyNames:
            print(f"{i}. {companyName}")
            i += 1
        
        CompanyChoice = int(input(f"Choose from 1 to {len(companyNames)}: "))
        print("\n")

        # companyNames = list(companyNames)[CompanyChoice - 1]
        companyNames = companyNames[CompanyChoice - 1]

        sheetsType = sheetsData.get(companyNames, {})

        i = 1

        for sheetTypes, sheetPrices in sheetsType.items():
            print(f"{i}. {sheetTypes} Rs.{sheetPrices}")
            i += 1

        sheetTypeChoice = int(input(f"Choose from 1 to {len(sheetsType)}: "))
        print("\n")
        

        




d = app.sheetChooser()
d