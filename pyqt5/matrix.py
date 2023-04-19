from random import randint, randrange

from tile import Tile


class Matrix:

    def __init__(self, parent):
        self.parent = parent
        self.data = []
        self.grid = 4
        self.space_between_tiles = 5
        self.tile_size = 55
        self.modified = False
        self.fill()

    def fill(self):
        x = randint(0, self.grid - 1)
        y = randint(0, self.grid - 1)
        for row in range(self.grid):
            self.data.append([])
            for column in range(self.grid):
                self.data[row].append([])
        for row in self.data:
            for cell in row:
                cell.append(Tile(self, 0))
        self.data[x][y][0].set_value(randrange(2, 5, 2))

    def cells_to_draw(self):
        cells = []
        for row in self.data:
            for cell in row:
                if cell[0].value != 0:
                    cells.append(cell[0])
        return cells

    def find_empty_cells(self):
        empty_cells = []
        for row in range(self.grid):
            for cell in range(self.grid):
                if self.data[row][cell][0].value == 0:
                    empty_cells.append((row, cell))
        return empty_cells

    def spawn(self):
        empty_cells = self.find_empty_cells()
        xy = randint(0, len(empty_cells) - 1)
        x = empty_cells[xy][0]
        y = empty_cells[xy][1]
        self.data[x][y][0].set_value(randrange(2, 5, 2))

    def left(self):
        for row in range(self.grid):
            for col in range(self.grid):
                if self.data[row][col][0].value != 0:
                    nr, nc = self.shift_tile_left(row, col)
                    if nc != col:
                        self.modified = True

    def shift_tile_left(self, r, c):
        if c == 0:
            return r, c
        if self.data[r][c - 1][0].value == 0:
            self.data[r][c - 1][0].set_value(self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return self.shift_tile_left(r, c - 1)
        if self.data[r][c - 1][0].value == self.data[r][c][0].value:
            self.data[r][c - 1][0].set_value(self.data[r][c - 1][0].value + self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return r, c - 1
        return r, c

    def up(self):
        for row in range(self.grid):
            for col in range(self.grid):
                if self.data[row][col][0].value != 0:
                    nr, nc = self.shift_tile_up(row, col)
                    if nr != row:
                        self.modified = True

    def shift_tile_up(self, r, c):
        if r == 0:
            return r, c
        if self.data[r - 1][c][0].value == 0:
            self.data[r - 1][c][0].set_value(self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return self.shift_tile_up(r - 1, c)
        if self.data[r - 1][c][0].value == self.data[r][c][0].value:
            self.data[r - 1][c][0].set_value(self.data[r - 1][c][0].value + self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return r - 1, c
        return r, c

    def right(self):
        for row in range(self.grid - 1, -1, -1):
            for col in range(self.grid - 1, -1, -1):
                if self.data[row][col][0].value != 0:
                    nr, nc = self.shift_tile_right(row, col)
                    if nc != col:
                        self.modified = True

    def shift_tile_right(self, r, c):
        if c == self.grid - 1:
            return r, c
        if self.data[r][c + 1][0].value == 0:
            self.data[r][c + 1][0].set_value(self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return self.shift_tile_right(r, c + 1)
        if self.data[r][c + 1][0].value == self.data[r][c][0].value:
            self.data[r][c + 1][0].set_value(self.data[r][c + 1][0].value + self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return r, c + 1
        return r, c

    def down(self):
        for row in range(self.grid - 1, -1, -1):
            for col in range(self.grid - 1, -1, -1):
                if self.data[row][col][0].value != 0:
                    nr, nc = self.shift_tile_down(row, col)
                    if nr != row:
                        self.modified = True

    def shift_tile_down(self, r, c):
        if r == self.grid - 1:
            return r, c
        if self.data[r + 1][c][0].value == 0:
            self.data[r + 1][c][0].set_value(self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return self.shift_tile_down(r + 1, c)
        if self.data[r + 1][c][0].value == self.data[r][c][0].value:
            self.data[r + 1][c][0].set_value(self.data[r + 1][c][0].value + self.data[r][c][0].value)
            self.data[r][c][0].set_value(0)
            return r + 1, c
        return r, c

    def check_state(self):
        if len(self.find_empty_cells()) == 0:
            return False
        return True

    def find_2048(self):
        for row in self.data:
            for cell in row:
                if cell[0].value == 2048:
                    return True
        return False
