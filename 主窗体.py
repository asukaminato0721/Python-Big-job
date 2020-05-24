"""
Copyright (c)2020
All rights reserved.
文件名称：主窗体.py
摘    要：大作业
当前版本：1.0
作    者：wuyudi
完成日期：2020 年 05 月 18 日 星期一
"""
from tkinter import *
from tkinter import messagebox
from 绘图 import query
# from 查询 import query
窗口 = Tk()
窗口.title("疫情统计")
输入区 = LabelFrame(窗口, text="输入区")
输入区.grid(padx=30, pady=30)
按钮区 = LabelFrame(窗口, text="按钮区")
按钮区.grid(padx=30, pady=20)
分隔符 = [
    Label(输入区, text="/"),
    Label(输入区, text="/"),
    Label(输入区, text="/"),
    Label(输入区, text="/")
]
time1 = Label(输入区, text="请输入你想查询的起始时间: ").grid(row=1, column=0)
time2 = Label(输入区, text="请输入你想查询的终止时间: ").grid(row=2, column=0)
year1 = StringVar()
year1.set("2020")
year1选项 = OptionMenu(输入区, year1, "2020")
year1选项.grid(row=1, column=1, ipadx=10)
分隔符[0].grid(row=1, column=2)
year2 = StringVar()
year2.set("2020")
year2选项 = OptionMenu(输入区, year2, "2020")
year2选项.grid(row=2, column=1, ipadx=10)
分隔符[1].grid(row=1, column=4)
month1 = StringVar()
month1.set("1")
month1选项 = OptionMenu(输入区, month1, *map(str, range(1, 13)))
month1选项.grid(row=1, column=3, ipadx=10)
分隔符[2].grid(row=2, column=2)
month2 = StringVar()
month2.set("1")
month2选项 = OptionMenu(输入区, month2, *map(str, range(1, 13)))
month2选项.grid(row=2, column=3, ipadx=10)
分隔符[3].grid(row=2, column=4)
day1 = StringVar()
day1.set("1")
day1选项 = OptionMenu(输入区, day1, *map(str, range(1, 32)))
day1选项.grid(row=1, column=5, ipadx=10)
day2 = StringVar()
day2.set("1")
day2选项 = OptionMenu(输入区, day2, *map(str, range(1, 32)))
day2选项.grid(row=2, column=5, ipadx=10)

类型 = StringVar()
类型.set("确诊")
类型选项 = OptionMenu(窗口, 类型, "确诊", "疑似", "死亡")
类型选项.grid(row=0, column=5, ipadx=10)

结果 = Entry(窗口, width=75)
结果.grid(column=0, row=4, columnspan=6)


def 按键触发():
    text = "查询" + "从 " + year1.get()+" 年 " + month1.get()+" 月 "+day1.get()+" 日 " +\
        "到 " + year2.get()+" 年 " + month2.get()+" 月 "+day2.get()+" 日 " + 类型.get()+"人数"
    response = messagebox.askyesno("确认", "是否要"+text+"?")
    if response:
        结果.delete(0, END)
        结果.insert(0, text)
        query(3)
        # query(year1.get(),month1.get(),day1.get(),year2.get(),month2.get(),day2.get())


def 清除输入():
    response = messagebox.askyesno("确认", "是否要清除")
    # https://stackoverflow.com/questions/23584325/cannot-use-geometry-manager-pack-inside
    if response:
        year1.set("2020")
        year2.set("2020")
        month1.set("1")
        month2.set("1")
        day1.set("1")
        day2.set("1")


def 关闭():
    response = messagebox.askyesno("确认", "是否要关闭界面?")
    if response:
        窗口.quit()


按钮 = Button(按钮区, text="开始查询", padx=20, pady=20, command=按键触发)
按钮.grid(row=3, column=1)
清除 = Button(按钮区, text="清除输入", padx=20, pady=20, command=清除输入)
清除.grid(row=3, column=3)
退出 = Button(按钮区, text="退出", padx=20, pady=20, command=关闭)
退出.grid(row=3, column=5)


成员名单 = {6: "窗体: 吴宇迪", 7: "xx: xxx", 8: "xx: xxx", 9: "xx: xxx", 10: "xx: xxx"}


for (位置, 成员) in 成员名单.items():
    Label(窗口, text="制作人员名单").grid(column=0, row=5, columnspan=5)
    Label(窗口, text=成员).grid(column=0, row=位置, columnspan=5)


窗口.mainloop()
