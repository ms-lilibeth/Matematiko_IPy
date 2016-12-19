# -*- coding: utf-8 -*-
import wpf
import System.Windows
from Game import Game
from Player import Player
from System.Windows.Media import Brushes
from System.Windows import FontWeights
from System.Windows.Markup import XamlReader
# Initialization Constants
Window = System.Windows.Window
Application = System.Windows.Application
Button = System.Windows.Controls.Button
StackPanel = System.Windows.Controls.StackPanel
Label = System.Windows.Controls.Label
Grid = System.Windows.Controls.Grid


class FieldCell(Label):
    def __init__(self, coords, game, player):
        if not isinstance(game, Game) or not isinstance(player, Player) \
            or not isinstance(coords, tuple):
            raise ValueError("Field cell: irrelevant types passed to constructor")
        self._this_game = game
        self._this_player = player
        self._coords = coords
        # Appearance initialization
        self.VerticalAlignment = System.Windows.VerticalAlignment.Stretch;
        self.HorizontalAlignment = System.Windows.HorizontalAlignment.Stretch;
        self.VerticalContentAlignment = System.Windows.VerticalAlignment.Center;
        self.HorizontalContentAlignment = System.Windows.HorizontalAlignment.Center;
        self.BorderThickness = System.Windows.Thickness(1);
        self.BorderBrush = Brushes.Black;
        self.Background = Brushes.LightYellow;
        self.FontWeight = FontWeights.Bold;
        self.FontSize = 22.0;   
        #self.MouseDoubleClick  = self.OnMouseDoubleClick    
    
    def OnMouseDoubleClick(self, e):
        #base.OnMouseDoubleClick(e);
        if self._this_player.get_the_value(self._coords)==0:        
            self.Content = self._this_game.get_current_card()
            self._this_player.tmp_cell_chosen(self, self._coords);


class PlayWindow(Window):
    def __init__(self, game, return_callback):        
        wpf.LoadComponent(self, 'PlayWindow.xaml')             
        if not isinstance(game, Game):
            raise ValueError("Play Window: irrelevant types passed to constructor")        
        
        self._this_game = game      
        self._return_callback = return_callback  
        # Filling fields with cells
        for i in range(self._this_game.field_lgth):
            for j in range(self._this_game.field_lgth):                
                tmp1 = FieldCell((i,j), self._this_game, self._this_game.player1);
                tmp2 = FieldCell((i,j), self._this_game, self._this_game.player2);
                Grid.SetRow(tmp1, i);
                Grid.SetColumn(tmp1, j);
                Grid.SetRow(tmp2, i);
                Grid.SetColumn(tmp2, j);                
                self.first_player_field.Children.Add(tmp1);
                self.second_player_field.Children.Add(tmp2)
        # Behavior
        self.BTTN_OK_1.Click += self.on_BTTN_OK_1_click
        self.BTTN_OK_2.Click += self.on_BTTN_OK_2_click
        self.BTTN_Return.Click += self.on_BTTN_return_click
        # Loading window
        #wpf.LoadComponent(self, 'PlayWindow.xaml')

    def on_BTTN_OK_1_click(self, sender, e):        
        self._this_game.player1.move_confirmed = True
        if self._this_game.both_confirmed:
            self._this_game.next_move()

    def on_BTTN_OK_2_click(self, sender, e):
        self._this_game.player2.move_confirmed = True
        if self._this_game.both_confirmed:
            self._this_game.next_move()

    def on_BTTN_return_click(self, sender, e):
        self._return_callback()
        self.Close()

    def on_window_closing(self, sender, e):
        self._return_callback()
              
