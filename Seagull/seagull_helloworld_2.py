import seagull as sg
from seagull import lifeforms as lf

board = sg.Board(size=(30,30))
board.add(lf.Blinker(length=3), loc=(4,4))
board.add(lf.Glider(), loc=(10,4))
board.add(lf.Glider(), loc=(15,4))
board.add(lf.Pulsar(), loc=(5,12))
board.view()  # View the current state of the board