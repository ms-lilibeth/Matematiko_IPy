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
    "INLINE_3EqNum": 40, # 3 одинаковых числа
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

class NotificationWindow(Window):
    def __init__(self, res1, res2):
        wpf.LoadComponent(self, 'NotificationWindow.xaml')
        self.initUI(res1, res2)

    def initUI(self, res1, res2):
        ''' Выводим сообщение о победителе '''
        if player1['Sum'] > player2['Sum']:
            self.congratulation.Text = "Победил первый игрок!"
        if player2['Sum'] > player1['Sum']:
            self.congratulation.Text = "Победил второй игрок!"
        if player1['Sum'] == player2['Sum']:
            self.congratulation.Text = "Ничья"

        '''Расписываем очки для каждого игрока'''
        # прописать для одного, а для другого сделать Ctrl+C, Ctrl+V и поменять левую часть выражения
        # ===================== Player1 ========================
        result = res1
        if result['INLINE_1_10_11_12_13']!=0 or result['BIAS_1_10_11_12_13']!=0:
            self.Pl1_1_10_11_12_13.Text = self.MessageBuilder(result['INLINE_1_10_11_12_13'] * scores['INLINE_1_10_11_12_13'],\
               result['INLINE_1_10_11_12_13'], result['BIAS_1_10_11_12_13'] * scores['BIAS_1_10_11_12_13'], result['BIAS_1_10_11_12_13'])
        if result['INLINE_2EqNums'] != 0 or result['BIAS_2EqNums'] != 0:
            self.Pl1_2EqNums.Text = self.MessageBuilder(result['INLINE_2EqNums'] * scores['INLINE_2EqNums'],\
               result['INLINE_2EqNums'], result['BIAS_2EqNums'] * scores['BIAS_2EqNums'], result['BIAS_2EqNums'])
        if result['INLINE_2PairsOfEqNums'] != 0 or result['BIAS_2PairsOfEqNums'] != 0:
            self.Pl1_2PairsOfEqNums.Text = self.MessageBuilder(result['INLINE_2PairsOfEqNums'] * scores['INLINE_2PairsOfEqNums'], \
                result['INLINE_2PairsOfEqNums'], result['BIAS_2PairsOfEqNums'] * scores['BIAS_2PairsOfEqNums'], result['BIAS_2PairsOfEqNums'])
        if result['INLINE_3EqNums'] != 0 or result['BIAS_3EqNums'] != 0:
            self.Pl1_3EqNums.Text = self.MessageBuilder(result['INLINE_3EqNums'] * scores['INLINE_3EqNums'], result['INLINE_3EqNums'], \
                result['BIAS_3EqNums'] * scores['BIAS_3EqNums'], result['BIAS_3EqNums'])
        if result['INLINE_3EqNums_plus_2EqNums'] != 0 or result['BIAS_3EqNums_plus_2EqNums'] != 0:
            self.Pl1_3plus2EqNums.Text = self.MessageBuilder(result['INLINE_3EqNums_plus_2EqNums'] * scores['INLINE_3EqNums_plus_2EqNums'],\
               result['INLINE_3EqNums_plus_2EqNums'], result['BIAS_3EqNums_plus_2EqNums'] * scores['BIAS_3EqNums_plus_2EqNums'], \
               result['BIAS_3EqNums_plus_2EqNums'])
        if result['INLINE_4EqNums'] != 0 or result['BIAS_4EqNums'] != 0:
            self.Pl1_4EqNums.Text = self.MessageBuilder(result['INLINE_4EqNums'] * scores['INLINE_4EqNums'],\
               result['INLINE_4EqNums'], result['BIAS_4EqNums'] * scores['BIAS_4EqNums'], result['BIAS_4EqNums'])
        if result['INLINE_4Ones'] != 0 or result['BIAS_4Ones'] != 0:
            self.Pl1_4Ones.Text = self.MessageBuilder(result['INLINE_4Ones'] * scores['INLINE_4Ones'], \
                result['INLINE_4Ones'], result['BIAS_4Ones'] * scores['BIAS_4Ones'], result['BIAS_4Ones'])
        if result['INLINE_5ConsecutiveNums'] != 0 or result['BIAS_5ConsecutiveNums'] != 0:
            self.Pl1_5ConsecutiveNums.Text = self.MessageBuilder(result['INLINE_5ConsecutiveNums'] * scores['INLINE_5ConsecutiveNums'],\
               result['INLINE_5ConsecutiveNums'], result['BIAS_5ConsecutiveNums'] * scores['BIAS_5ConsecutiveNums'], result['BIAS_5ConsecutiveNums'])
        if result['INLINE_Three_1_Two_13'] != 0 or result['BIAS_Three_1_Two_13'] != 0:
            self.Pl1_Three_1_Two_13.Text = self.MessageBuilder(result['INLINE_Three_1_Two_13'] * scores['INLINE_Three_1_Two_13'], \
                result['INLINE_Three_1_Two_13'], result['BIAS_Three_1_Two_13'] * scores['BIAS_Three_1_Two_13'], result['BIAS_Three_1_Two_13'])
        self.Pl1_Sum.Text = str(result['Sum'])
        # ===================== Player2 ========================
        result = res2
        if result['INLINE_1_10_11_12_13']!=0 or result['BIAS_1_10_11_12_13']!=0:
            self.Pl1_1_10_11_12_13.Text = self.MessageBuilder(result['INLINE_1_10_11_12_13'] * scores['INLINE_1_10_11_12_13'],\
               result['INLINE_1_10_11_12_13'], result['BIAS_1_10_11_12_13'] * scores['BIAS_1_10_11_12_13'], result['BIAS_1_10_11_12_13'])
        if result['INLINE_2EqNums'] != 0 or result['BIAS_2EqNums'] != 0:
            self.Pl2_2EqNums.Text = self.MessageBuilder(result['INLINE_2EqNums'] * scores['INLINE_2EqNums'],\
               result['INLINE_2EqNums'], result['BIAS_2EqNums'] * scores['BIAS_2EqNums'], result['BIAS_2EqNums'])
        if result['INLINE_2PairsOfEqNums'] != 0 or result['BIAS_2PairsOfEqNums'] != 0:
            self.Pl2_2PairsOfEqNums.Text = self.MessageBuilder(result['INLINE_2PairsOfEqNums'] * scores['INLINE_2PairsOfEqNums'], \
                result['INLINE_2PairsOfEqNums'], result['BIAS_2PairsOfEqNums'] * scores['BIAS_2PairsOfEqNums'], result['BIAS_2PairsOfEqNums'])
        if result['INLINE_3EqNums'] != 0 or result['BIAS_3EqNums'] != 0:
            self.Pl2_3EqNums.Text = self.MessageBuilder(result['INLINE_3EqNums'] * scores['INLINE_3EqNums'], result['INLINE_3EqNums'], \
                result['BIAS_3EqNums'] * scores['BIAS_3EqNums'], result['BIAS_3EqNums'])
        if result['INLINE_3EqNums_plus_2EqNums'] != 0 or result['BIAS_3EqNums_plus_2EqNums'] != 0:
            self.Pl2_3plus2EqNums.Text = self.MessageBuilder(result['INLINE_3EqNums_plus_2EqNums'] * scores['INLINE_3EqNums_plus_2EqNums'],\
               result['INLINE_3EqNums_plus_2EqNums'], result['BIAS_3EqNums_plus_2EqNums'] * scores['BIAS_3EqNums_plus_2EqNums'], \
               result['BIAS_3EqNums_plus_2EqNums'])
        if result['INLINE_4EqNums'] != 0 or result['BIAS_4EqNums'] != 0:
            self.Pl2_4EqNums.Text = self.MessageBuilder(result['INLINE_4EqNums'] * scores['INLINE_4EqNums'],\
               result['INLINE_4EqNums'], result['BIAS_4EqNums'] * scores['BIAS_4EqNums'], result['BIAS_4EqNums'])
        if result['INLINE_4Ones'] != 0 or result['BIAS_4Ones'] != 0:
            self.Pl2_4Ones.Text = self.MessageBuilder(result['INLINE_4Ones'] * scores['INLINE_4Ones'], \
                result['INLINE_4Ones'], result['BIAS_4Ones'] * scores['BIAS_4Ones'], result['BIAS_4Ones'])
        if result['INLINE_5ConsecutiveNums'] != 0 or result['BIAS_5ConsecutiveNums'] != 0:
            self.Pl2_5ConsecutiveNums.Text = self.MessageBuilder(result['INLINE_5ConsecutiveNums'] * scores['INLINE_5ConsecutiveNums'],\
               result['INLINE_5ConsecutiveNums'], result['BIAS_5ConsecutiveNums'] * scores['BIAS_5ConsecutiveNums'], result['BIAS_5ConsecutiveNums'])
        if result['INLINE_Three_1_Two_13'] != 0 or result['BIAS_Three_1_Two_13'] != 0:
            self.Pl2_Three_1_Two_13.Text = self.MessageBuilder(result['INLINE_Three_1_Two_13'] * scores['INLINE_Three_1_Two_13'], \
                result['INLINE_Three_1_Two_13'], result['BIAS_Three_1_Two_13'] * scores['BIAS_Three_1_Two_13'], result['BIAS_Three_1_Two_13'])
        self.Pl2_Sum.Text = str(result['Sum'])

    def MessageBuilder(inline_sum, inline_qty, bias_sum, bias_qty):
        s = "+" + str(inline_sum) + " (" + str(inline_qty) + " в стр./стб.) + " \
            + str(bias_sum) + " (" + str(bias_qty) + " по диаг.)"
        return s

