from lms.MasterData import MasterData
from lms.QualifyCustomer import QualifyCustomer

l_customername = None
l_creditscore = None
l_loanamount = None
print ('\nHello Dear Customer\n')

while True :
    l_customername= input('Enter your name :')
    if not l_customername.isalpha():
        print("That is not a valid Name")
    else:
        break
while True :
    l_creditscore= input('Enter your CreditScore : ')
    if not l_creditscore.isnumeric():
        print("That is not a valid CreditScore")
    else:
        l_creditscore= int(l_creditscore)
        break
while True:
    l_loanamount= input ('Enter your LoanAmount : ')
    if not l_loanamount.isnumeric(): 
        print("That is not a valid LoanAmount")
    else:
        l_loanamount= int(l_loanamount)
        break

def totalloanAmount(p_creditScore,p_loanAmount,p_masterdata) :
        masterdata = p_masterdata
        creditscore = p_creditScore
        loanamount = p_loanAmount
        for data in masterdata:
            if creditscore >= int(data['CS_START']) and creditscore <= int(data['CS_END']) and loanamount >= int(data['LOAN_AMOUNT_START']) and loanamount <= int(data['LOAN_AMOUNT_END']):
                total_loan_amount = loanamount + (loanamount/100) * float(data['INTEREST'])
                print(f"You have to pay {total_loan_amount} for {data['DURATION']} months and interest rate will be {data['INTEREST']} %")                  


lms_masterdata_file_path="C:/Users/dkc91/OneDrive/Desktop/Python_classes/My_Python_Code/lms_project/lms_masterdata.csv"
objmd = MasterData(lms_masterdata_file_path)
dict_masterdata = objmd.buildmasterdata()
masterdata = dict_masterdata['Data']
# print (masterdata)

objQC = QualifyCustomer(l_creditscore,l_loanamount,masterdata)
dict_customer_qualify = objQC.check_customer_qualification()
if dict_customer_qualify['Status']=='Success':
    totalloanAmount(l_creditscore,l_loanamount,masterdata)
else:
    print(dict_customer_qualify['message'])
