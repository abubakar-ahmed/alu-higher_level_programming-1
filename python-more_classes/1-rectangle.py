#!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
"""


class Rectangle:
    """A Rectangle class with attributes  width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
