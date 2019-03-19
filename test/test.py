#-*- coding:utf-8 -*-
import difflib
a_text = """jhfhj
            fgh
            gh"""
b = """"""
with open(r'D:\gitDir\1768\test.html',"w+") as f:
    ae =  difflib.HtmlDiff.make_file(difflib.HtmlDiff(),a_text,b)
    f.write(ae)
