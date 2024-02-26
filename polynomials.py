from util import *


@cache
def short(polynomial):
    if polynomial != "":
        try: return lex_to_math(str(powsimp(simplify(expand(lex_to_python(polynomial))))))
        except: showerror("Ошибка многочлена", f"Нельзя упростить многочлен: {polynomial}")
    return ""


@cache
def alg_progressive(d, n):
    if d != "" and n != "":
        try: return str(1 + eval(lex_to_python(d)) * (eval(lex_to_python(n)) - 1))
        except: showerror("Ошибка прогрессии", f"Нельзя вычислить прогрессию: d = {d}, n = {n}")
    return ""


@cache
def geom_progressive(d, n):
    if d != "" and n != "":
        try: return str(eval(lex_to_python(d)) ** (eval(lex_to_python(n)) - 1))
        except: showerror("Ошибка прогрессии", f"Нельзя вычислить прогрессию: d = {d}, n = {n}")
    return ""


@cache
def solve_eq(right, left):
    if right != "" and left != "":
        try: return "; ".join(map(str, solve("(" + lex_to_python(right) + ")-(" + lex_to_python(left) + ")", Symbol("x"))))
        except: showerror("Ошибка уравнения", f"Нельзя решить уравнение: {left + ' = ' + right}")
    return ""


@cache
def formula_md(formula, fnm, geterr = True):
    fnums = fnm.replace(" ", "")
    if formula != "" and fullmatch(".*(.*;)*", fnums) and fnums != "":
        try:
            n = list(map(lambda el: eval(lex_to_python(el)), fnums.split(";")))
            new = lex_to_python(formula)
            syms = list(set(filter(lambda el: el in list("abcdefghijklmnopqrstuvwxyz"), lex_to_python(formula))))
            for i in range(len(syms)):
                try: new = new.replace(syms[i], "(" + str(n[i]) + ")")
                except IndexError:
                    if geterr: showerror("Ошибка подстановки", f"Слишком мало значений: {fnm}")
            return eval(new)
        except:
            if geterr: showerror("Ошибка подстановки", f"Нельзя подставить значения в формулу: {fnm}")
    return ""