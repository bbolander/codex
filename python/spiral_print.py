#!/usr/bin/python
#
#   spiral-print.py    
#   
#   Given an m x n matrix print the elements in spiral order
#
# A = [
#       [ 1, 2, 3 ],
#       [ 4, 5, 6 ],
#       [ 7, 8, 9 ]
#     ]
#
#   [1, 2, 3, 6, 9, 8, 7, 4, 5]
#
###############################################################################

A = [
      [1, 2, 3],
      [4, 5, 6]
    ]

A = [
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]

result = []

T = 0               # Top index
B = len(A)          # Bottom index
L = 0               # Left index
R = len(A[0])       # Right index

dir = 0

#print A
#print "B: " + str(B) + " R: " + str(R)

while(T <= (B - 1) and L <= (R - 1)):
   if dir == 0:
      for i in range(L, R):
         #print "i: " + str(i) + " T: " + str(T) + " Value: " + str(A[T][i])
         result.append(A[T][i])
      T += 1
      dir = 1
   elif dir == 1:
      for i in range(T, B):
         #print "i: " + str(i) + " R: " + str(R) + " Value: " + str(A[i][R - 1])
         result.append(A[i][R - 1])
      R -= 1
      dir = 2
   elif dir == 2:
      for i in range(R - 1, L - 1, -1):
         #print "i: " + str(i) + " B: " + str(B) + " Value: " + str(A[B - 1][i])
         result.append(A[B - 1][i])
      B -= 1
      dir =3
   elif dir == 3:
      for i in range(B - 1, T - 1, -1):
         #print "i: " + str(i) + " L: " + str(L) + " Value: " + str(A[i][L])
         result.append(A[i][L])
      L += 1
      dir = 0


print "Result: "
print result


