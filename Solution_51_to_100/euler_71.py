#!/usr/bin/python -Wall
# -*- coding: utf-8 -*-
"""
<div id="content">
<div style="text-align:center;" class="print"><img src="images/print_page_logo.png" alt="projecteuler.net" style="border:none;" /></div>
<h2>Ordered fractions</h2><div id="problem_info" class="info"><h3>Problem 71</h3><span>Published on Friday, 4th June 2004, 06:00 pm; Solved by 17354; Difficulty rating: 10%</span></div>
<div class="problem_content" role="problem">
<p>Consider the fraction, <i>n/d</i>, where <i>n</i> and <i>d</i> are positive integers. If <i>n</i>&lt;<i>d</i> and HCF(<i>n,d</i>)=1, it is called a reduced proper fraction.</p>
<p>If we list the set of reduced proper fractions for <i>d</i> &le; 8 in ascending order of size, we get:</p>
<p style="text-align:center;font-size:90%;">1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, <b>2/5</b>, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8</p>
<p>It can be seen that 2/5 is the fraction immediately to the left of 3/7.</p>
<p>By listing the set of reduced proper fractions for <i>d</i> &le; 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.</p>
</div><br />
<br /></div>
"""
MAXNUM=1000001
n = 3
d = 7
on = 2
od = 5

for i in range(7, MAXNUM):
    if (i%7 == 0):
        continue
    r = (i * n)/d
    if (r * od) > (on * i):
        on = r 
        od = i

#print on, od
print on

