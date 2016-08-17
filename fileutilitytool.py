# gui based file utility tool built using PyQt. 
# the script only works for window os as evident from the format of the absolute path i.e C:\\...


import os, sys, zipfile, shutil
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CzipWindow(QMainWindow):     #displays the window for creating the zip file
 def __init__(self):
  QMainWindow.__init__(self)
  self.setWindowTitle("Create zip")
  self.resize(300,150)
  layout = QVBoxLayout()
  self.filename= QTextEdit()
  self.zipname=QTextEdit()
  self.next=QPushButton("Next")
  layout.addWidget(self.filename)
  layout.addWidget(self.zipname)  
  layout.addWidget(self.next)
  self.widget = QWidget()
  self.widget.setLayout(layout)
  self.setCentralWidget(self.widget)
  self.zipname.setText("enter zip file name with directory path like C:\\zip_name.zip")
  self.filename.setText("enter file name to be added like C:\\file_name.txt")
  self.next.clicked.connect(self.crzip)
  self.next.clicked.connect(self.close)
 def crzip(self):
   var7=self.zipname.toPlainText()
   var8=self.filename.toPlainText()
   nzip=zipfile.ZipFile(var7,'a')
   nzip.write(var8, compress_type=zipfile.ZIP_DEFLATED)
   nzip.close()
   
class EzipWindow(QMainWindow):            # creates the window for extracting zip file
 def __init__(self):
  QMainWindow.__init__(self)
  self.setWindowTitle("Extract zip")
  self.resize(300,150)
  layout = QVBoxLayout()
  self.source= QTextEdit()
  self.dest=QTextEdit()
  self.next=QPushButton("OK")
  layout.addWidget(self.source)
  layout.addWidget(self.dest)  
  layout.addWidget(self.next)
  self.widget = QWidget()
  self.widget.setLayout(layout)
  self.setCentralWidget(self.widget)
  self.source.setText("enter zip file name with directory path")
  self.dest.setText("destination directory")
  self.next.clicked.connect(self.exzip)
  self.next.clicked.connect(self.close)
 def exzip(self):
   var10=self.source.toPlainText()
   var11=self.dest.toPlainText()
   os.chdir(var11)
   exzip=zipfile.ZipFile(var10)
   exzip.extractall()
   exzip.close()  
  
class DeleteWindow(QMainWindow):                     # creates the window for deleting file
 def __init__(self):
  QMainWindow.__init__(self)
  self.setWindowTitle("Delete")
  self.resize(300,150)
  layout = QVBoxLayout()
  self.source = QTextEdit()
  self.subm=QPushButton("ok")
  self.source.setText("enter source directory with file name")
  layout.addWidget(self.source)
  layout.addWidget(self.subm)
  self.widget = QWidget()
  self.widget.setLayout(layout)
  self.setCentralWidget(self.widget)
  self.subm.clicked.connect(self.deletefile)
  self.subm.clicked.connect(self.close)  
 def deletefile(self):
   var6=self.source.toPlainText()
   os.unlink(var6)
   

class MoveWindow(QMainWindow):                       # creates the window for moving file  
 def __init__(self):
  QMainWindow.__init__(self)
  self.setWindowTitle("Move")
  self.resize(300,150)
  layout = QVBoxLayout()
  self.source = QTextEdit()
  self.dest=QTextEdit()
  self.subm=QPushButton("ok")
  self.source.setText("enter source directory with file name")
  self.dest.setText("enter destination directory like C:\\foldername\\...")
  layout.addWidget(self.source)
  layout.addWidget(self.dest)  
  layout.addWidget(self.subm)
  self.widget = QWidget()
  self.widget.setLayout(layout)
  self.setCentralWidget(self.widget)  
  self.subm.clicked.connect(self.movefile)
  self.subm.clicked.connect(self.close)
  
 def movefile(self):
  var4=self.source.toPlainText()
  var5=self.dest.toPlainText()
  shutil.move(var4,var5)  
  
class RenameWindow(QMainWindow):                 # creates the window for renaming file
 def __init__(self):
  QMainWindow.__init__(self)
  self.setWindowTitle("Rename")
  self.resize(300,150)
  layout = QVBoxLayout()
  self.source = QTextEdit()
  self.dest=QTextEdit()
  self.subm=QPushButton("ok")
  self.source.setText("enter directory path with original file name like C:\\apple.txt ")
  self.dest.setText("enter directory path with new file name like D:\\new_filename...")
  layout.addWidget(self.source)
  layout.addWidget(self.dest)  
  layout.addWidget(self.subm)
  self.widget = QWidget()
  self.widget.setLayout(layout)
  self.setCentralWidget(self.widget)
  self.subm.clicked.connect(self.renfile)
  self.subm.clicked.connect(self.close)

 def renfile(self):
  var4=self.source.toPlainText()
  var5=self.dest.toPlainText()
  shutil.move(var4,var5) 
  
class CreateWindow(QMainWindow):                   # creates window for creating file                       
 def __init__(self):
  QMainWindow.__init__(self)
  self.setWindowTitle("Create file")
  self.resize(300,150)
  layout = QVBoxLayout()
  self.text = QTextEdit()
  self.text1=QTextEdit()
  self.subm=QPushButton("ok")
  self.text1.setText("enter file name")
  self.text.setText("enter directory like C:\\foldername\\...")
  layout.addWidget(self.text)
  layout.addWidget(self.subm)  
  layout.addWidget(self.text1)
  self.widget = QWidget()
  self.widget.setLayout(layout)
  self.setCentralWidget(self.widget)
  self.subm.clicked.connect(self.cfile)
  self.subm.clicked.connect(self.close)  
 
  
 def cfile(self):
   var1=self.text.toPlainText()
   os.chdir(var1)
   fname=self.text1.toPlainText()
   f=open(fname,'w')
   f.write('hello world\n')
   f.close()

class CopyWindow(QMainWindow):                    #creates the window for copying file
 def __init__(self):
  QMainWindow.__init__(self)
  self.setWindowTitle("Copy")
  self.resize(300,150)
  layout = QVBoxLayout()
  self.source = QTextEdit()
  self.dest=QTextEdit()
  self.subm=QPushButton("ok")
  self.source.setText("enter source directory with file name")
  self.dest.setText("enter destination directory like C:\\foldername\\...")
  layout.addWidget(self.source)
  layout.addWidget(self.dest)  
  layout.addWidget(self.subm)
  self.widget = QWidget()
  self.widget.setLayout(layout)
  self.setCentralWidget(self.widget)  
  self.subm.clicked.connect(self.copfile)
  self.subm.clicked.connect(self.close)
  
 def copfile(self):
  var2=self.source.toPlainText()
  var3=self.dest.toPlainText()
  shutil.copy(var2, var3) 

  
class Menu(QWidget):                    # class deals with the central widget of the main window
 def __init__(self):
  super(Menu,self).__init__()
  self.options()
 def options(self):
  create=QPushButton('Create File',self)
  copy=QPushButton('Copy File',self)
  rename=QPushButton('Rename File',self)
  move=QPushButton('Move File',self)
  delete=QPushButton('Delete File',self)
  czip=QPushButton('Create ZipFile',self)
  ezip=QPushButton('Extract ZipFile',self) 
  grid=QGridLayout()
  self.setLayout(grid)
  grid.addWidget(create,1,0,1,3)
  grid.addWidget(copy,2,0,1,3)
  grid.addWidget(rename,3,0,1,3)
  grid.addWidget(move,4,0,1,3)
  grid.addWidget(delete,5,0,1,3)
  grid.addWidget(czip,6,0,1,3)
  grid.addWidget(ezip,7,0,1,3)
  self.connect(create, SIGNAL('clicked()'), self.create_newWindow)
  self.connect(copy, SIGNAL('clicked()'), self.copy_newWindow)
  self.connect(rename, SIGNAL('clicked()'), self.rename_newWindow)
  self.connect(delete, SIGNAL('clicked()'), self.delete_newWindow)
  self.connect(move, SIGNAL('clicked()'), self.move_newWindow)
  self.connect(czip, SIGNAL('clicked()'), self.czip_newWindow)
  self.connect(ezip, SIGNAL('clicked()'), self.ezip_newWindow)
 def ezip_newWindow(self):
   self.ezipscreen= EzipWindow()
   self.ezipscreen.show()  
 def czip_newWindow(self):
   self.czipscreen= CzipWindow()
   self.czipscreen.show()   
 def delete_newWindow(self):
   self.deletescreen= DeleteWindow()
   self.deletescreen.show()   
 
 def move_newWindow(self):
   self.movescreen= MoveWindow()
   self.movescreen.show()   
 def copy_newWindow(self):
  self.copyscreen= CopyWindow()
  self.copyscreen.show()
 def create_newWindow(self):
   self.myOtherWindow = CreateWindow()
   self.myOtherWindow.show()
 def rename_newWindow(self):
  self.renamescreen= RenameWindow()
  self.renamescreen.show()
  
class MainWindow(QMainWindow):                                # class provides the main window, the central widget
 def __init__(self):                                          #is part of menu class
  QMainWindow.__init__(self)
  exit = QAction(QIcon('icons/exit.png'), 'Exit', self)
  exit.setShortcut('Ctrl+Q')
  exit.setStatusTip('Exit application')
  self.connect(exit,SIGNAL('triggered()'), SLOT('close()'))
  menubar = self.menuBar()
  file = menubar.addMenu('&File')
  file.addAction(exit)
  c=Menu()
  self.setCentralWidget(c)
  
  
if __name__ == "__main__":
  app = QApplication(sys.argv)
  mainWindow = MainWindow()   
  mainWindow.show()
  sys.exit(app.exec_()) 
