# -*- coding: utf-8 -*-
import wpf
import System.Windows

# Initialization of Constants
Window = System.Windows.Window
Application = System.Windows.Application
Button = System.Windows.Controls.Button
StackPanel = System.Windows.Controls.StackPanel
Label = System.Windows.Controls.Label

# Кол-во очков, дающееся за выполнение каждого условия
scores = {
    "INLINE_3EqNums": 40, # 3 одинаковых числа
    "INLINE_2EqNums": 10, # 2 одинаковых числа
    "INLINE_4EqNums": 160, # 4 одинаковых числа
    "INLINE_2PairsOfEqNums": 20, # 2 пары одинаковых чисел
    "INLINE_3EqNums_plus_2EqNums": 80, # 3+2 одинаковых чисел
    "INLINE_5ConsecutiveNums": 50, # 5 послед.чисел в любом порядке
    "INLINE_Three_1_Two_13": 100,# 3 единицы, 2 "13"
    "INLINE_1_10_11_12_13": 150, # "1", "10", "11", "12", "13" в любом порядке
    "INLINE_4Ones": 200, # четыре единицы
    # по диагонали
    "BIAS_2EqNums": 20, # 2 одинаковых числа
    "BIAS_3EqNums": 50, # 3 одинаковых числа
    "BIAS_4EqNums": 170, # 4 одинаковых числа
    "BIAS_2PairsOfEqNums": 30, #  2 пары одинаковых чисел
    "BIAS_3EqNums_plus_2EqNums": 90, # 3+2 одинаковых чисел
    "BIAS_5ConsecutiveNums": 60, # 5 послед.чисел в любом порядке
    "BIAS_Three_1_Two_13": 110,# 3 единицы, 2 "13"
    "BIAS_1_10_11_12_13": 160, # "1", "10", "11", "12", "13" в любом порядке
    "BIAS_4Ones": 210 #  четыре единицы
    }

postfix_list = ['2EqNums', '3EqNums', '4EqNums', '2PairsOfEqNums', '3EqNums_plus_2EqNums',
                '5ConsecutiveNums', 'Three_1_Two_13', '1_10_11_12_13', '4Ones']


class NotificationWindow(Window):
    def __init__(self, res1, res2):
        wpf.LoadComponent(self, 'NotificationWindow.xaml')        
        self.player1_labels = {'2EqNums': self.Pl1_2EqNums, '3EqNums': self.Pl1_3EqNums, 
                               '4EqNums': self.Pl1_4EqNums, '2PairsOfEqNums': self.Pl1_2PairsOfEqNums,
                               '3EqNums_plus_2EqNums': self.Pl1_3plus2EqNums, '5ConsecutiveNums': self.Pl1_5ConsecutiveNums, 
                               'Three_1_Two_13': self.Pl1_Three_1_Two_13, '1_10_11_12_13': self.Pl1_1_10_11_12_13, 
                               '4Ones': self.Pl1_4Ones}
        self.player2_labels = {'2EqNums': self.Pl2_2EqNums, '3EqNums': self.Pl2_3EqNums, 
                               '4EqNums': self.Pl2_4EqNums, '2PairsOfEqNums': self.Pl2_2PairsOfEqNums,
                               '3EqNums_plus_2EqNums': self.Pl2_3plus2EqNums, '5ConsecutiveNums': self.Pl2_5ConsecutiveNums, 
                               'Three_1_Two_13': self.Pl2_Three_1_Two_13, '1_10_11_12_13': self.Pl2_1_10_11_12_13, 
                               '4Ones': self.Pl2_4Ones}
        self.initUI(res1, res2)

    def initUI(self, res1, res2):
        ''' Выводим сообщение о победителе '''
        if res1['Sum'] > res2['Sum']:
            self.congratulation.Text = "Победил первый игрок!"
        if res2['Sum'] > res1['Sum']:
            self.congratulation.Text = "Победил второй игрок!"
        if res1['Sum'] == res2['Sum']:
            self.congratulation.Text = "Ничья"

        for p in postfix_list:
            self.player1_labels[p].Text = self.MessageBuilder(res1, p)
            self.player2_labels[p].Text = self.MessageBuilder(res2, p)
        
        self.Pl1_Sum.Text = str(res1['Sum'])           
        self.Pl2_Sum.Text = str(res2['Sum'])

    def MessageBuilder(self, result, postfix):
        inline = 'INLINE_'+postfix
        bias = 'BIAS_'+postfix
        if result[inline] != 0 or result[bias]!=0:
            inline_qty = result[inline]
            inline_sum = inline_qty * scores[inline]
            bias_qty = result[bias]
            bias_sum = bias_qty * scores[bias]        
            s = "+" + str(inline_sum) + " (" + str(inline_qty) + " в стр./стб.) + " \
                + str(bias_sum) + " (" + str(bias_qty) + " по диаг.)"
        else:
            s = "0"
        return s
