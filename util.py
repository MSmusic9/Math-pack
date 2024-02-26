from re import split as separate
from functools import cache
from re import *
from sympy import *
from sympy.parsing.sympy_parser import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from numpy import arange
from math import *
from keyboard import *
from time import sleep
from threading import Thread


name_re = "[a-zA-Zа-яА-Я][a-zA-Zа-яА-Я0-9]*"
float_re = "(\\-?[0-9]+(\\,[0-9]+)?)"
e_re = "(" + float_re + "e(\\+)?" + float_re + ")"
namearg_re = "(" + name_re + "(;" + name_re + ")*)"
func_re = name_re + "\\(" + namearg_re + "?\\)"
shortmul_re = float_re + name_re
array_re = "{.*(;.*)*}"
variables = {}
is_dark = False


def lex(s): return [i for i in separate(r'([\d.]+|\W+)', s.replace(" ", "")) if i]


def lex_to_python(string): return str(parse_expr(string.replace(",", "."), evaluate = False, transformations = "all"))


def lex_to_math(string): return string.replace(".", ",").replace("**", "^")


@cache
def is_prime(p):
    if p != "":
        try:
            n = eval(lex_to_python(p))
            for i in arange(2, round(n ** 0.5) + 1):
                if n % i == 0: return "нет"
            return "да"
        except: showerror("Ошибка", f"Нельзя проверить простоту числа: {p}")
    return "нет"


@cache
def lim(fn, v):
    if fn != "" and v != "":
        try: return str(limit(lex_to_python(fn), Symbol("x"), eval(lex_to_python(v))))
        except: showerror("Ошибка предела", f"Нельзя вычислить предел: {fn}")
    return ""


@cache
def diff_fn(fn):
    if fn != "":
        try: return str(diff(lex_to_python(fn), Symbol("x")))
        except: showerror("Ошибка дифференциала", f"Нельзя вычислить дифференциал: {fn}")
    return ""


@cache
def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n - 1)


@cache
def geom_md(nms):
    if fullmatch(".*(.*;\\s)*", nms) and nms != "":
        try: return sum(map(lambda el: eval(lex_to_python(el)), nms.split("; "))) ** (1 / len(nms.split("; ")))
        except BaseException as err: showerror("Ошибка среднего геометрического", f"Нельзя вычислить среднее геометрическое: {err.args}")
    return ""