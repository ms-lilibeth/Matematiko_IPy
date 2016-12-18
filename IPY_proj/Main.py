# -*- coding: utf-8 -*-
import wpf
import clr
import System.Windows
from PlayWindow import PlayWindow
from Game import Game

# Initialization Constants
Window = System.Windows.Window
Application = System.Windows.Application
Button = System.Windows.Controls.Button
StackPanel = System.Windows.Controls.StackPanel
Label = System.Windows.Controls.Label

class MainWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'MainWindow.xaml')
        self.button_new_game.Click += self.on_button_new_game_click

    def on_button_new_game_click(self, sender, event):
        #self.button_new_game.Content = "It works!"
        new_game = Game()
        play_window = PlayWindow(new_game, self.Show)
        self.Hide()
        new_game.start(play_window)
    

if __name__ == '__main__':    
    Application().Run(MainWindow())
