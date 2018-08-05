#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  vinput.py
#  
#  Copyright 2018 Tomáš Votava <info@tomasvotava.eu>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

"""
VInput 1.1
Simple console input with validation and (TODO: optional) color feedback.

USAGE:
from vinput import vinput, VALID_LIST
answer = vinput("Do you want to quit smoking?",default=None,validation=VALID_LIST,options=["yes","no"])
print("You answered %s."%answer)
"""

try:
	from pformat import pprint, pinput
except ImportError:
	print("This module requires pformat to work. This will hopefully change in the future.")

VALID_VALID		= 0
VALID_NONEMPTY	= 1
VALID_NUMBER	= 2
VALID_FLOAT		= 4
VALID_LIST		= 8

def vinput(prompt,default=None,validation=VALID_VALID,options=[]):
	e = VALID_VALID
	done = False
	i = ""
	while not done:
		if (e & VALID_NONEMPTY):
			pprint(":bwhite::red:Cannot be empty.")
		if (e & VALID_NUMBER):
			pprint(":bwhite::red:Integer numbers only.")
		if (e & VALID_FLOAT):
			pprint(":bwhite::red:Floating point numbers only.")
		if (e & VALID_LIST):
			pprint(":bwhite::red:Choose from list of values only.")
		if (validation & VALID_LIST) and len(options)>0:
			dstring = "/".join(options)
		elif (validation & VALID_LIST) and len(options)==1:
			dstring = options[0]
		else:
			dstring = default if default!= None else ""
		pprompt = ":cyan:%s :-::bold:[%s]: "%(prompt,(dstring))
		i = pinput(pprompt).strip()
		if validation & VALID_VALID: return i
		if (validation & VALID_NONEMPTY) and (i==""):
			e = VALID_NONEMPTY
			continue
		if (validation & VALID_NUMBER):
			if i=="": i = default
			try: int(i)
			except ValueError:
				e = VALID_NUMBER
				continue
		if (validation & VALID_FLOAT):
			try: float(i)
			except ValueError:
				e = VALID_FLOAT
				continue
		if (validation & VALID_LIST) and (i.lower() not in list(map(str.lower,options))):
			e = VALID_LIST
			continue
		done = True
		break
	if (i==""): i = default
	return i
