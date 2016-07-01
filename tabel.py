from PyQt4 import QtGui,QtCore
import tabel_ui
import sys
import xlrd
from xlrd import *

class Main(QtGui.QDialog,tabel_ui.Ui_Dialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.bersih()
		self.progressBar.setValue(0)
		self.tableWidget.setColumnCount(0)
		self.tableWidget.setRowCount(0)
		self.pushButton.pressed.connect(self.isiDataTable)

	def bersih(self):
		self.tableWidget.clear()

	def isiDataTable(self):
		book=xlrd.open_workbook("allitem2.xlsx")
		sh = book.sheet_by_name('Sheet1')
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setRowCount(sh.nrows)

		for i in range(101): # menghitung sampai 100
			a=((sh.nrows/100)*i)
			b=(sh.nrows/100)*(i+1)
			
			for x in range(a,b): # membagi jumlah baris menjadi seperseratus

				if x < int(sh.nrows): # melakukan pengecekan supaya tidak error 
										# saat perhitungan melebihi jumlah total baris
					teks = (
					str(sh.row_values(x)[0]),
					str(sh.row_values(x)[1]),
					str(sh.row_values(x)[2]),
					str(sh.row_values(x)[3]),
					str(sh.row_values(x)[4]),
					str(sh.row_values(x)[5]),
					str(sh.row_values(x)[6]))

					for e in range(0,6): # mengisi data masing - masing kolom tiap baris
						b=str(e)
						item = QtGui.QTableWidgetItem()
						item.setFlags(
							QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
						exec "item.setToolTip(teks["+b+"])"
						exec "item.setText(teks[" + b + "])"
						exec "self.tableWidget.setItem(x," + b + ",item)"
					self.progressBar.setValue(i)

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	form = Main()
	form.show()
	sys.exit(app.exec_())