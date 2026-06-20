import sys
from PyQt5 import QtWidgets
import window as ui
import HandleDatabase as db
from PyQt5.QtWidgets import QTableWidgetItem

class Controller:
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.activeEvent()
    
        try:
            self.db = db.HandleDB()
        except Exception as e:
            print("Database error:", e)
        
        self.updatecomboBox()


    def activeEvent(self):
        self.ui.pushButton.clicked.connect(self.performLogin)
        self.ui.pushButton_2.clicked.connect(self.performSignUp)
        self.ui.pushButton_3.clicked.connect(self.showSignUp)
        self.ui.pushButton_4.clicked.connect(self.showlogin)
        self.ui.pushButton_7.clicked.connect(self.showforget)
        self.ui.pushButton_6.clicked.connect(self.showlogin)
        self.ui.pushButton_9.clicked.connect(self.showaddProduct)
        self.ui.pushButton_10.clicked.connect(self.showSuppliers)
        self.ui.pushButton_11.clicked.connect(self.showCustomers)
        self.ui.pushButton_12.clicked.connect(self.showPurchase)
        self.ui.pushButton_13.clicked.connect(self.showSales)
        self.ui.pushButton_8.clicked.connect(self.showhome)
        self.ui.pushButton_16.clicked.connect(self.saveProductTask)
        self.ui.pushButton_17.clicked.connect(self.saveSupplierTask)
        self.ui.pushButton_18.clicked.connect(self.saveCustomerTask)
        self.ui.pushButton_19.clicked.connect(self.savePurcahseTask)
        self.ui.pushButton_20.clicked.connect(self.savesalesTask)
        self.ui.pushButton_15.clicked.connect(self.showlogin)
        self.ui.pushButton_14.clicked.connect(self.showsummary)
        self.ui.pushButton_21.clicked.connect(lambda : self.showTable('daybook'))
        self.ui.pushButton_22.clicked.connect(lambda : self.showTable('product'))
        self.ui.pushButton_23.clicked.connect(lambda : self.showTable('supplier'))
        self.ui.pushButton_24.clicked.connect(lambda : self.showTable('purchase'))
        self.ui.pushButton_25.clicked.connect(lambda : self.showTable('sales'))
        self.ui.pushButton_26.clicked.connect(lambda : self.showTable('stock'))
        self.ui.pushButton_37.clicked.connect(self.showalter)
        self.ui.pushButton_27.clicked.connect(self.showproduct)
        self.ui.pushButton_28.clicked.connect(self.showsupplier)
        self.ui.pushButton_29.clicked.connect(self.showcustomer)
        self.ui.pushButton_30.clicked.connect(self.showpurchase)
        self.ui.pushButton_31.clicked.connect(self.showsale)
        self.ui.comboBox_5.currentTextChanged.connect(self.showProductDetails)
        self.ui.comboBox_6.currentTextChanged.connect(self.showsupplierDetails)
        self.ui.comboBox_7.currentTextChanged.connect(self.showCustomerDetails)
        self.ui.comboBox_8.currentTextChanged.connect(self.showPurchaseDetails)
        self.ui.comboBox_11.currentTextChanged.connect(self.showSaleDetails)
        self.ui.pushButton_38.clicked.connect(self.updateProduct)
        self.ui.pushButton_39.clicked.connect(self.updateSupplier)
        self.ui.pushButton_40.clicked.connect(self.updateCustomer)
        self.ui.pushButton_41.clicked.connect(self.updatePurchase)
        self.ui.pushButton_42.clicked.connect(self.updateSale)


    def showSignUp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def showlogin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stackedWidgetPage1)

    def showforget(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def performSignUp(self):
        username = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        cpassword = self.ui.lineEdit_5.text()
        mobileno = self.ui.lineEdit_6.text()
        if password == cpassword:
            status = self.db.insertUser(username, password, mobileno)
            print(status)
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
        else:
            print('Password and confirm password does not match')

    def performLogin(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text() 
        data = self.db.showdata(username, password)  
        print(data)
        if data >= 1:
            self.ui.stackedWidget_11.setCurrentWidget(self.ui.page_3)
        else:
            print('Invalid username or password')

    def showaddProduct(self):
        self.ui.stackedWidget_14.setCurrentWidget(self.ui.page_4)

    def showSuppliers(self):
        self.ui.stackedWidget_14.setCurrentWidget(self.ui.page_5)    

    def showCustomers(self):
        self.ui.stackedWidget_14.setCurrentWidget(self.ui.page_6)    

    def showPurchase(self):
        self.ui.stackedWidget_14.setCurrentWidget(self.ui.page_7) 

    def showSales(self):            
        self.ui.stackedWidget_14.setCurrentWidget(self.ui.page_8)

    def showhome(self):
        self.ui.stackedWidget_14.setCurrentIndex(0)

    def showlogin(self):
        self.ui.stackedWidget_11.setCurrentWidget(self.ui.stackedWidget_11Page1)    
   
    def updatecomboBox(self):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.db.getAllsuppliers())
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItems(self.db.getAllcustomers())
        self.ui.comboBox_4.clear()
        self.ui.comboBox_4.addItems(self.db.getAllproducts())
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(self.db.getAllproducts())
        self.ui.comboBox_5.clear()
        self.ui.comboBox_5.addItems(self.db.getproductID())
        self.ui.comboBox_6.clear()
        self.ui.comboBox_6.addItems(self.db.getsupplierID())
        self.ui.comboBox_7.clear()
        self.ui.comboBox_7.addItems(self.db.getcustomerID())
        self.ui.comboBox_8.clear()
        self.ui.comboBox_8.addItems(self.db.getpurchaseID())
        self.ui.comboBox_11.clear()
        self.ui.comboBox_11.addItems(self.db.getsaleID())
        

    def showsummary(self):
        self.ui.stackedWidget_14.setCurrentWidget(self.ui.page_9)

    def showalter(self):
        self.ui.stackedWidget_14.setCurrentWidget(self.ui.page_10)
    
    def showproduct(self):
        self.ui.stackedWidget_54.setCurrentWidget(self.ui.stackedWidget_54Page1)

    def showsupplier(self):
        self.ui.stackedWidget_54.setCurrentWidget(self.ui.page_11)

    def showcustomer(self):
        self.ui.stackedWidget_54.setCurrentWidget(self.ui.page_12)

    def showpurchase(self):
        self.ui.stackedWidget_54.setCurrentWidget(self.ui.page_13)

    def showsale(self):
        self.ui.stackedWidget_54.setCurrentWidget(self.ui.page_14)


    def saveProductTask(self):
        pn = self.ui.lineEdit_11.text()
        unit = self.ui.lineEdit_12.text()
        tax = self.ui.lineEdit_13.text()
        print(pn, unit, tax)
        msg = self.db.insertproduct(pn, unit, tax)
        print(msg)
        self.db.showproduct()
        
    def saveSupplierTask(self):
        sn = self.ui.lineEdit_14.text()
        mn = self.ui.lineEdit_15.text()
        add = self.ui.lineEdit_16.text()
        pt = self.ui.lineEdit_24.text()
        pd = self.ui.textEdit.toPlainText()
        print(sn, mn, add, pt, pd)
        msg = self.db.insertsupplier(sn, mn, add, pt, pd)
        print(msg)
        self.db.showsupplier()

    def saveCustomerTask(self):
        cn = self.ui.lineEdit_18.text()
        mn = self.ui.lineEdit_25.text()
        add = self.ui.lineEdit_26.text()
        pt = self.ui.lineEdit_27.text()
        pd = self.ui.textEdit_2.toPlainText()
        print(cn, mn, add, pt, pd)
        msg = self.db.insertcustomer(cn, mn, add, pt, pd)
        print(msg)
        self.db.showcustomer()

    def savePurcahseTask(self):
        sn = self.ui.comboBox_3.currentText()
        sbn = self.ui.lineEdit_33.text()
        pro = self.ui.comboBox_4.currentText()
        qua = self.ui.lineEdit_31.text()
        tr = self.ui.lineEdit_32.text()
        amm = self.ui.lineEdit_34.text()
        print(sn, sbn, pro, qua, tr, amm)
        msg = self.db.insertpurchase(sn, sbn, pro, qua, tr, amm)
        print(msg)
        self.db.showpurchase()

    def savesalesTask(self):
        sn = self.ui.comboBox.currentText()
        sbn = self.ui.lineEdit_38.text()
        pro = self.ui.comboBox_2.currentText()
        qua = self.ui.lineEdit_40.text()
        tr = self.ui.lineEdit_41.text()
        amm = self.ui.lineEdit_35.text()
        print(sn, sbn, pro, tr, amm, qua)
        msg = self.db.insertsale(sn, sbn, pro, qua, tr, amm)
        print(msg)
        self.db.showsale()
    
    def showTable(self, label):
        print(label)
        data = []
        if label == 'product':
            data = self.db.showproduct() 
            self.ui.tableWidget.setHorizontalHeaderLabels(['ProductID','Name', 'Product', 'Unit', 'Tax'])
        elif label == 'supplier':
            data = self.db.showsupplier()
            self.ui.tableWidget.setHorizontalHeaderLabels(['SupplierID','Supplier','Mobile no.', 'Address', 'Payment type', 'Payment detail'])
        elif label == 'purchase':
            data = self.db.showpurchase()
            self.ui.tableWidget.setHorizontalHeaderLabels(['PurchaseID','Supplier', 'Bill no.', 'Product', 'Quantity', 'Tax', 'Amount'])
        elif label == 'sales':
            data = self.db.showsale()
            self.ui.tableWidget.setHorizontalHeaderLabels(['SalesID','Customer', 'Bill no.', 'Product', 'Quantity', 'Tax', 'Amount'])
        elif label == 'stock':
            data = self.db.getStockInHand()
            self.ui.tableWidget.setHorizontalHeaderLabels([ 'Product', 'Quantity', 'Rate'])    
            
        # Error fix: Agar data empty hai to table clear kar do
        if not data:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(0)
            return

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))

        r = 0
        for row in data:
            c = 0
            for d in row:
                self.ui.tableWidget.setItem(r, c, QTableWidgetItem(str(d)))
                c += 1
            r += 1


    def showProductDetails(self):
        text = self.ui.comboBox_5.currentText()
        if not text or "SELECT" in text: return
        pid = text.split("-")[0]
        data = self.db.getoneprduct(pid)
        
        # Error fix: Check if data is not None
        if data:
            self.ui.lineEdit_28.setText(str(data[1]))
            self.ui.lineEdit_29.setText(str(data[2]))
            self.ui.lineEdit_30.setText(str(data[3]))  
        else:
            self.ui.lineEdit_28.clear()
            self.ui.lineEdit_29.clear()
            self.ui.lineEdit_30.clear()

    def showsupplierDetails(self):
        text = self.ui.comboBox_6.currentText()
        if not text or "SELECT" in text: return
        sid = text.split("-")[0]
        data = self.db.getonesupplier(sid)
        
        if data:
            self.ui.lineEdit_36.setText(str(data[1]))
            self.ui.lineEdit_37.setText(str(data[2]))
            self.ui.lineEdit_39.setText(str(data[3]))
            self.ui.lineEdit_42.setText(str(data[4]))
            self.ui.textEdit_3.setText(str(data[5]))
        else:
            self.ui.lineEdit_36.clear()
            self.ui.lineEdit_37.clear()
            self.ui.lineEdit_39.clear()
            self.ui.lineEdit_42.clear()
            self.ui.textEdit_3.clear()

    def showCustomerDetails(self):
        text = self.ui.comboBox_7.currentText()
        if not text or "SELECT" in text: return
        cid = text.split("-")[0]
        data = self.db.getonecustomer(cid)
        
        if data:
            self.ui.lineEdit_43.setText(str(data[1]))
            self.ui.lineEdit_44.setText(str(data[2]))
            self.ui.lineEdit_45.setText(str(data[3]))
            self.ui.lineEdit_46.setText(str(data[4]))
            self.ui.textEdit_4.setText(str(data[5]))
        else:
            self.ui.lineEdit_43.clear()
            self.ui.lineEdit_44.clear()
            self.ui.lineEdit_45.clear()
            self.ui.lineEdit_46.clear()
            self.ui.textEdit_4.clear()
    
    def showPurchaseDetails(self):
        text = self.ui.comboBox_8.currentText()
        if not text or "SELECT" in text: return
        pid = text.split("-")[0]
        data = self.db.getonepurchase(pid)
        
        if data:
            self.ui.lineEdit_55.setText(str(data[1]))
            self.ui.lineEdit_47.setText(str(data[2]))
            self.ui.lineEdit_56.setText(str(data[3]))
            self.ui.lineEdit_48.setText(str(data[4]))
            self.ui.lineEdit_49.setText(str(data[5]))
            self.ui.lineEdit_50.setText(str(data[6]))
        else:
            self.ui.lineEdit_55.clear()
            self.ui.lineEdit_47.clear()
            self.ui.lineEdit_56.clear()
            self.ui.lineEdit_48.clear()
            self.ui.lineEdit_49.clear()
            self.ui.lineEdit_50.clear()

    def showSaleDetails(self):
        text = self.ui.comboBox_11.currentText()
        if not text or "SELECT" in text: return
        sid = text.split("-")[0]
        data = self.db.getonesale(sid)
        
        if data:
            self.ui.lineEdit_57.setText(str(data[1]))
            self.ui.lineEdit_51.setText(str(data[2]))
            self.ui.lineEdit_58.setText(str(data[3]))
            self.ui.lineEdit_52.setText(str(data[4]))
            self.ui.lineEdit_53.setText(str(data[5]))
            self.ui.lineEdit_54.setText(str(data[6]))
        else:
            self.ui.lineEdit_57.clear()
            self.ui.lineEdit_51.clear()
            self.ui.lineEdit_58.clear()
            self.ui.lineEdit_52.clear()
            self.ui.lineEdit_53.clear()
            self.ui.lineEdit_54.clear()

    def updateProduct(self):
        pn = self.ui.lineEdit_28.text()
        un = self.ui.lineEdit_29.text()
        tx = self.ui.lineEdit_30.text()
        text = self.ui.comboBox_5.currentText()
        if not text or "SELECT" in text: return
        pid = text.split("-")[0]
        status = self.db.updateProductInDB(pid, pn, un, tx)

    def updateSupplier(self):
        sn = self.ui.lineEdit_36.text()
        mb = self.ui.lineEdit_37.text()
        add = self.ui.lineEdit_39.text()
        pt = self.ui.lineEdit_42.text()
        pd = self.ui.textEdit_3.toPlainText()
        text = self.ui.comboBox_6.currentText()
        if not text or "SELECT" in text: return
        sid = text.split("-")[0]
        status = self.db.updateSupplierInDB(sid, sn, mb, add, pt, pd)

    def updateCustomer(self):
        cn = self.ui.lineEdit_43.text()
        mb = self.ui.lineEdit_44.text()
        add = self.ui.lineEdit_45.text()
        pt = self.ui.lineEdit_46.text()
        pd = self.ui.textEdit_4.toPlainText()
        text = self.ui.comboBox_7.currentText()
        if not text or "SELECT" in text: return
        cid = text.split("-")[0]
        status = self.db.updateCustomerInDB(cid, cn, mb, add,  pt, pd)

    def updatePurchase(self):
        sn = self.ui.lineEdit_55.text()
        sbn = self.ui.lineEdit_47.text()
        pro = self.ui.lineEdit_56.text()
        qua = self.ui.lineEdit_48.text()
        tr = self.ui.lineEdit_49.text()
        amm = self.ui.lineEdit_50.text()
        text = self.ui.comboBox_8.currentText()
        if not text or "SELECT" in text: return
        pid = text.split("-")[0]
        status = self.db.updatePurchaseInDB(pid, sn, sbn, pro, qua, tr, amm)
        
    def updateSale(self):
        cn = self.ui.lineEdit_57.text()
        cbn = self.ui.lineEdit_51.text()
        pro = self.ui.lineEdit_58.text()
        qua = self.ui.lineEdit_53.text()
        tr = self.ui.lineEdit_52.text()
        amm = self.ui.lineEdit_54.text()
        text = self.ui.comboBox_11.currentText()
        if not text or "SELECT" in text: return
        sid = text.split("-")[0]
        status = self.db.updateSaleInDB(sid, cn, cbn, pro, qua, tr, amm)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())
    