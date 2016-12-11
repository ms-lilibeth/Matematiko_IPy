import wpf

from System.Windows import Window

class NotificationWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'NotificationWindow.xaml')
