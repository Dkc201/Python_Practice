import pymysql
import os,csv


class ProductData:    
    def loadproduct_in_db(self):
        try:
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='billingsystem')
        except pymysql.err.OperationalError as error:
            print("Unable to make a connection to the mysql database")
        else:
            print("Successfully connected to mysql Database") 
            cursor = connection.cursor()
            product_csvfilepath = "C:/Users/dkc91/OneDrive/Desktop/Python_classes/My_Python_Code/BillingSystem/products.csv"
            if os.path.exists(product_csvfilepath):
                with open(product_csvfilepath) as productfile:
                    product_csv_file = csv.reader(productfile)
                    header = []
                    header = next(product_csv_file)
                    productdata = []
                    product_insert_query = "insert into product(product_id,product_catagory,product_name,unit_price) values(%s,%s,%s,%s)"
                    for row in product_csv_file:
                        product_id = int(row[0])
                        product_catagory = row[1]
                        product_name = row[2]
                        unit_price = float(row[3])
                        record = (product_id,product_catagory,product_name,unit_price)
                        cursor.execute(product_insert_query,record)
                connection.commit()
                print("Data inserted in to product table")
            else:
                print("Path does not exist")
                
            cursor.close()
            connection.close()
            print("\n MySQL connection is closed")
    def product_data(self):
        try:
            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='billingsystem')
        except pymysql.err.OperationalError as error:
            print("Unable to make a connection to the mysql database")
        else:
            print("Successfully connected to mysql Database") 
            cursor = connection.cursor()
            cursor.execute("select product_id,product_catagory,product_name,unit_price from product")
            productdata = []
            for pid,pcat,pname,untp in cursor.fetchall():
                productdata.append({'product_id':pid,
                        'product_catagory':pcat,
                        'product_name':pname,
                        'unit_price':untp}
                        )
            cursor.close()
            connection.close()
            # print("\n MySQL connection is closed")
            return productdata
if __name__=='__main__':
    productdata = ProductData()
    print(productdata.product_data())
