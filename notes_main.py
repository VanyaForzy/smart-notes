#почни тут створювати додаток з розумними замітками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QListWidget, 
                             QLayout, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit,
                             QLineEdit, QInputDialog)  

app = QApplication([])

win = QWidget()
win.setWindowTitle("Smart notes")
win.resize(900,600)

list_notes = QListWidget() 
list_tags = QListWidget() 

btn_note_create = QPushButton("Create")
btn_note_del = QPushButton("Delete")
btn_note_save = QPushButton("Save")
btn_tag_add = QPushButton("Add")
btn_tag_del = QPushButton("Delete")
btn_tag_search = QPushButton("Search")

line_edit = QLineEdit()
text_edit = QTextEdit()
line_edit.setPlaceholderText("Enter tag...")

col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

row_1 = QHBoxLayout()
row_2 = QHBoxLayout()
row_3 = QHBoxLayout()
row_4 = QHBoxLayout()

layout = QHBoxLayout()

row_1.addWidget(btn_note_create)
row_1.addWidget(btn_note_del)
row_2.addWidget(btn_note_save)
row_3.addWidget(btn_tag_add)
row_3.addWidget(btn_tag_del)
row_4.addWidget(btn_tag_search)

col_1.addWidget(text_edit)
col_2.addWidget(list_notes)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags)
col_2.addWidget(line_edit)
col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout.addLayout(col_1, stretch=2)
layout.addLayout(col_2, stretch=1)
win.setLayout(layout)
win.show()
app.exec_()
















