# -*- coding: utf-8 -*-



class Tree:
    branches = []
    feuilles = []
    name = "racine"

    def __init_(self, parent=None ,name = "racine"):
        self.parent = parent
        self.name = name

if __name__=="__main__":
    A = Tree()
    