#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      ZWW
#
# Created:     20/01/2014
# Copyright:   (c) ZWW 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
import codecs

a={u"哈哈^_^": 121}
b=json.dumps(a, ensure_ascii=False)
file = codecs.open("test.txt", "w", "utf-8")
file.write(b)
file.close()

