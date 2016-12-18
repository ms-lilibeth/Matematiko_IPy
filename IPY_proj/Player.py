# -*- coding: utf-8 -*-
class Player:
    def __init__(self, field_lgth):
        self.field = [[0 for j in range(field_lgth)] for i in range(field_lgth)]
        self.move_confirmed = False  # подтвердил ли игрок свой выбор
        self._last_cell_chosen = (-1, -1)  # выбранная, но не подтвержденная клетка               
    # Записывает значение, поставленное в эту клетку поля, в матрицу
    def save_the_value(self, value):
        pass

    def tmp_cell_chosen(self, cell, coords):
        pass

    def get_the_value(self, coords):
        return self._field[coords[0]][coords[1]]