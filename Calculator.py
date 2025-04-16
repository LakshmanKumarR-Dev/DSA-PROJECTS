from collections import deque

cost = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3}

class Stack:
    def __init__(self):
        self.container = deque()
    
    def is_empty(self):
        return len(self.container)==0
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

def is_operand(c):
    return c.isdigit()

def infix_postfix(exp):
    operators = Stack()
    num = deque()
    i = 0
    while i < len(exp):
        if is_operand(exp[i]):
            number = ''
            while i < len(exp) and is_operand(exp[i]):
                number += exp[i]
                i += 1
            num.append(number)
            continue
        elif exp[i] == '(':
            operators.push(exp[i])
        elif exp[i] == ')':
            while (not operators.is_empty() and operators.peek() != '('):
                num.append(operators.pop())
            operators.pop()
        else:
            while(not operators.is_empty() and operators.peek() != '(' and cost[operators.peek()] >= cost[exp[i]]):
                num.append(operators.pop())
            operators.push(exp[i])
        
        i += 1

    while not operators.is_empty():
        num.append(operators.pop())

    return num

def postfix_calculate(num):
    s = Stack()

    for i in num:
        if is_operand(i):
            s.push(int(i))
        else:
            x2 = s.pop()
            x1 = s.pop()
            if i == '+' :
                s.push(x1 + x2)
            elif i == '-' :
                s.push(x1 - x2)
            elif i == '*' :
                s.push(x1 * x2)
            elif i == '/' :
                s.push(x1 / x2)
            elif i == '^' :
                s.push(x1 ** x2)
    
    return s.pop()

import tkinter as tk

window = tk.Tk()
window.title("CALCULATOR")

lk = tk.Entry(window, width = 40, font = ('Arial', 16))
lk.grid(row = 0, column = 0, columnspan = 4)

def click(val):
    cur_exp = lk.get()
    lk.delete(0, tk.END)
    lk.insert(tk.END, cur_exp + val)

def total():
    x = lk.get()
    x = [i for i in x if i != ' ']
    res = postfix_calculate(infix_postfix(x))
    rl.config(text = "Result: " + str(res))

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('+', 4, 1), ('^', 4, 2), ('(', 4, 3),
    (')', 5, 0), ('C', 5, 1), ('=', 5, 2, 2)
]

for (text, row, col, *args) in buttons:
    if text == "=":
        btn = tk.Button(window, text=text, width=12, height=3, command=total)
    elif text == "C":
        btn = tk.Button(window, text=text, width=12, height=3, command=lambda: lk.delete(0, tk.END))
    else:
        btn = tk.Button(window, text=text, width=12, height=3, command=lambda value=text: click(value))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

rl = tk.Label(window, text="Result: ", font=('Arial', 14))
rl.grid(row=6, column=0, columnspan=4)

window.mainloop()