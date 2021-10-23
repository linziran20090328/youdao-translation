#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time         :       2021/10/17 11:55
# @Author       :       林子然
# @File         :       youdao_translate.py
# @Software     :       Pycharm

import tkinter as tk
from tkinter import ttk
from translate import translate, lang


root = tk.Tk()
root.title('有道翻译')
root.geometry('1000x400')
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0)
frame2 = tk.Frame(root, )
frame2.grid(row=0, column=1)
frame3 = tk.Frame(root)
frame3.grid(row=0, column=2)

def translate_command():
    lang_from, lang_to = combobox.get().split(' » ')[0], combobox.get().split(' » ')[1]
    target = text.get(0.0, tk.END)
    result = translate(lang_from=lang_from, lang_to=lang_to, word=target)

    text2.delete(0.0, tk.END)
    text2.insert('insert', result)


tk.Label(frame2, text='请输入翻译的句子或段落').pack()
string_value = tk.StringVar()
string_value.set('中文 » 英语')
values = tuple(lang.keys())
combobox = ttk.Combobox(
    master=frame1,
    state='readonly',
    textvariable=string_value,
    values=values
)
combobox.pack()

scroll = tk.Scrollbar(frame2)
text = tk.Text(
    master=frame2,
    yscrollcommand=scroll.set,
    width=60
)
scroll.config(command=text.yview)
text.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
tk.Button(frame2, text='开始翻译', command=translate_command).pack(side=tk.BOTTOM)

tk.Label(frame3, text='翻译结果(勿动)').pack()
scroll2 = tk.Scrollbar(frame3)
text2 = tk.Text(
    master=frame3,
    yscrollcommand=scroll2.set,
    width=60
)
scroll2.config(command=text2.yview)
text2.pack(side=tk.LEFT)
scroll2.pack(side=tk.RIGHT, fill=tk.Y)


root.mainloop()