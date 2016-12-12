import clr
import random
import json
from PlayWindow import PlayWindow
from NotificationWindow import NotificationWindow
from System.Windows.Media import Brushes
class Player:
    def __init__(self, field_lgth):
        self.field = [[0 for j in range(field_lgth)] for i in range(field_lgth)]
        self.move_confirmed = False     
        self._last_cell_chosen = (-1, -1)                   
    #  Окончательно записывает значение, поставленное в эту клетку поля, в матрицу
    def save_the_value(self, value):
        pass

    def tmp_cell_chosen(self, cell, coords):
        pass

    def get_the_value(self, coords):
        return self._field[coords[0]][coords[1]]

class Game:
    def __init__(self):
        self.both_confirmed = False
        self.field_lgth = 5
        self.player1 = Player(field_lgth)
        self.player2 = Player(field_lgth)
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
            field1D_1 = [i for i in j for j in player1.field]
            field1D_2 = [i for i in j for j in player2.field]
            res_str1 = _result_counter.CountResults(field1D_1, self.field_lgth)
            res_str2 = _result_counter.CountResults(field1D_2, self.field_lgth)
            res1 = json.loads(res_str1)
            res2 = json.loads(res_str2)
            notify_win = NotificationWindow(res1, res2)
            notify_win.ShowDialog()
