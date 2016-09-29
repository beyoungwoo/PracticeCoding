#!/usr/bin/python -Wall
# -*- coding: utf-8 -*-
"""
<div id="content">
<div style="text-align:center;" class="print"><img src="images/print_page_logo.png" alt="projecteuler.net" style="border:none;" /></div>
<h2>Convergents of e</h2><div id="problem_info" class="info"><h3>Problem 65</h3><span>Published on Friday, 12th March 2004, 06:00 pm; Solved by 18247; Difficulty rating: 15%</span></div>
<div class="problem_content" role="problem">
<p>The square root of 2 can be written as an infinite continued fraction.</p>
<div style="margin-left:20px;">
<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td>&radic;2 = 1 +</td>
<td colspan="4" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
</tr>
<tr>
<td>&nbsp;</td>
<td>2 +</td>
<td colspan="3" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>2 +</td>
<td colspan="2" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>2 +</td>
<td style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>2 + ...</td>
</tr>
</table>
</div>
<p>The infinite continued fraction can be written, &radic;2 = [1;(2)], (2) indicates that 2 repeats <i>ad infinitum</i>. In a similar way, &radic;23 = [4;(1,3,1,8)].</p>
<p>It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for &radic;2.</p>
<div style="margin-left:20px;">
<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td>1 +</td>
<td style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>= 3/2</td>
</tr>
<tr>
<td>&nbsp;</td>
<td><div style="text-align:center;">2</div></td>
<td>&nbsp;</td>
</tr>
</table>
<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td>1 +</td>
<td colspan="2" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>= 7/5</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>2 +</td>
<td style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><div style="text-align:center;">2</div></td>
<td>&nbsp;</td>
</tr>
</table>
<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td>1 +</td>
<td colspan="3" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>= 17/12</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>2 +</td>
<td colspan="2" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>2 +</td>
<td style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><div style="text-align:center;">2</div></td>
<td>&nbsp;</td>
</tr>
</table>
<table border="0" cellspacing="0" cellpadding="0">
<tr>
<td>1 +</td>
<td colspan="4" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>= 41/29</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>2 +</td>
<td colspan="3" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>2 +</td>
<td colspan="2" style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>2 +</td>
<td style="border-bottom:1px solid #000;"><div style="text-align:center;">1</div></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td><div style="text-align:center;">2</div></td>
<td>&nbsp;</td>
</tr>
</table>
</div>
<p>Hence the sequence of the first ten convergents for &radic;2 are:</p>
<div class="note">1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...</div>
<p>What is most surprising is that the important mathematical constant,<br /><i>e</i> = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2<i>k</i>,1, ...].</p>
<p>The first ten terms in the sequence of convergents for <i>e</i> are:</p>
<div class="note">2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...</div>
<p>The sum of digits in the numerator of the 10<sup>th</sup> convergent is 1+4+5+7=17.</p>
<p>Find the sum of digits in the numerator of the 100<sup>th</sup> convergent of the continued fraction for <i>e</i>.</p>
</div><br />
<br /></div>
"""

MAXNUM=34
def E65():
    a1=2
    a2=3
    mul = 2
    a3=a2*mul # 6
    for i in range(1, MAXNUM):
        a11=a1+a3
        a22=a11+a2
        a33=a11+a22
#        print [3*i],a11, [3*i+1],a22, [3*i+2],a33
        a1 = a22
        a2 = a33
        mul+=2
        a3 = a33*mul
        if (3*i)+1 == 100:
            ret=str(a22)
            l = len(ret)
            tot = 0
            for i in range(0, l):
                tot+=int(ret[i])

            print tot



    return 0

E65()
