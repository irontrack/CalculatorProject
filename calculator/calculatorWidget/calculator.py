from PyQt4 import QtCore, QtGui
from cal_eval import c_eval

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(791, 538)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))        
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_14 = QtGui.QPushButton(Dialog)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_14.clicked.connect(self.btn_p_open_pushed)
        self.verticalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_17 = QtGui.QPushButton(Dialog)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_17.clicked.connect(self.btn_p_closed_pushed)
        self.verticalLayout_3.addWidget(self.pushButton_17)
        self.dot_btn = QtGui.QPushButton(Dialog)
        self.dot_btn.setObjectName(_fromUtf8("dot_btn"))
        self.dot_btn.clicked.connect(self.btn_dot_pushed)
        self.verticalLayout_3.addWidget(self.dot_btn) 
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.seven_btn = QtGui.QPushButton(Dialog)
        self.seven_btn.setObjectName(_fromUtf8("seven_btn"))
        self.seven_btn.clicked.connect(self.btn_7_pushed)
        self.horizontalLayout_4.addWidget(self.seven_btn)
        self.eight_btn = QtGui.QPushButton(Dialog)
        self.eight_btn.setObjectName(_fromUtf8("eight_btn"))
        self.eight_btn.clicked.connect(self.btn_8_pushed)
        self.horizontalLayout_4.addWidget(self.eight_btn)
        self.nine_btn = QtGui.QPushButton(Dialog)
        self.nine_btn.setObjectName(_fromUtf8("nine_btn"))
        self.nine_btn.clicked.connect(self.btn_9_pushed)
        self.horizontalLayout_4.addWidget(self.nine_btn)
        self.CE_btn = QtGui.QPushButton(Dialog)
        self.CE_btn.setObjectName(_fromUtf8("CE_btn"))
        self.CE_btn.clicked.connect(self.btn_CE_pushed)
        self.horizontalLayout_4.addWidget(self.CE_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.four_btn = QtGui.QPushButton(Dialog)
        self.four_btn.setObjectName(_fromUtf8("four_btn"))
        self.four_btn.clicked.connect(self.btn_4_pushed)
        self.horizontalLayout.addWidget(self.four_btn)
        self.five_btn = QtGui.QPushButton(Dialog)
        self.five_btn.setObjectName(_fromUtf8("five_btn"))
        self.five_btn.clicked.connect(self.btn_5_pushed)
        self.horizontalLayout.addWidget(self.five_btn)
        self.six_btn = QtGui.QPushButton(Dialog)
        self.six_btn.setObjectName(_fromUtf8("six_btn"))
        self.six_btn.clicked.connect(self.btn_6_pushed)
        self.horizontalLayout.addWidget(self.six_btn)
        self.div_btn = QtGui.QPushButton(Dialog)
        self.div_btn.setObjectName(_fromUtf8("div_btn"))
        self.div_btn.clicked.connect(self.btn_div_pushed)
        self.horizontalLayout.addWidget(self.div_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.one_btn = QtGui.QPushButton(Dialog)
        self.one_btn.setObjectName(_fromUtf8("one_btn"))
        self.one_btn.clicked.connect(self.btn_1_pushed)
        self.horizontalLayout_2.addWidget(self.one_btn)
        self.two_btn = QtGui.QPushButton(Dialog)
        self.two_btn.setObjectName(_fromUtf8("two_btn"))
        self.two_btn.clicked.connect(self.btn_2_pushed)
        self.horizontalLayout_2.addWidget(self.two_btn)
        self.three_btn = QtGui.QPushButton(Dialog)
        self.three_btn.setObjectName(_fromUtf8("three_btn"))
        self.three_btn.clicked.connect(self.btn_3_pushed)
        self.horizontalLayout_2.addWidget(self.three_btn)
        self.star_btn = QtGui.QPushButton(Dialog)
        self.star_btn.setObjectName(_fromUtf8("star_btn"))
        self.star_btn.clicked.connect(self.btn_star_pushed)
        self.horizontalLayout_2.addWidget(self.star_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zero_btn = QtGui.QPushButton(Dialog)
        self.zero_btn.setObjectName(_fromUtf8("zero_button"))
        self.eql_btn = QtGui.QPushButton(Dialog)
        self.eql_btn.setObjectName(_fromUtf8("eql_btn"))
        self.zero_btn.clicked.connect(self.btn_0_pushed)
        self.horizontalLayout_3.addWidget(self.eql_btn)
        self.eql_btn.clicked.connect(self.btn_eql_pushed)
        self.horizontalLayout_3.addWidget(self.zero_btn)
        self.plus_btn = QtGui.QPushButton(Dialog)
        self.plus_btn.setObjectName(_fromUtf8("plus_btn"))
        self.plus_btn.clicked.connect(self.btn_plus_pushed)
        self.horizontalLayout_3.addWidget(self.plus_btn)
        self.sub_btn = QtGui.QPushButton(Dialog)
        self.sub_btn.setObjectName(_fromUtf8("sub_btn"))
        self.sub_btn.clicked.connect(self.btn_sub_pushed)
        self.horizontalLayout_3.addWidget(self.sub_btn)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.expression = ''
    def btn_p_open_pushed(self):
        self.expression += '('
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_p_closed_pushed(self):
        self.expression += ')'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_dot_pushed(self):
        self.expression += '.'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_7_pushed(self):
        self.expression += '7'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_8_pushed(self):
        self.expression += '8'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_9_pushed(self):
        self.expression += '9'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_CE_pushed(self):
        self.expression = ''
        self.plainTextEdit.clear()
    def btn_4_pushed(self):
        self.expression += '4'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_5_pushed(self):
        self.expression += '5'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_6_pushed(self):
        self.expression += '6'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_div_pushed(self):
        self.expression += '/'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_1_pushed(self):
        self.expression += '1'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_2_pushed(self):
        self.expression += '2'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_3_pushed(self):
        self.expression += '3'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_0_pushed(self):
        self.expression += '0'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_star_pushed(self):
        self.expression += '*'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)   
    def btn_eql_pushed(self):
        self.plainTextEdit.clear()
        a = str(c_eval(self.expression))
        self.plainTextEdit.appendPlainText(a)
        self.expression = ''
        
    def btn_plus_pushed(self):
        self.expression += '+'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
    def btn_sub_pushed(self):
        self.expression += '-'
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.expression)
             
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton_14.setText(_translate("Dialog", "(", None))
        self.pushButton_17.setText(_translate("Dialog", ")", None))
        self.dot_btn.setText(_translate("Dialog", ".", None))
        self.seven_btn.setText(_translate("Dialog", "7", None))
        self.eight_btn.setText(_translate("Dialog", "8", None))
        self.nine_btn.setText(_translate("Dialog", "9", None))
        self.CE_btn.setText(_translate("Dialog", "CE", None))
        self.four_btn.setText(_translate("Dialog", "4", None))
        self.five_btn.setText(_translate("Dialog", "5", None))
        self.six_btn.setText(_translate("Dialog", "6", None))
        self.div_btn.setText(_translate("Dialog", "/", None))
        self.one_btn.setText(_translate("Dialog", "1", None))
        self.two_btn.setText(_translate("Dialog", "2", None))
        self.three_btn.setText(_translate("Dialog", "3", None))
        self.star_btn.setText(_translate("Dialog", "*", None))
        self.eql_btn.setText(_translate("Dialog", "=", None))
        self.plus_btn.setText(_translate("Dialog", "+", None))
        self.sub_btn.setText(_translate("Dialog", "-", None))
        self.zero_btn.setText(_translate("Dialog", "0", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())