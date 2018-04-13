# Tutorials > 30 Days of Code > Day 13: Abstract Classes
# Build on what you've already learned about Inheritance with this Abstract Classes challenge
#
# https://www.hackerrank.com/challenges/30-abstract-classes/problem
#

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass
# (skeliton_head) ----------------------------------------------------------------------


class MyBook(Book):

    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


# (skeliton_tail) ----------------------------------------------------------------------
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
