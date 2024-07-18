# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:46:50 2024

@author: marku
"""

"""

Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, 
which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability 
(range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, 
and frequency distribution of the sample. You can create a class called Statistics and create all the functions
that do statistical calculations as methods for the Statistics class. Check the output below.

"""
# A self written statistics class
class Statistics:
    # init method or constructor
    def __init__(self, list=[0,1,2,3]):
        # self.test = list_in
        self.distribution = list
    
    # max Method
    def max(self):
        return max(self.distribution)

    # min Method
    def min(self):
        return min(self.distribution)

    # mean Method
    def mean(self):
        return sum(self.distribution)/len(self.distribution)
    
    # median Method
    def median(self):
        self.distribution.sort()
        if len(self.distribution)%2 ==0:
           return (self.distribution[len(self.distribution)//2-1] + self.distribution[len(self.distribution)//2]) /2
        else:
            return self.distribution[len(self.distribution)//2]
        
        #change to percentile(self,percentile_in=50)
        
    # mode Method
    def mode(self):
        return max(set(self.distribution), key=self.distribution.count)
        
    def findYPoint(xa,xb,ya,yb,xc):
        m = (ya - yb) / (xa - xb)
        return (xc - xb) * m + yb

    # percentile Method
    def percentile(self,percentile_in=50):
        # something doesn't work here!!
        # self.distribution.sort()
        # idx_1 = percentile_in * len(self.distribution) // 100 
        # idx_2 = idx_1 + 1
        # y1 = self.distribution[idx_1]
        # y2 = self.distribution[idx_2]
        # x1 = idx_1*100/len(self.distribution)
        # x2 = idx_2*100/len(self.distribution)
        # m = (y2 - y1) / (x2 - x1)
        # b = y1 - m * x1
        # return (percentile_in) * m + b
        import numpy as np
        return np.percentile(self.distribution, percentile_in)
  
        
    # count Method
    def count(self):
        return len(self.distribution)
    
    # range Method
    def range(self):
        return max(self.distribution)-min(self.distribution)
    
    # variance Method
    def var(self):
        
        return sum((self.distribution-self.mean())**2)/(len(self.distribution))
    
    # standard deviation Method
    def std(self):
        import math
        return math.sqrt(self.var())
    
    # frequency distribution Method
    def frequency(self):
        # I don't understand why this is not sorted!!
        return [(i, self.distribution.count(i)) for i in set(self.distribution)]
        
    
        
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

p = Statistics([ages[:4]])

#%%%

"""
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income,
total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its
description. The same goes for expenses.
 
"""

# could do it but it's getting late. 
# Also more info missing !
class PersonAccount:
     # init method or constructor
     def __init__(self,firstname, lastname, incomes, expenses, properties):
         # self.test = list_in
         self.distribution = list
         self.firstname = firstname
         self.lastname = lastname 
         self.incomes = incomes
         self.expenses = expenses
         self.properties = properties
         
         def  total_income(self):
             return 'WIP'
         
         def total_expense(self):
             return 'WIP'

         def account_info(self):
             return 'WIP'

         def add_income(self):
             return 'WIP'

         def add_expense(self):
             return 'WIP'

         def account_balance(self):
             return 'WIP'

         