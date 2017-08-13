# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def computeWi1D(Q=None,velocities=None,T0=None,*args,**kwargs):
    varargin = computeWi1D.varargin
    nargin = computeWi1D.nargin

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
    
    if size(velocities,1) == 1:
        velocities=velocities.T
    
    u=0
    T0sqrt=sqrt(T0)
    M=zeros(Q,1)
    vQ=zeros(Q,Q)
    for i in arange(0,Q - 1).reshape(-1):
        M[i + 1]=evaluatenormaldistmthmoment(i,u,T0sqrt)
        vQ[i + 1,:]=velocities.T ** i
    
    W=numpy.linalg.solve(vQ,M)
    return W