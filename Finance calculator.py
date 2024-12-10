def calculate_finance(monthly_income:float,tax_rate:float,monthly_expenditure:float,curr:str) -> None:
    monthly_tax: float = monthly_income * (tax_rate/100)
    monthly_net_income: float = monthly_income - monthly_tax - monthly_expenditure
    yearly_income: float = monthly_income*12
    yearly_tax: float = monthly_tax*12
    yearly_expenditure: float = monthly_expenditure*12
    yearly_net_income: float = yearly_income - yearly_tax - yearly_expenditure

    print('-'*50)
    print(f"Tax rate = {tax_rate:.0f}%")

    print(f"Monthy income = {curr}{monthly_income:,.2f}")
    print(f"Monthy tax = {curr}{monthly_tax:,.2f}")
    print(f"Monthy expenditure = {curr}{monthly_expenditure:,.2f}")
    print(f"Monthy net income = {curr}{monthly_net_income:,.2f}")

    print(f"Yearly income = {curr}{yearly_income:,.2f}")
    print(f"Yearly tax = {curr}{yearly_tax:,.2f}")
    print(f"Yearly expenditure = {curr}{yearly_expenditure:,.2f}")
    print(f"Yearly net income = {curr}{yearly_net_income:,.2f}")
    print('-'*50)

def main() -> None:
    monthly_income: str = input("Enter your Monthy income: ")
    tax_rate: str = input("Enter your Tax rate: ")
    monthly_expenditure: str = input("Enter Monthy Expendiure: ")

    if not monthly_income.replace(".",'',1).isnumeric():
        print("Enter number for Monthly Income")
        
    if not tax_rate.replace(".",'',1).isnumeric():
        print("Enter number for Tax Rate")

    if not monthly_expenditure.replace(".",'',1).isnumeric():
        print("Enter number for Monthly Expenditure")

    calculate_finance(float(monthly_income),float(tax_rate),float(monthly_expenditure),"₹")

if __name__=="__main__":
    main()