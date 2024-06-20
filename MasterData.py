import csv
import os


class MasterData:

    def __init__(self, p_lms_masterdata_file_path):
        self.lms_masterdata_file_path = p_lms_masterdata_file_path


    def validation_masterdata(self,p_lms_masterdata):
        data = None
        try:
            passflag=int(p_lms_masterdata[0])
            passflag=int(p_lms_masterdata[1])
            passflag=int(p_lms_masterdata[2])
            passflag=int(p_lms_masterdata[3])
            passflag=float(p_lms_masterdata[4])
            passflag=int(p_lms_masterdata[5])
        except:
            return{'Operation':'validation_masterdata','status':'Failed','message': 'Incorrect one or more field Data : '+', '.join([str(elem) for elem in p_lms_masterdata])} 
        else:
            return{'Operation':'validation_masterdata','status':'success','message':'Valid Data'}
        
        
    def buildmasterdata(self):
        if os.path.exists(self.lms_masterdata_file_path):
            with open(self.lms_masterdata_file_path) as lms_MD_file:
                lms_MD_filereader=csv.reader(lms_MD_file)

                header=[]
                header=next(lms_MD_file)
                # print(header)

                lms_masterdata=[]
                for row in lms_MD_filereader:
                    if self.validation_masterdata(row)['status']=='success':
                        lms_masterdata.append({'CS_START':row[0],
                                     'CS_END':row[1],
                                     'LOAN_AMOUNT_START':row[2],
                                     'LOAN_AMOUNT_END':row[3],
                                     'INTEREST':row[4],
                                     'DURATION':row[5],
                                     })
                    else:
                        return self.validation_masterdata(row)
                    
                #print(rows)
            return {'Operation':'buildmasterdata','Status':'Success','Data':lms_masterdata}
        else :
            return{'Operation':'buildmasterdata','Status':'Failed','message':'File could not find'}
            
"""
#### To Test This Class and Functions #######

lms_masterdata_file_path="C:/Users/dkc91/OneDrive/Desktop/Python_classes/My_Python_Code/lms_project/lms_masterdata.csv"
objmd=MasterData(lms_masterdata_file_path)               
print(objmd.buildmasterdata())
"""
