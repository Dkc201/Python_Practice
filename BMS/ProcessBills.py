import pymysql
import csv,os,shutil
import json
import glob

class ProcessBills:
    def __init__(self,p_bill_json_files_path):
        self.bill_json_files_path = p_bill_json_files_path
        
        
    def read_bill_json_files(self):
        list_bill_json_files = []
        for bill_json_file in glob.glob(self.bill_json_files_path):
            list_bill_json_files.append(bill_json_file)
        return list_bill_json_files
        
    
    def insert_into_database(self,bill_csvfile,billdetails_csvfile):
        try:
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='billingsystem')
        except pymysql.err.OperationalError as error:
            print("Unable to make a connection to the mysql database")
        else:
            print("Successfully connected to mysql Database") 
            cursor = connection.cursor()
            if os.path.exists(bill_csvfile):
                with open(bill_csvfile) as billcsvfile:
                    bill_csvfile_data = csv.reader(billcsvfile)
                    header = []
                    header = next(bill_csvfile_data)
                    bill_insert_query = "insert into bill(bill_id,bill_date,store_id,bill_total) values(%s,%s,%s,%s)"
                    for row in bill_csvfile_data:
                        bill_id = row[0]
                        bill_date = row[1]
                        store_id = int(row[2])
                        bill_total = float(row[3])
                        record = (bill_id,bill_date,store_id,bill_total)
                        cursor.execute(bill_insert_query,record)
                connection.commit()
                print("Data inserted in to bill table")
            else:
                print("Path does not exist")
            if os.path.exists(billdetails_csvfile):
                with open(billdetails_csvfile) as billdetailscsvfile:
                    billdetails_csvfile_data = csv.reader(billdetailscsvfile)
                    header = []
                    header = next(billdetails_csvfile_data)
                    billdetails_insert_query = "insert into bill_details(bill_id,product_id,product_name,quantity,total_price) values(%s,%s,%s,%s,%s)"
                    for row in billdetails_csvfile_data:
                        bill_id = int(row[0])
                        product_id = int(row[1])
                        product_name = row[2]
                        quantity = int(row[3])
                        total_price = float(row[4])
                        record = (bill_id,product_id,product_name,quantity,total_price)
                        cursor.execute(billdetails_insert_query,record)
                connection.commit()
                print("Data inserted in to billdetail table")
            else:
                print("Path does not exist")
            cursor.close()
            connection.close()
            print("\n MySQL connection is closed")    
                
                
    def create_billcsvfile(self,bill):
        bill_csv_columns = ['bill_id','bill_date','store_id','bill_total']
        bill_csvfile = "C:\\Users\\dkc91\\OneDrive\\Desktop\\Python_classes\\My_Python_Code\\BillingSystem\\Bill.csv"
        file_exists = os.path.isfile(bill_csvfile)
        with open(bill_csvfile, 'a',newline="") as billcsvfile:
            writer = csv.DictWriter(billcsvfile, fieldnames = bill_csv_columns)
            if not file_exists:
                writer.writeheader()
            for data in bill:
                writer.writerow(data)
                        
                        
    def create_billdetailscsvfile(self,billdetails):
        billdetails_csv_columns = ['bill_id','product_id','product_name','quantity','total_price']
        billdetails_csvfile = "C:\\Users\\dkc91\\OneDrive\\Desktop\\Python_classes\\My_Python_Code\\BillingSystem\\BillDetails.csv"
        file_exists = os.path.isfile(billdetails_csvfile)
        with open(billdetails_csvfile, 'a',newline="") as billdetailscsvfile:
            writer = csv.DictWriter(billdetailscsvfile, fieldnames=billdetails_csv_columns)
            if not file_exists:
                writer.writeheader()
            for data in billdetails:
                writer.writerow(data)
                
                
    def move_to_processedfolder(self,list_bill_json_files):
        processedbills_folder = 'C:\\Users\\dkc91\\OneDrive\\Desktop\\Python_classes\\My_Python_Code\\BillingSystem\\ProcessedBills'
        for bill_json_file in list_bill_json_files:
            shutil.move(bill_json_file, processedbills_folder)
            print(f'{bill_json_file} file is successfuly moved to processedbills folder')
        
        
    def process_bill_json(self):
        list_bill_json_files = self.read_bill_json_files()
        for bill_json_file in list_bill_json_files:
            # print(bill_json_file)
            with open(bill_json_file) as billfile:
                billdata = json.load(billfile)
                # print(billdata)
                bill = [{'bill_id':billdata['bill_id'],
                        'bill_date':billdata['bill_date'],
                        'store_id':billdata['store_id'],
                        'bill_total':billdata['bill_total']}]
                # print(f'\n\n bill = {bill}')
                self.create_billcsvfile(bill)
                bill_details = []
                for data in billdata['bill_details']:
                    bill_details.append({'bill_id':billdata['bill_id']
                                ,'product_id':data['product_id']
                                ,'product_name':data['product_name']
                                ,'quantity':data['quantity']
                                ,'total_price':data['total_price']
                                })
                # print(f'\n billdetail = {bill_details}')
                self.create_billdetailscsvfile(bill_details)
        self.move_to_processedfolder(list_bill_json_files)
        # self.insert_into_database(bill_csvfile,billdetails_csvfile)
        
if __name__=='__main__': 
    bill_json_files_path = 'C:\\Users\\dkc91\\OneDrive\\Desktop\\Python_classes\\My_Python_Code\\BillingSystem\\Bills\\*.json'        
    billobj = ProcessBills(bill_json_files_path)
    billobj.process_bill_json()
