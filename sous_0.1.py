#-------------------------------------------------------------------------------
# Name:         Sous
# Version:      0.1
# Purpose:      Load meals from Json files and parse to create relevant objects
#
# Author:       Dave
#
# Created:      10/02/2013
# Copyright:    (c) Dave 2013
# Licence:      <Hands off!>
#-------------------------------------------------------------------------------


from pprint import pprint       #Pretty Print
from data_structures import *   #Task & Meal classes, associated functions

from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search



def main():

    meals = []
    dir1 = "meal1.json"
    dir2 = "meal2.json"
    meals.append(load_meal_from_file(dir1, printYN=True))
    meals.append(load_meal_from_file(dir2))

    print meals[1].to_string()

    pprint (meals[1].graph, width=40)
    pprint (meals[0].graph)


    #pass

if __name__ == '__main__':
    main()
