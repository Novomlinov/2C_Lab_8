#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def first(tag):
    def second(s):
        group = tag, s
        return group

    return second


if __name__ == "__main__":
    A = input("Введите тег ")
    B = input("Введите содержимое строки ")
    print(first(A)(B))