import sys
import demo
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget

if __name__ == '__main__':
    #创建QApplication类的实例
    app = QApplication(sys.argv)
    #创建一个窗口
    mainwindow = QMainWindow()
    ui = demo.Ui_MainWindow()
    ui.setupUi(mainwindow)
    #w = QWidget()
    #设置窗口尺寸
    # w.resize(400,300)
    # #移动窗口
    # w.move(300,300)
    #
    # #设置窗口的标题
    mainwindow.setWindowTitle('窗口一')
    #显示窗口
    mainwindow.show()
    #进入主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
