import tkinter as tk

GRID_OFFSET = 10
MIN_CELL_SIZE = 50

FONT_STYLE = 'Consolas'
FONT_SIZE = 20

task = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

subsquare_numbers = {
    '0,0': 0,
    '0,1': 1,
    '0,2': 2,
    '1,0': 3,
    '1,1': 4,
    '1,2': 5,
    '2,0': 6,
    '2,1': 7,
    '2,2': 8
}


def create_grid():
    """
    creates Sudoku grid made of 3x3 subsquares made of 3x3 cells
    :return: list of Label objects
    """
    labels = []
    for subsquare in range(9):
        frm_subsquare = tk.Frame(master=frm_main, bg='green')
        frm_subsquare.grid(row=subsquare // 3, column=subsquare % 3, padx=1, pady=1, sticky='nswe')
        labels_subsquare = []
        for cell_row in range(3):
            frm_subsquare.columnconfigure(cell_row, weight=1, minsize=MIN_CELL_SIZE)
            frm_subsquare.rowconfigure(cell_row, weight=1, minsize=MIN_CELL_SIZE)
            labels_row = []
            for cell_col in range(3):
                lbl_num = tk.Label(master=frm_subsquare, fg='green', bg='black', text='', font=(FONT_STYLE, FONT_SIZE))
                lbl_num.grid(row=cell_row, column=cell_col, padx=1, pady=1, sticky='nswe')
                labels_row.append(lbl_num)
            labels_subsquare.append(labels_row)
        labels.append(labels_subsquare)
    return labels


def populate_grid():
    for row in range(9):
        for col in range(9):
            subsquare_index = subsquare_numbers[str(row // 3) + ',' + str(col // 3)]
            row_index = row % 3
            col_index = col % 3
            lbl_num = labels[subsquare_index][row_index][col_index]

            num = task[row][col]
            if num != 0:
                str_num = str(num)
                lbl_num['text'] = str_num
                lbl_num.config(fg='white')


window = tk.Tk()
window.config(bg='green')
frm_main = tk.Frame(master=window, bg='green')
frm_main.pack(padx=GRID_OFFSET, pady=GRID_OFFSET, expand=True)

labels = create_grid()
populate_grid()

window.mainloop()
