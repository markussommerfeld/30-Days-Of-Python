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
           return (self.distribution[len(self.distribution)//2-1] + self.distribution[len(self.distribution)//2+1]) /2
        else:
            return self.distribution[len(self.distribution)//2]
        
    # mode Method
    def mode(self):
        return max(set(self.distribution), key=self.distribution.count)
        
    # percentile Method
    def percentile(self,percentile_in=50):
        self.distribution.sort()
        idx = round(len(self.distribution)*percentile_in/100)
        return self.distribution[idx]
        
    # count Method
    def count(self):
        return len(self.distribution)
    
    # range Method
    def range(self):
        return max(self.distribution)-min(self.distribution)
    
    # variance Method
    def var(self):
        return 'WIP'
    
    # standard deviation Method
    def std(self):
        return 'WIP'
    
    # frequency distribution Method
    def frequency(self):
        return 'WIP'
        
    
        
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

p = Statistics([ages[:4]])

#%%%

"""
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income,
total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its
description. The same goes for expenses.
 
"""