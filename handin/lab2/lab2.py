#!/usr/bin/env python
#encoding: utf-8

import sys, math




def Q1(C):
    """
    Question 1
    """
    C = float(raw_input())

    F = (9. * C / 5.)  +  32.

    return F




def Q2(F):
    """
    Question 2
    """
    F = float(raw_input())
    
    C = ( F  -  32. ) * 5. / 9.
    
    return C




def Q3(s):
    """
    Question 3
    """
    s = float(raw_input())
    
    return s * s




def Q4(l, w):
    """
    Question 4
    """
    l = float(raw_input())
    w = float(raw_input())
    
    return l * w




def Q5(h, b):
    """
    Question 5
    """
    h = float(raw_input())
    b = float(raw_input())
    
    return h * b / 2.




def Q6(a, b):
    """
    Question 6
    """
    a = float(raw_input())
    b = float(raw_input())
    
    return math.sqrt(a * a  +  b * b)




def Q7(r):
    """
    Question 7
    """
    r = float(raw_input())
    
    return 2. * math.pi * r




def Q8(r):
    """
    Question 8
    """
    r = float(raw_input())
    
    return math.pi * r * r




def Q9(n, d):
    """
    Question 9
    """
    n = int(raw_input())
    d = int(raw_input())
    
    return float(n) / float(d)




def Q10(a, b, c):
    """
    Question 10
    """
    a = float(raw_input())
    b = float(raw_input())
    c = float(raw_input())
    
    return ( a + b + c ) / 3.




def Q11(a, b):
    """
    Question 11
    """
    a = int(raw_input())
    b = int(raw_input())
    
    return a + b
    
    return a * b
    
    return a % b




def Q12(s, e, sf, ef):
    """
    Question 12
    """
    s = float(raw_input())
    e = float(raw_input())
    
    sf = float(raw_input())
    ef = float(raw_input())
    
    return (sf - ef) / (e - s)




def Q13(c):
    """
    Question 13
    """
    c = float(raw_input())
    u = c / 1.12
    
    
    return "%.2f" % u




def Q14(h, w):
    """
    Question 14
    """
    h = float(raw_input())
    w = float(raw_input())
    index = w / ( h * h )
    
    return "%.1f"   %   index




def Q15(L):
    """
    Question 15
    """
    L = float(raw_input())
    
    return 1.34 * math.pow(L, 0.5)




def Q16(sg, eg, days):
    """
    Question 16
    """
    sg = float(raw_input())
    eg = float(raw_input())
    
    days = int(raw_input())
    
    return "%.2f" % (  ((eg - sg) * 0.01433  +  days * 0.0902) * 1.05  )




def Q17(P, R, t):
    """
    Question 17
    """
    P = int(raw_input())
    
    R = float(raw_input())
    R = R / 12.
    
    t = int(raw_input())
    T = float(t) * 12.
    
    return "%.2f"  %  ( ( P * R * math.pow(1 + R, T) ) / ( math.pow(1 + R, T) - 1 ) )




def main():
    """
    Main function
    """
    Q = {"q1": Q1,   "q2": Q2,   "q3": Q3,   "q4": Q4,   "q5": Q5,   "q6": Q6,
         "q7": Q7,   "q8": Q8,   "q9": Q9,   "q10": Q10, "q11": Q11, "q12": Q12,
         "q13": Q13, "q14": Q14, "q15": Q15, "q16": Q16, "q17": Q17}




#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

