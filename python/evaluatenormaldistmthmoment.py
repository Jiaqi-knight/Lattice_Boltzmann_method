# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def evaluatenormaldistmthmoment(m=None,mu=None,sigma=None,*args,**kwargs):
    varargin = evaluatenormaldistmthmoment.varargin
    nargin = evaluatenormaldistmthmoment.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: May 27th, 2014
#    Last update: May 27th, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    ##
    
    n=floor(m / 2)
    M=0
    if dot(2,n) == m:
        for i in arange(0,n).reshape(-1):
            M=M + multiply(dot(dot(binomialfactor(dot(2,n),dot(2,i)),normaldistcoeff(dot(2,n) - dot(2,i))),(sigma ** (dot(2,n) - dot(2,i)))),(mu ** (dot(2,i))))
    else:
        for i in arange(0,n).reshape(-1):
            M=M + multiply(dot(dot(binomialfactor(dot(2,n) + 1,dot(2,i) + 1),normaldistcoeff((dot(2,n) + 1) - (dot(2,i) + 1))),(sigma ** ((dot(2,n) + 1) - (dot(2,i) + 1)))),(mu ** (dot(2,i) + 1)))
    
    return M