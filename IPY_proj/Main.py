import wpf
import clr
import System.Windows

# Initialization Constants
Window = System.Windows.Window
Application = System.Windows.Application
Button = System.Windows.Controls.Button
StackPanel = System.Windows.Controls.StackPanel
Label = System.Windows.Controls.Label

class MainWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'MainWindow.xaml')
        self.button_new_game.Content = "It works!"
    

if __name__ == '__main__':    
    Application().Run(MyWindow())
