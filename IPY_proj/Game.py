class Player:
    def __init__(self, field_lgth):
        self._field = [[0 for j in range(field_lgth)] for i in range(field_lgth)]
        self._move_confirmed = False        
        pass 

    def save_the_value(self, value):
        pass

    def tmp_cell_chosen(self, cell, row, column):
        pass

    def get_the_value(self, row, column):
        return self._field[row][column]

