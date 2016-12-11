import wpf
import clr
from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'MainWindow.xaml')
        self.button_new_game.Content = "It works!"
    

if __name__ == '__main__':    
    Application().Run(MyWindow())
