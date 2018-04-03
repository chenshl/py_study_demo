#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
操作XML有DOM和SAX两种方法。DOM会吧整个XML读入内存，占用内存较大；SAX是流模式，边读边解析占用
内存较小，正常情况下优先考虑SAX
ParserCreate模块的使用
@author: chensl
"""

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print("sax:start_element: %s, attrs: %s" % (name, str(attrs)))

    def end_element(self, name):
        print("sax:end_element: %s" % name)

    def char_data(self, text):
        print("sax:char_data: %s" % text)


if __name__ == "__main__":
    xml = r"""<?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
    </ol>
    """

    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
