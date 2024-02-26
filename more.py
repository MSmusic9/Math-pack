from lists import *


@cache
def caesar_cisper(s, sh):
    if s != "" and sh != "":
        try: return "".join([chr(ord(i) + eval(lex_to_python(sh)) % 255) for i in s])
        except: showerror("Ошибка шифровки", f"Нельзя закодировать текст: {sh}")
    return ""


def more():
    app = Tk()
    app.title("Больше - Math pack")
    app.geometry("700x400")
    app.resizable(0, 0)

    Label(app, text = "Шифр Цезаря:", font = "Tahoma 12 bold").place(x = 10, y = 10)
    Label(app, text = "Сдвиг:", font = "Tahoma 12 bold").place(x = 10, y = 40)
    Label(app, text = "Текст:", font = "Tahoma 12 bold").place(x = 10, y = 70)
    sh = Entry(app, width = 3, font = "Tahoma 12 bold")
    sh.place(x = 80, y = 40)
    txt = Entry(app, width = 12, font = "Tahoma 12 bold")
    txt.place(x = 80, y = 70)
    Label(app, text = "Результат:", font = "Tahoma 12 bold").place(x = 10, y = 100)
    cisper = Entry(app, width = 10, font = "Tahoma 12 bold")
    cisper.place(x = 120, y = 100)

    Label(app, text = "Геомет. прогрессия:", font = "Tahoma 12 bold").place(x = 10, y = 150)
    Label(app, text = "d  = ", font = "Tahoma 12 bold").place(x = 10, y = 180)
    Label(app, text = "n  = ", font = "Tahoma 12 bold").place(x = 10, y = 210)
    n = Entry(app, width = 6, font = "Tahoma 12 bold")
    n.place(x = 60, y = 210)
    d = Entry(app, width = 6, font = "Tahoma 12 bold")
    d.place(x = 60, y = 180)
    Label(app, text = "Результат:", font = "Tahoma 12 bold").place(x = 10, y = 235)
    prog = Entry(app, width = 6, font = "Tahoma 12 bold")
    prog.place(x = 120, y = 235)

    Label(app, text="Предел функции:", font="Tahoma 12 bold").place(x=250, y=10)
    Label(app, text="f(x) = ", font="Tahoma 12 bold").place(x=250, y=40)
    Label(app, text="x -> ", font="Tahoma 12 bold").place(x=250, y=70)
    fx = Entry(app, width=6, font="Tahoma 12 bold")
    fx.place(x=310, y=40)
    x = Entry(app, width=6, font="Tahoma 12 bold")
    x.place(x=300, y=70)
    Label(app, text="Результат:", font="Tahoma 12 bold").place(x=250, y=100)
    limx = Entry(app, width=6, font="Tahoma 12 bold")
    limx.place(x=355, y=100)

    Label(app, text="Производная функции:", font="Tahoma 12 bold").place(x=250, y=150)
    Label(app, text="f(x) = ", font="Tahoma 12 bold").place(x=250, y=180)
    fn1 = Entry(app, width=6, font="Tahoma 12 bold")
    fn1.place(x=310, y=180)
    Label(app, text="Результат:", font="Tahoma 12 bold").place(x=250, y=215)
    difx = Entry(app, width=6, font="Tahoma 12 bold")
    difx.place(x=360, y=215)

    Label(app, text="Среднее геомет.:", font="Tahoma 12 bold").place(x=480, y=10)
    Label(app, text="Числа:", font="Tahoma 12 bold").place(x=480, y=40)
    Label(app, text="Пример: -3,4; 2; 0,3^2", font="Tahoma 12 bold").place(x=480, y=70)
    nums = Entry(app, width=12, font="Tahoma 12 bold")
    nums.place(x=550, y=40)
    Label(app, text="Результат:", font="Tahoma 12 bold").place(x=480, y=100)
    geom_res = Entry(app, width=6, font="Tahoma 12 bold")
    geom_res.place(x=590, y=100)

    Label(app, text="Подстановка в формулу:", font="Tahoma 12 bold").place(x=480, y=150)
    Label(app, text="Формула:", font="Tahoma 12 bold").place(x=480, y=180)
    Label(app, text="Числа:", font="Tahoma 12 bold").place(x=480, y=215)
    formula = Entry(app, width=6, font="Tahoma 12 bold")
    formula.place(x=575, y=180)
    fnums = Entry(app, width=6, font="Tahoma 12 bold")
    fnums.place(x=550, y=215)
    Label(app, text="Результат:", font="Tahoma 12 bold").place(x=480, y=250)
    fres = Entry(app, width=6, font="Tahoma 12 bold")
    fres.place(x=585, y=250)

    def reset(all = False):
        prog.delete(0, END)
        cisper.delete(0, END)
        limx.delete(0, END)
        difx.delete(0, END)
        geom_res.delete(0, END)
        fres.delete(0, END)
        if all:
            nums.delete(0, END)
            fn1.delete(0, END)
            fx.delete(0, END)
            x.delete(0, END)
            d.delete(0, END)
            n.delete(0, END)
            sh.delete(0, END)
            txt.delete(0, END)
            formula.delete(0, END)
            fnums.delete(0, END)

    def run():
        try:
            reset()
            prog.insert(END, geom_progressive(d.get(), n.get()))
            cisper.insert(END, caesar_cisper(txt.get(), sh.get()))
            limx.insert(END, lim(fx.get(), x.get()))
            difx.insert(END, diff_fn(fn1.get()))
            geom_res.insert(END, geom_md(nums.get()))
            fres.insert(END, formula_md(formula.get(), fnums.get()))
        except TclError: ...

    add_hotkey("ctrl+r", reset)
    add_hotkey("ctrl+a", lambda: reset(True))
    Button(app, text = "Рассчитать", font = "Tahoma 15 bold", bg = "blue", fg = "white", command = run).place(x = 290, y = 300)
    #Button(app, text = "Новая программа", font = "Tahoma 15 bold", bg = "blue", fg = "white", command = create_program).place(x = 255, y = 350)

    app.mainloop()
more()