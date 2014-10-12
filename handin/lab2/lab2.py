#!/usr/bin/env python
#encoding: utf-8

import sys, math




def Q1(C):
    """
    Question 1
    """
    F = (9. * C / 5.)  +  32.

    return F




def Q2(F):
    """
    Question 2
    """
    C = ( F  -  32. ) * 5. / 9.
    
    return C




def Q3(s):
    """
    Question 3
    """
    return s * s




def Q4(l, w):
    """
    Question 4
    """
    return l * w




def Q5(h, b):
    """
    Question 5
    """
    return h * b / 2.




def Q6(a, b):
    """
    Question 6
    """
    return math.sqrt(a * a  +  b * b)




def Q7(r):
    """
    Question 7
    """
    return 2. * math.pi * r




def Q8(r):
    """
    Question 8
    """
    return math.pi * r * r




def Q9(n, d):
    """
    Question 9
    """
    return float(n) / float(d)




def Q10(a, b, c):
    """
    Question 10
    """
    return ( a + b + c ) / 3.




def Q11(a, b):
    """
    Question 11
    """
    return (a + b),  (a * b), (a % b)




def Q12(s, e, sf, ef):
    """
    Question 12
    """
    return (sf - ef) / (e - s)




def Q13(c):
    """
    Question 13
    """
    u = c / 1.12
    
    return "%.2f" % u




def Q14(h, w):
    """
    Question 14
    """
    index = w / ( h * h )
    
    return "%.1f"   %   index




def Q15(L):
    """
    Question 15
    """
    return 1.34 * math.pow(L, 0.5)




def Q16(sg, eg, days):
    """
    Question 16
    """
    return "%.2f" % (  ((eg - sg) * 0.01433  +  days * 0.0902) * 1.05  )




def Q17(P, R, t):
    """
    Question 17
    """
    R = R / 12.
    T = float(t) * 12.
    return "%.2f"  %  ( ( P * R * math.pow(1 + R, T) ) / ( math.pow(1 + R, T) - 1 ) )




def main():
    """
    Main function
    """
    # map of functions, number and types of their arguments
    targs = {"q1":  [Q1,  1, [float]],
             "q2":  [Q2,  1, [float]],
             "q3":  [Q3,  1, [float]],
             "q4":  [Q4,  2, [float, float]],
             "q5":  [Q5,  2, [float, float]],
             "q6":  [Q6,  2, [float, float]],
             "q7":  [Q7,  1, [float]],
             "q8":  [Q8,  1, [float]],
             "q9":  [Q9,  2, [int, int]],
             "q10": [Q10, 3, [float, float, float]],
             "q11": [Q11, 2, [int, int]],
             "q12": [Q12, 4, [float, float, float, float]],
             "q13": [Q13, 1, [float]],
             "q14": [Q14, 2, [float, float]],
             "q15": [Q15, 1, [float]],
             "q16": [Q16, 3, [float, float, int]],
             "q17": [Q17, 3, [int, float, int]]}

    # get a function name from 'argv'
    if len(sys.argv) - 1 == 0:
        sys.stderr.write("Need to supply a question, e.g. \"q1\", \"q2\", ...\n")
        exit(1)
    request = sys.argv[1]

    if request not in targs:
        sys.stderr.write("Unrecognized function: `%s'\n" % request)
        exit(1)



#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

