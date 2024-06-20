def master_data():
    c_master_data = [
         {"cs_start":100,"cs_end":199,"loan_amt_start":10000,"loan_amt_end":19999,"interest":5  ,"duration":65}
        ,{"cs_start":400,"cs_end":499,"loan_amt_start":10000,"loan_amt_end":19999,"interest":3.5,"duration":65}
        ,{"cs_start":200,"cs_end":299,"loan_amt_start":10000,"loan_amt_end":19999,"interest":4.5,"duration":65}
        ,{"cs_start":300,"cs_end":399,"loan_amt_start":10000,"loan_amt_end":19999,"interest":4  ,"duration":65}
        ]
    return c_master_data
    
def chk_cust_qualify(CreditScore,LoanAmount):
    c_master_data=[]
    c_master_data=master_data()
    #print(c_master_data)
    reject=0
    all_cs=[]
    all_loan_amt=[]
    for chk in c_master_data :
        all_cs.append(chk['cs_start'])
        all_cs.append(chk['cs_end'])
        all_loan_amt.append(chk['loan_amt_start'])
        all_loan_amt.append(chk['loan_amt_end'])

    max_cs=max(all_cs)
    max_loan_amt=max(all_loan_amt)
    min_cs=min(all_cs)
    min_loan_amt=min(all_loan_amt)
    #print('Credit Score should be between',min_cs,'and',max_cs)
    #print('Loan Amount should be between',min_loan_amt,'and',max_loan_amt)

    if CreditScore>max_cs or CreditScore<min_cs or LoanAmount>max_loan_amt or LoanAmount<min_loan_amt :
        #print('CreditScore :',CreditScore,'and LoanAmount :', LoanAmount,' are not enough for the loan')
        reject=1
    return reject



def Calculate_TotalLoanAmount(CreditScore,LoanAmount) :
    c_master_data=master_data()
    reject=chk_cust_qualify(CreditScore,LoanAmount)
    
    if reject==0 :   
        for c in c_master_data:
    #print(c)
    #print(c['cs_start'])
            if CreditScore>=c['cs_start'] and CreditScore<=c['cs_end'] and LoanAmount>=c['loan_amt_start'] and LoanAmount<=c['loan_amt_end']:
                TotalAmount = LoanAmount + (LoanAmount/100)*c['interest']
                print('You have to pay', TotalAmount,'for',c['duration'],'months and interest rate will be',c['interest'],'%')
               
    else :
        print('Either Credit Score or Loan Amount is not suffecient')
                
l_CustomerName='A'
l_CreditScore=30
l_LoanAmount=10029

Calculate_TotalLoanAmount(l_CreditScore,l_LoanAmount)

  
#reject=chk_cust_qualify(300,109)
#print(reject)
