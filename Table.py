import math

class Table:

    def __init__(self, rows, title="No Title"):
        self.title = title
        self.rows = rows

        if len(rows) < 1:
            return

        self.columnCount = len(self.rows[0])
        self.rowCount = len(self.rows)
        self.padding = 2
        self.fullWidth = 0

        self.set_dimensions()
        self.make_table()
    
    def set_dimensions(self):
        self.greatestWidth = [0 for i in range(self.columnCount)]
        self.widths = [[0 for i in range(self.columnCount)] for j in range(self.rowCount)]

        for rowIndex, row in enumerate(self.rows):
            for columnIndex, word in enumerate(row):
                if (self.greatestWidth[columnIndex] <= len(str(word))):
                    self.greatestWidth[columnIndex] = len(str(word))

                self.widths[rowIndex][columnIndex] = len(str(word))
                
        for i in range(len(self.greatestWidth)):
            self.greatestWidth[i] += 1
            self.fullWidth += self.greatestWidth[i] + self.padding + 1

    def make_table(self):
        self.requiredSpaces = [[0 for i in range(self.columnCount)] for j in range(self.rowCount)]
        
        for rowIndex, row in enumerate(self.rows):
            for columnIndex, word in enumerate(row):
                difference = self.greatestWidth[columnIndex] - self.widths[rowIndex][columnIndex]
                self.requiredSpaces[rowIndex][columnIndex] = difference
        
        self.tempTable = [['' for j in range(self.columnCount)] for j in range(self.rowCount) ]

        for rowIndex, row in enumerate(self.rows):
            for columnIndex, word in enumerate(row):
                self.tempTable[rowIndex][columnIndex] = str(word) + ( ' ' * (self.requiredSpaces[rowIndex][columnIndex] + self.padding) )

        self.table = ['' for j in range(self.rowCount)]

        for rowIndex, row in enumerate(self.tempTable):
            self.table[rowIndex] = ''.join(row)
            self.table[rowIndex] += '\n'

        self.table = ''.join(self.table).replace(',', '\n')
        self.table = ''.join(self.table)

    def print(self):
        if (len(self.rows) < 1):
            print("table '" + self.title.capitalize() + "' has no content")
            return
        
        self.print_title()
        print(self.table)

    def print_title(self):
        non_title_distance = math.ceil (self.fullWidth / 2)  - len(self.title)
        offset = ( ("=" * non_title_distance ) )
        
        print(offset, self.title.capitalize(), offset)