#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import re

string = 'hellomypythonhistorypthon123pythontm'
pattern = re.compile('.python.') #预编译
result = pattern.findall(string)
print(result)