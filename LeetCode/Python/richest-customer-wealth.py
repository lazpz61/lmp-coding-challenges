"""
You are given an m x n integer grid accounts where accounts[i][j] is 
the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth
"""
class Solution:
  def maximumWealth (self, accounts):
      res, curr= 0, 0
      for w in accounts:
          for c in w:
            curr+=c
            res=max(res,curr)
          curr=0
      return res


maximumWealth([1,2,3],[3,4,5],[3,3,3])