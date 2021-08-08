import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
import NewWindow  # Это наш конвертированный файл дизайна
import DialogWL2
import AddNewWL
import OpenWLDesc
print(os.getcwd())
NewFolder = os.getcwd()


def UpdateWL(Array):
    os.chdir(NewFolder)
    os.chdir('..')
    WFile2 = open('WL.csv', 'w')
    WLwriter2 = csv.writer(WFile2, delimiter = ",", lineterminator="\n")
    WLwriter2.writerow(Array)
    WFile2.close()
def LoadWL():
    os.chdir(NewFolder)
    os.chdir('..')
    print(os.getcwd())
    f = open('WL.csv', 'r')
    WLN = []
    for line in f:
        Plate = ''
        for pl in line:
            if pl != ',':
                Plate += pl
            elif pl == ',':
                WLN.append(Plate)
                Plate = ''
        print(Plate, 'PLATE')
        Max = 0
        for i in Plate:
            
            Max +=1
        Max -= 1
        print(Max, "MAX")
        WLN.append(Plate[0:Max])   
    
    f.close()
    return WLN
        
class ExampleApp(QtWidgets.QMainWindow, NewWindow.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.showFullScreen()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.WhiteListButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки

    def browse_folder(self):
        # = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        
        window2 = ExampleApp2()  # Создаём объект класса ExampleApp
       
        window2.exec_()
        
        
class ExampleApp2(QDialog, DialogWL2.Ui_Dialog):
    NCurrentRow = 1
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.listWidget.clear()

        WL = []
        WL = LoadWL()
        for t in WL:
            Space = 0
            Plate = ''
            for y in t:
                if Space < 3 and y != '_':
                    Plate += y
                elif y == '_' and Space < 3:
                    Plate += ' '
                    Space += 1
                elif Space == 3:
                    self.listWidget.addItem(Plate)
                    break
        self.DelNumberWL.clicked.connect(self.delete)
        self.AddNumberWL.clicked.connect(self.add_WLnumber)
        self.AddNumberWL_2.clicked.connect(self.load)
        
        self.listWidget.itemDoubleClicked.connect(self.open_desc) 
        
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
         # Это нужно для инициализации нашего дизайна
    def delete(self):
        if self.listWidget.currentRow() > -1:
            
            os.chdir(NewFolder)
            os.chdir('..')
            
            
        
            WL2 = []
            WL2 = LoadWL()
           
            os.chdir(NewFolder)
            
            Row = self.listWidget.currentRow()
            self.listWidget.takeItem(Row)
            print(Row)
            WL2.pop(Row)
            print(WL2)
            
            UpdateWL(WL2)
        
    def load(self):
        
        
        self.listWidget.clear()
        
        
        WL = []
        WL = LoadWL()
        for t in WL:
            Space = 0
            Plate = ''
            for y in t:
                if Space < 3 and y != '_':
                    Plate += y
                elif y == '_' and Space < 3:
                    Plate += ' '
                    Space += 1
                elif Space == 3:
                    self.listWidget.addItem(Plate)
                    break

    def open_desc(self):
        ExampleApp2.NCurrentRow = self.listWidget.currentRow()
        window4 = ExampleApp4()  # Создаём объект класса ExampleApp
        
        window4.exec_()
    def add_WLnumber(self):
        # = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        
        window3 = ExampleApp3()  # Создаём объект класса ExampleApp
       
        window3.exec_()    
        
class ExampleApp3(QDialog, AddNewWL.Ui_AddNewPlate):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.SendNumber.clicked.connect(self.send_WLnumber)
    def send_WLnumber(self):
        # = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
        
        Text = self.lineEdit.text() + '_' + self.FIO.text() + '_' + self.FIO_2.text() + '_' + self.FIO_3.text() + '_' + self.CarDesc.text() + '_' + self.Number.text() + '_' + self.Mail.text()
        
        WL = []
        
        WL = LoadWL()
        print(WL)
        WL.append(Text)
        print(WL)
        UpdateWL(WL)
        self.close()
        # Это здесь нужно для доступа к переменным, методам
        
class ExampleApp4(QDialog, OpenWLDesc.Ui_AddNewPlate):
    def __init__(self):
        CurrentRow = ExampleApp2.NCurrentRow
        print(CurrentRow)
        super().__init__()
        self.setupUi(self) 
        Twl = LoadWL()
        Twl2 = []
        for i, NNum in enumerate(Twl):
            print(i)
            if i == CurrentRow:
                Plate = ''
                
                for n in NNum:
                    if n != '_':
                        Plate += n
                    else:
                        Twl2.append(Plate)
                        Plate = ''
                Twl2.append(Plate)
                break
        print(Twl2)
        for c, h in enumerate(Twl2):
            self.listWidget2.addItem(h) 
        
    
        # Это здесь нужно для доступа к переменным, методам
 
    
        
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
    
