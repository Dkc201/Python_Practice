from lms.MasterData import MasterData

class QualifyCustomer:

    def __init__(self, p_creditscore, p_loanamount, p_masterdata):
        self.creditscore = p_creditscore
        self.loanamount = p_loanamount
        self.masterdata = p_masterdata
    
    def check_customer_qualification(self):
        all_csstart = []
        all_csend = []
        all_loanamountstart = []
        all_loanamountend = []
        for data in self.masterdata:
                all_csstart.append(data['CS_START'])
                all_csend.append(data['CS_END'])
                all_loanamountstart.append(data['LOAN_AMOUNT_START'])
                all_loanamountend.append(data['LOAN_AMOUNT_END'])
        # print (f"{all_csstart} \n {all_csend}")
        
        min_csstart = int(min(all_csstart))
        max_csend = int(max(all_csend))
        min_loanamountstart = int(min(all_loanamountstart))
        max_loanamountend = int(max(all_loanamountend))
        # print(min_loanamountstart,max_loanamountend)
        # print(min_csstart,max_csend)
        
        if (self.creditscore >= min_csstart and self.creditscore <= max_csend) and (self.loanamount >= min_loanamountstart and self.loanamount <= max_loanamountend):
            return {"Operation":"Check_customer_qualification"
                ,"Status":"Success"
                ,"message":"Customer is qualified for the loan"
            }
            
        if (self.creditscore < min_csstart or self.creditscore > max_csend) and (self.loanamount < min_loanamountstart or self.loanamount > max_loanamountend):
            return {"Operation":"Check_customer_qualification"
                ,"Status":"Failed"
                ,"message":"Creditscore and loanamount do not fit in the criteria"
            }
            
        if (self.creditscore < min_csstart or self.creditscore > max_csend):
            return {"Operation":"Check_customer_qualification"
                ,"Status":"Failed"
                ,"message":"Creditscore does not fit in the criteria"
            }
            
        if (self.loanamount < min_loanamountstart or self.loanamount > max_loanamountend):
            return {"Operation":"Check_customer_qualification"
                ,"Status":"Failed"
                ,"message":"Loanamount does not fit in the criteria"
            } 
       
                
"""

#### To Test This Class and Functions #######       
        
        
lms_masterdata_file_path="C:/Users/dkc91/OneDrive/Desktop/Python_classes/My_Python_Code/lms_project/lms_masterdata.csv"
objmd = MasterData(lms_masterdata_file_path)
dict_masterdata = objmd.buildmasterdata()
masterdata = dict_masterdata['Data']
# print (masterdata)

objQC = QualifyCustomer(378,1000,masterdata)
print(objQC.check_customer_qualification())
       
""" 
        
