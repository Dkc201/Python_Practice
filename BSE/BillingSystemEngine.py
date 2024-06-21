from multiprocessing import Process
from GenerateBills import GenerateBills
from ProcessBills import ProcessBills
import time

def generate_bill():
    generatebills_obj = GenerateBills()
    while True:
        generatebills_obj.generate_bill()
        time.sleep(3)
    
    
def process_bill():
    bill_json_files_path = 'C:\\Users\\dkc91\\OneDrive\\Desktop\\Python_classes\\My_Python_Code\\BillingSystem\\Bills\\*.json'        
    processbills_obj = ProcessBills(bill_json_files_path)
    while True:
        time.sleep(45)
        processbills_obj.process_bill_json()
        
if __name__=='__main__':
    generatebill_process = Process(target=generate_bill)
    generatebill_process.start()
    processbill_process = Process(target=process_bill)
    processbill_process.start()
