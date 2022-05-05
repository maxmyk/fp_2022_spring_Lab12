"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
            col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
            col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
            col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        n_path = Stack()
        n_path.push(self._start_cell)
        while not n_path.is_empty():
            cur_cell = n_path.peek()
            self._mark_path(cur_cell.row, cur_cell.col)
            if self._exit_found(cur_cell.row, cur_cell.col):
                return True
            moves = [
                (cur_cell.row, cur_cell.col-1),
                (cur_cell.row+1, cur_cell.col),
                (cur_cell.row, cur_cell.col+1),
                (cur_cell.row-1, cur_cell.col)
            ]
            has_valid = False
            for move in moves:
                if self._valid_move(move[0], move[1]):
                    n_path.push(_CellPosition(move[0], move[1]))
                    has_valid = True
            if not has_valid:
                self._mark_tried(cur_cell.row, cur_cell.col)
                n_path.pop()
                # for move in reversed(moves):
                #     if 0 <= move[0] < self.num_rows() and 0 <= move[1] < self.num_cols():
                #         if self._maze_cells[move[0], move[1]] == self.PATH_TOKEN:
                #             n_path.push(_CellPosition(move[0], move[1]))
            # print(self, '\n')
        return False

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] != self.MAZE_WALL:
                    self._maze_cells[row, col] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        return ' \n'.join([
            ' '.join([
                self._maze_cells[row, col] or '_'
                for col in range(self.num_cols())
            ]) for row in range(self.num_rows())
        ])+' '

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
            and col >= 0 and col < self.num_cols() \
            and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""

    def __init__(self, row, col):
        self.row = row
        self.col = col


def build_maze(filename):
    """Builds a maze based on a text format in the given file."""
    infile = open(filename, "r")

    # Read the size of the maze.
    nrows, ncols = read_value_pair(infile)
    maze1 = Maze(nrows, ncols)

    # Read the starting and exit positions.
    row, col = read_value_pair(infile)
    maze1.set_start(row, col)
    row, col = read_value_pair(infile)
    maze1.set_exit(row, col)

    # Read the maze itself.
    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            if line[col] == "*":
                maze1.set_wall(row, col)

    # Close the maze file and return the newly constructed maze.
    infile.close()

    return maze1


def read_value_pair(infile):
    """Extracts an integer value pair from the given input file."""
    line = infile.readline()
    val_a, val_b = line.split()
    return int(val_a), int(val_b)


if __name__ == '__main__':
    maze = build_maze("Maze/mazefile1.txt")
    print(maze.find_path())
    print(maze)
