# -*- coding: utf-8 -*-
import clr
import random
import json
import itertools
from Player import Player
from NotificationWindow import NotificationWindow
from System import Array

class Game:
    def __init__(self):
        self.both_confirmed = False
        self.field_lgth = 5
        self.player1 = Player(self.field_lgth)
        self.player2 = Player(self.field_lgth)
        self._this_window = None
        self._cards = []        
        self._cards_qty = 25
        self._current_card = 0
        clr.AddReferenceByName("MatematikoCountScores.dll")
        from MatematikoCountScores import ResultCounter
        self._result_counter = ResultCounter

    def get_current_card(self):
        return self._current_card

    def both_confirmed(self):
        if player1.move_confirmed() and player2.move_confirmed():
            return True
        return False        

    def _init_cards(self, cards_num):
        ''' Заполняет стек из 25 карточек случайными числами от 1 до 13 
             (каждое повторяется не более 4х раз) '''
        repetition_list = [0 for i in range(13)]
        while len(self._cards) != self._cards_qty:
            tmp = random.randint(1, 13) # endpoints included
            if repetition_list[tmp-1] < 4:
                self._cards.append(tmp)
                repetition_list[tmp-1] += 1        

    def _next_card(self):
        if len(self._cards) == 0:
            return 0
        res = self._cards[-1]
        del self._cards[-1]
        return res

    def start(self, play_window):
        self._this_window = play_window
        self._init_cards()
        self._current_card = self._next_card()
        self._this_window.LBL_Current_card.Content = self._current_card
        self._this_window.Show()
    
    def next_move(self):
        # Записывает значение, поставленное в соотв.клетку поля в матрицу
        self.player1.save_the_value(self._current_card)
        self.player2.save_the_value(self._current_card)
        if len(self._cards) != 0:
            self._current_card = self._next_card()
            self._this_window.LBL_Current_card.Content = self._current_card
            # Изменяем цвет метки
            if self._this_window.LBL_Current_card.Background == Brushes.Khaki:
                self._this_window.LBL_Current_card.Background = Brushes.Gold
            else:
                self._this_window.LBL_Current_card.Background = Brushes.Khaki
        else:
            #TODO: вызов методов из dll для подсчета результатов
            #TODO: is it right?
            field1D_1 = list(itertools.chain.from_iterable(player1.field))
            field1D_2 = list(itertools.chain.from_iterable(player2.field))
            arr1 = Array.CreateInstance(int, self.field_lgth*self.field_lgth)
            arr2 = Array.CreateInstance(int, self.field_lgth*self.field_lgth)
            for i in range(len(field1D_1)):
                arr1[i] = field1D_1[i]
                arr2[i] = field1D_2[i]
            res_str1 = _result_counter.CountResults(arr1, self.field_lgth)
            res_str2 = _result_counter.CountResults(arr2, self.field_lgth)
            res1 = json.loads(res_str1)
            res2 = json.loads(res_str2)
            notify_win = NotificationWindow(res1, res2)
            notify_win.ShowDialog()
