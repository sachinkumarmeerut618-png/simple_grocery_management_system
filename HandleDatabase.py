import sqlite3

class HandleDB:
    
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
        self.create_customerTable()
        self.create_productTable()
        self.create_purchaseTable()
        self.create_salesTable()
        self.create_supplierTable()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                mobileno TEXT
            )
        """)
        self.conn.commit()

    def create_productTable(self):
        self.cursor.execute("""        
            CREATE TABLE IF NOT EXISTS product(
                pid INTEGER PRIMARY KEY AUTOINCREMENT,
                productname TEXT UNIQUE,
                unit NUMBER,
                Tax_rate NUMBER            
            )                           
        """)
        self.conn.commit()

    def create_customerTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer(
                cid INTEGER PRIMARY KEY AUTOINCREMENT,
                customername TEXT  UNIQUE,
                mobileno TEXT,
                address TEXT,
                paymenttype TEXT,
                paymentdetails TEXT
            )
        """)
        self.conn.commit()

    def create_supplierTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS supplier(
                sid INTEGER PRIMARY KEY AUTOINCREMENT,
                suppliername TEXT UNIQUE,
                mobileno TEXT,
                address TEXT,
                paymenttype TEXT,
                paymentdetails TEXT
                )            
                
        """) 
        self.conn.commit()     

    def create_purchaseTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS purchase(
                pid INTEGER PRIMARY KEY AUTOINCREMENT,
                suppliername TEXT UNIQUE,
                supplierbillno TEXT,
                product_name TEXT,
                quantity  TEXT,
                rate NUMBER,
                amount NUMBER
                )
        """)
        self.conn.commit()

    def create_salesTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sale(
                sid INTEGER PRIMARY KEY AUTOINCREMENT,
                customername TEXT UNIQUE,
                customerbillno TEXT,
                product_name TEXT,
                quantity  TEXT,
                rate NUMBER,
                amount NUMBER
                )
        """)
        self.conn.commit()                                          

    def insertUser(self, username, password, mobileno):
        try:
            self.cursor.execute("INSERT INTO users (username, password, mobileno) VALUES (?, ?, ?)",
                                (username, password, mobileno))
            self.conn.commit()
            return "User registered successfully"
        except sqlite3.IntegrityError:
            return "Username already exists"
        except Exception as e:
            return f"Error: {e}"
    
    def showdata(self, username, password):
        try:
            row = "select count(*) from users where username = ? and password = ?"
            self.cursor.execute(row, (username, password)) 
            data = self.cursor.fetchone() 
            return data[0] if data else 0
        except Exception as e:
            print(f"Error: {e}")
            return 0

    def updatePassword(self, username, password, mobileno):
        try:
            update_pass = "update users set password = ? where username = ? and mobileno = ?"   
            self.cursor.execute(update_pass, (password, username, mobileno)) 
            self.conn.commit()
            return "Password updated successfully"
        except Exception as e:
            return f"Error: {e}"

    def insertpurchase(self, sn, sbn, pro, qua, tr, amm):    
        try:
            self.cursor.execute("INSERT INTO purchase( suppliername, supplierbillno, product_name,  quantity, rate, amount) VALUES( ?, ?, ?, ?, ?, ?)",
                                (sn, sbn, pro, qua, tr, amm))
            self.conn.commit()
            return "Purchase saved successfully"
        except Exception as e:
            return f"Error: {e}"
        
    def insertsale(self, sn, sbn, pro, qua, tr, amm):
        try:
            self.cursor.execute("INSERT INTO sale( customername, customerbillno, product_name, quantity, rate, amount) VALUES(?, ?, ?, ?, ?, ?)",
                                (sn, sbn, pro, qua, tr, amm))
            self.conn.commit()
            return "Sale saved successfully"
        except Exception as e:
            return f"Error: {e}"
        
    def insertcustomer(self, cn, mn, add, pt, pd):
        try:
            self.cursor.execute("INSERT INTO customer(customername, mobileno, address, paymenttype, paymentdetails) VALUES(?, ?, ?, ?, ?)",
                                (cn, mn, add, pt, pd))
            self.conn.commit()
            return "Customer saved successfully"
        except Exception as e:
            return f"Error: {e}"
        
    def insertsupplier(self, sn, mn, add, pt, pd):
        try:
            self.cursor.execute("INSERT INTO supplier(suppliername, mobileno, address, paymenttype, paymentdetails) VALUES(?, ?, ?, ?, ?)",
                                (sn, mn, add, pt, pd))
            self.conn.commit()
            return "Supplier saved successfully"
        except Exception as e:
            return f"Error: {e}"
        
    def insertproduct(self, pn, unit, tax):
        try:
            self.cursor.execute("INSERT INTO product( productname, unit, Tax_rate) VALUES( ?, ?, ?)",
                             (pn, unit, tax))
            self.conn.commit()
            return "Product saved successfully"
        except Exception as e:
            return f"Error: {e}"

    def showproduct(self):
        try:
            self.cursor.execute("SELECT * FROM product")
            result = self.cursor.fetchall()
            return list(result)
        except Exception as e:
            print(f"Error: {e}")
            return []

    def showcustomer(self):
        try:
            self.cursor.execute("SELECT * FROM customer")
            result = self.cursor.fetchall()
            return list(result)
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def showsupplier(self):
        try:
            self.cursor.execute("SELECT * FROM supplier")
            result = self.cursor.fetchall()
            return list(result)
        except Exception as e:
            print(f"Error: {e}")
            return []

    def showpurchase(self):
        try:
            self.cursor.execute("SELECT * FROM purchase")
            result = self.cursor.fetchall()
            return list(result)
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def showsale(self):
        try:
            self.cursor.execute("SELECT * FROM sale")
            result = self.cursor.fetchall()
            return list(result)
        except Exception as e:
            print(f"Error: {e}")
            return []

    def getAllsuppliers(self):
        try:
            self.cursor.execute("SELECT suppliername FROM supplier")   
            result = self.cursor.fetchall()
            result = list(map(lambda name: name[0], result))
            result.insert(0, '<SELECT SUPPLIERS>')
            return result
        except Exception as e:
            print(f"Error: {e}")
            return ['<SELECT SUPPLIERS>']

    def getAllproducts(self):
        try:
            self.cursor.execute("select productname FROM product")   
            result = self.cursor.fetchall()
            result = list(map(lambda name: name[0], result))
            result.insert(0, '<SELECT PRODUCTS>')
            return result
        except Exception as e:
            print(f"Error: {e}")
            return ['<SELECT PRODUCTS>']

    def getAllcustomers(self):
        try:
            self.cursor.execute("SELECT customername FROM customer")   
            result = self.cursor.fetchall()
            result = list(map(lambda name: name[0], result))
            result.insert(0, '<SELECT CUSTOMERS>')
            return result
        except Exception as e:
            print(f"Error: {e}")
            return ['<SELECT CUSTOMERS>']
 
    def getStockInHand(self):
        try:
            self.cursor.execute("SELECT p.product_name, SUM(p.quantity) AS total_purchase, IFNULL(s.total_sale,0) AS total_sale, SUM(p.quantity)-IFNULL(s.total_sale,0) AS closing_stock From purchase p LEFT JOIN (SELECT product_name, SUM(quantity) AS total_sale FROM sale GROUP BY product_name) s ON p.product_name=s.product_name GROUP BY p.product_name")
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def getproductID(self):
        try:
            self.cursor.execute("select pid, productname from product")
            result = self.cursor.fetchall()
            result = list(map(lambda d: str(d[0]) + "-" + d[1], result))
            return result
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def getoneprduct(self, pid):
        try:
            self.cursor.execute("select * from product where pid = ?", (pid,))
            result = self.cursor.fetchall()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def getsupplierID(self):
        try:
            self.cursor.execute("select sid, suppliername from supplier")
            result = self.cursor.fetchall()
            result = list(map(lambda d: str(d[0]) + "-" + d[1], result))
            return result
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def getonesupplier(self, sid):
        try:
            self.cursor.execute("select * from supplier where sid = ?", (sid,))
            result = self.cursor.fetchall()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def getcustomerID(self):
        try:
            self.cursor.execute("select cid, customername from customer")
            result = self.cursor.fetchall()
            result = list(map(lambda d: str(d[0]) + "-" + d[1], result))
            return result
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def getonecustomer(self, cid):
        try:
            self.cursor.execute("select * from customer where cid = ?", (cid,))
            result = self.cursor.fetchall()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def getpurchaseID(self):
        try:
            self.cursor.execute("select pid, suppliername from purchase")
            result = self.cursor.fetchall()
            result = list(map(lambda d: str(d[0]) + "-" + d[1], result))
            return result
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def getonepurchase(self, pid):
        try:
            self.cursor.execute("select * from purchase where pid = ?", (pid,))
            result = self.cursor.fetchall()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def getsaleID(self):
        try:
            self.cursor.execute("select sid, customername from sale")
            result = self.cursor.fetchall()
            result = list(map(lambda d: str(d[0]) + "-" + d[1], result))
            return result
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def getonesale(self, sid):
        try:
            self.cursor.execute("select * from sale where sid = ?", (sid,))
            result = self.cursor.fetchall()
            return result[0] if result else None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def updateProductInDB(self, pid, pn, un, tx):
        try:
            self.cursor.execute("update product set productname = ?, unit = ?, Tax_rate = ? where pid = ?", (pn, un, tx, pid))
            self.conn.commit()
            print("update successfully")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def updateSupplierInDB(self, sid, sn, mb, add, pt, pd):
        try:
            self.cursor.execute("update supplier set suppliername = ?, mobileno = ?, address = ?, paymenttype = ?, paymentdetails = ? where sid = ?", (sn, mb, add, pt, pd, sid))
            self.conn.commit()
            print("update successfully")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def updateCustomerInDB(self, cid, cn, mb, add, pt, pd):
        try:
            self.cursor.execute("update customer set customername = ?, mobileno = ?, address = ?, paymenttype = ?, paymentdetails = ? where cid = ?", (cn, mb, add, pt, pd, cid))
            self.conn.commit()
            print("update successfully")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def updatePurchaseInDB(self, pid, sn, sbn, pro, qua, tr, amm):
        try:
            self.cursor.execute("update purchase set suppliername = ?, supplierbillno = ?, product_name =  ?, quantity = ?, rate = ?, amount = ? where pid = ?", (sn, sbn, pro, qua, tr, amm, pid))       
            self.conn.commit()
            print("update successfully")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def updateSaleInDB(self, sid, cn, cbn, pro, qua, tr, amm):
        try:
            self.cursor.execute("update sale set customername = ?, customerbillno = ?, product_name = ?, quantity = ?, rate = ?, amount = ? where sid = ?", (cn, cbn, pro, qua, tr, amm, sid))
            self.conn.commit()
            print("update successfully")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

if __name__ == '__main__':
    obj = HandleDB()
    stock = obj.getStockInHand()
    print(stock)