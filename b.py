#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s获取成绩为:%s' % (self.name, self.score))

    def get_grade(self):
        if self.score > 85:
            print('A')
        elif self.score > 60:
            print('B')
        else:
            print('c')

abart=Student('MBA', 95)
adam=Student('CTU', 65)

abart.print_score()
adam.print_score()

abart.get_grade()
adam.get_grade()

