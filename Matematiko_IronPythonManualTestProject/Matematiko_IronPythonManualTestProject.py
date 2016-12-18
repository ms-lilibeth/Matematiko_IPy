import wpf
from System.Windows import Application, Window
import NotificationWindowTest
class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Matematiko_IronPythonManualTestProject.xaml')            

if __name__ == '__main__':
    NotificationWindowTest.TestFixedResultSet()
    #Application().Run(MyWindow())
