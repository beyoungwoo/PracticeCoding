#!/usr/bin/python -Wall
# -*- coding: utf-8 -*-
"""
<div id="content">
<div style="text-align:center;" class="print"><img src="images/print_page_logo.png" alt="projecteuler.net" style="border:none;" /></div>
<h2>Maximum path sum II</h2><div id="problem_info" class="info"><h3>Problem 67</h3><span>Published on Friday, 9th April 2004, 06:00 pm; Solved by 60468; Difficulty rating: 5%</span></div>
<div class="problem_content" role="problem">
<p>By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.</p>
<p style="text-align:center;font-family:courier new;font-size:12pt;"><span style="color:#ff0000;"><b>3</b></span><br />
<span style="color:#ff0000;"><b>7</b></span> 4<br />
2 <span style="color:#ff0000;"><b>4</b></span> 6<br />
8 5 <span style="color:#ff0000;"><b>9</b></span> 3</p>
<p>That is, 3 + 7 + 4 + 9 = 23.</p>
<p>Find the maximum total from top to bottom in <a href="project/resources/p067_triangle.txt">triangle.txt</a> (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.</p>
<p class="note"><b>NOTE:</b> This is a much more difficult version of <a href="problem=18">Problem 18</a>. It is not possible to try every route to solve this problem, as there are 2<sup>99</sup> altogether! If you could check one trillion (10<sup>12</sup>) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)</p>
</div><br />
<br /></div>
"""

f=open('67.dat', 'r')
Tri=[]
for line in f:
    Tri.append(map(int, line.split()))

rTri = Tri[::-1]
l = len(rTri)
for i in range(0, l-1):
    for j in range(0, len(rTri[i])-1):
        rTri[i+1][j] += max(rTri[i][j], rTri[i][j+1])

print rTri[l-1]
