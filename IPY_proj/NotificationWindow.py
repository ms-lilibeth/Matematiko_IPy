import wpf
import System.Windows

# Initialization Constants
Window = System.Windows.Window
Application = System.Windows.Application
Button = System.Windows.Controls.Button
StackPanel = System.Windows.Controls.StackPanel
Label = System.Windows.Controls.Label


class NotificationWindow(Window):
    def __init__(self, res1, res2):
        wpf.LoadComponent(self, 'NotificationWindow.xaml')
