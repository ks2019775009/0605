import turtle as t # 2019775009 김수민
from winsound import Beep

freq = { "c4":262, "d4":294, "e4":294, "f4":294, "g4":294, "a4":294, "b4":294,
         "c5":294, "d5":294 }
def play_freq(n):
    Beep(freq[n], 300)

def Key_1():
    play_freq("c4")
def Key_2():
    play_freq("d4")
def Key_3():
    play_freq("e4")
def Key_4():
    play_freq("f4")
def Key_5():
    play_freq("g4")
def Key_6():
    play_freq("a4")
def Key_7():
    play_freq("b4")
def Key_8():
    play_freq("c5")
def Key_9():
    play_freq("d5")

t.setup(600,600)
s = t.Screen()

s.onkey(Key_1, "1")
s.onkey(Key_2, "2")
s.onkey(Key_3, "3")
s.onkey(Key_4, "4")
s.onkey(Key_5, "5")
s.onkey(Key_6, "6")
s.onkey(Key_7, "7")
s.onkey(Key_8, "8")
s.onkey(Key_9, "9")
s.listen()

