class Solution:
  def reverse(self, x: int) -> int:

     if x == 0:
        return x
     string = str(x)
     string2 = ""
     if(x < 0):
        string2 = string[0] + (string[1:])[::-1]
     else:
        string2 = string[::-1]
     value  = int(string2)
     if value < -1 * pow(2,31) or value > pow(2,31) -1:
         return 0
     else :
         return value
