# Autogenerated with SMOP 
from smop.core import *
# 

    dtFlambda[:,i]=multiply(multiply(scheme(i,4),rho(arange(),1)),(multiply(dot(0.5,(G11 - delta + multiply((multiply(u(arange(),1),u(arange(),1))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,1),scheme(i,1)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(((multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq) - multiply(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)),invcssq) - multiply(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)),invcssq))) + dot(dot(0.5,(G12 + multiply((multiply(u(arange(),1),u(arange(),2))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,1),scheme(i,2)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 1)),invcssq) - multiply(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 2)),invcssq))) + dot(dot(0.5,(G13 + multiply((multiply(u(arange(),1),u(arange(),3))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,1),scheme(i,3)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 1)),invcssq) - multiply(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 3)),invcssq))) + dot(dot(0.5,(G21 + multiply((multiply(u(arange(),2),u(arange(),1))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,2),scheme(i,1)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 2)),invcssq) - multiply(multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 1)),invcssq))) + multiply(dot(0.5,(G22 - delta + multiply((multiply(u(arange(),2),u(arange(),2))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,2),scheme(i,2)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(((multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq) - multiply(multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)),invcssq) - multiply(multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)),invcssq))) + dot(dot(0.5,(G23 + multiply((multiply(u(arange(),2),u(arange(),3))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,2),scheme(i,3)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 2)),invcssq) - multiply(multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 3)),invcssq))) + dot(dot(0.5,(G31 + multiply((multiply(u(arange(),3),u(arange(),1))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,3),scheme(i,1)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 3)),invcssq) - multiply(multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 1)),invcssq))) + dot(dot(0.5,(G32 + multiply((multiply(u(arange(),3),u(arange(),2))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,3),scheme(i,2)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 3)),invcssq) - multiply(multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 2)),invcssq))) + multiply(dot(0.5,(G33 - delta + multiply((multiply(u(arange(),3),u(arange(),3))),invcssq))),(multiply(multiply(multiply(multiply(scheme(i,3),scheme(i,3)),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) - multiply(((multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq) - multiply(multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)),invcssq) - multiply(multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)),invcssq))) + multiply((multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3))),invcssq) + multiply(multiply(multiply((multiply(scheme(i,1),u(arange(),1)) + multiply(scheme(i,2),u(arange(),2)) + multiply(scheme(i,3),u(arange(),3))),(multiply(scheme(i,1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(scheme(i,2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(scheme(i,3),F(arange(),dot(3,(i - 1)) + 3)))),invcssq),invcssq) + multiply(- (multiply(u(arange(),1),F(arange(),dot(3,(i - 1)) + 1)) + multiply(u(arange(),2),F(arange(),dot(3,(i - 1)) + 2)) + multiply(u(arange(),3),F(arange(),dot(3,(i - 1)) + 3))),invcssq)))