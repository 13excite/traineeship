#!/usr/bin env python

import subprocess


ps_output = subprocess.Popen(['ps', '-eo', 'vsz'], stdout=subprocess.PIPE).communicate()[0]
ps_output = ps_output.split()[1:]

total_vsz = 0 
for elm in ps_output:
	total_vsz += int(elm)

print total_vsz
