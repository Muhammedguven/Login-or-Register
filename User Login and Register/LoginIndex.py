from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from Login import Ui_LoginWindow
import  re
class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.loginBtn.clicked.connect(self.Log)
        self.ui.RegBtn.clicked.connect(self.Reg)
    
    def Reg(self):
        file = open("Users.txt","a",encoding = 'utf-8')
        msg2 = QMessageBox()
        if self.ui.passwordTxt.text() != self.ui.password2Txt.text():
            msg2.setWindowTitle("Error")
            msg2.setText("Passwords have to be same")
            msg2.setIcon(QMessageBox.Warning)
            msg2.setDefaultButton(QMessageBox.Ok)
            msg2.exec_()
        elif self.ui.nameTxt.text() == "":
             msg2.setWindowTitle('Error')
             msg2.setIcon(QMessageBox.Warning)
             msg2.setText('Please write your name!')
             msg2.exec_()
        elif self.ui.snameTxt.text() == "":
             msg2.setWindowTitle('Error')
             msg2.setIcon(QMessageBox.Warning)
             msg2.setText('Please write your surname!')
             msg2.exec_()
        elif self.ui.userNameTxt.text() == "":
             msg2.setWindowTitle('Error')
             msg2.setIcon(QMessageBox.Warning)
             msg2.setText('Please write your username!')
             msg2.exec_()
        elif self.ui.passwordTxt.text() == "":
             msg2.setWindowTitle('Error')
             msg2.setIcon(QMessageBox.Warning)
             msg2.setText('Please write your password!')
             msg2.exec_()
        elif self.ui.ageTxt.text() == "":
             msg2.setWindowTitle('Error')
             msg2.setIcon(QMessageBox.Warning)
             msg2.setText('Please write your age!')
             msg2.exec_()
        else:  
            file.write(self.ui.nameTxt.text()+"|"+ self.ui.snameTxt.text()+"|"+ self.ui.userNameTxt.text()+"|"+
             self.ui.passwordTxt.text()+"|"+ self.ui.ageTxt.text()+ "\n")
            msg2.setWindowTitle("Registered")
            msg2.setText('Dear, ' + self.ui.userNameTxt.text() +  ' you have successfully registered.' )
            msg2.setIcon(QMessageBox.Information)
            msg2.setDefaultButton(QMessageBox.Ok)
            file.close()
            msg2.exec_()
    
    def Log(self):
        msg = QMessageBox()
        reading = open("Users.txt","r",encoding = 'utf-8')
        data = reading.read()

        for i in range(len(data)):
            uname = re.search(self.ui.userName.text(),data)
        for j in range(len(data)):
            psw = re.search(self.ui.password.text(),data)
            if self.ui.userName.text() == "":
                msg.setWindowTitle('Error')
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Please write your username!')
                
            elif self.ui.password.text() == "":
                msg.setWindowTitle('Error')
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Please write your password')
                

            elif  uname and psw:
                
                msg.setWindowTitle("Logged In")
                msg.setText('Welcome ' + self.ui.userName.text() + '!')
                msg.setIcon(QMessageBox.Information)
                msg.setDefaultButton(QMessageBox.Ok)
                
            else: 
                msg.setWindowTitle('User has not found!')
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Check your username or password.')
        msg.exec_()

def app():
    app=QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
app()