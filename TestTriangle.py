# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""
import unittest
from datetime import date
from Triangle import classifyTriangle

def my_brand():
    print("=*=*=*= Eshan Sharma =*=*=*=\n")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*= \n")
    print("=*=*=*= HW 02a - Testing a legacy program and reporting on testing results  =*=*=*= \n")
    print("=*=*=*=", date.today(), "=*=*=*= \n")

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a scalene triangle')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(2,2,3),'Isoceles','2,2,3 is a isoceles triangle')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,100,1),'NotATriangle','1,100,1 is not a triangle')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(1,1,0),'InvalidInput','1,1,0 is an invalid input')
    
    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(1,1,201),'InvalidInput','1,1,201 is an invalid input')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(1,1,-1),'InvalidInput','1,1,-1 is an invalid input')

    def testInvalidInput4(self):
        self.assertEqual(classifyTriangle(1,1,0.1),'InvalidInput','1,1,0.1 is an invalid input')

my_brand()

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()