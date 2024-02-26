from more import *


app = Tk()
app.title("Math pack")
app.geometry("450x450")
app.resizable(0, 0)


Label(app, text = "Решить уравнение:", font = "Tahoma 12 bold").place(x = 250, y = 5)
left = Entry(app, width = 6, font = "Tahoma 12 bold")
left.place(x = 250, y = 30)
Label(app, text = " = ", font = "Tahoma 12 bold").place(x = 320, y = 30)
right = Entry(app, width = 6, font = "Tahoma 12 bold")
right.place(x = 355, y = 30)
Label(app, text = "x  = ", font = "Tahoma 12 bold").place(x = 250, y = 60)
x = Entry(app, width = 7, font = "Tahoma 12 bold")
x.place(x = 300,  y = 60)


Label(app, text = "График функции:", font = "Tahoma 12 bold").place(x = 250, y = 110)
Label(app, text = "y(x)  = ", font = "Tahoma 12 bold").place(x = 250, y = 145)
func = Entry(app, width = 6, font = "Tahoma 12 bold")
func.place(x = 320, y = 145)


Label(app, text = "Ариф. прогрессия:", font = "Tahoma 12 bold").place(x = 250, y = 190)
Label(app, text = "d  = ", font = "Tahoma 12 bold").place(x = 250, y = 220)
Label(app, text = "n  = ", font = "Tahoma 12 bold").place(x = 250, y = 250)
n = Entry(app, width = 6, font = "Tahoma 12 bold")
n.place(x = 310, y = 250)
d = Entry(app, width = 6, font = "Tahoma 12 bold")
d.place(x = 310, y = 220)
Label(app, text = "Результат:", font = "Tahoma 12 bold").place(x = 250, y = 285)
prog = Entry(app, width = 6, font = "Tahoma 12 bold")
prog.place(x = 360, y = 285)


Label(app, text = "Разложить многочлен:", font = "Tahoma 12 bold").place(x = 10, y = 5)
Label(app, text = "Результат: ", font = "Tahoma 12 bold").place(x = 10, y = 65)
expr = Entry(app, width = 10, font = "Tahoma 12 bold")
expr.place(x = 12, y = 35)
shorted = Entry(app, width = 16, font = "Tahoma 12 bold")
shorted.place(x = 10, y = 95)


Label(app, text = "Проверка на простоту:", font = "Tahoma 12 bold").place(x = 10, y = 140)
Label(app, text = "Простое ли: ", font = "Tahoma 12 bold").place(x = 10, y = 200)
primenum = Entry(app, width = 6, font = "Tahoma 12 bold")
primenum.place(x = 12, y = 170)
res = Entry(app, width = 3, font = "Tahoma 12 bold")
res.place(x = 120, y = 200)


def reset(all = False):
    x.delete(0, END)
    shorted.delete(0, END)
    res.delete(0, END)
    prog.delete(0, END)
    if all:
        primenum.delete(0, END)
        expr.delete(0, END)
        n.delete(0, END)
        d.delete(0, END)
        func.delete(0, END)
        right.delete(0, END)
        left.delete(0, END)


def main():
    try:
        reset()
        x.insert(END, solve_eq(left.get(), right.get()))
        shorted.insert(END, short(expr.get()))
        prog.insert(END, alg_progressive(d.get(), n.get()))
        res.insert(END, is_prime(primenum.get()))
        create_graph(func.get())
    except TclError: ...


add_hotkey("ctrl+r", reset)
add_hotkey("ctrl+a", lambda: reset(True))
Button(app, text = "Рассчитать", width = 10, font = "Tahoma 15 bold", command = main, bg = "blue", fg = "white").place(x = 160, y = 350)
Button(app, text = "Больше", width = 10, font = "Tahoma 15 bold", command = more, bg = "blue", fg = "white").place(x = 160, y = 400)


app.mainloop()