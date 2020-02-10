#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  y = 5
  while(y>0):
    print(y)
    y = y -1


  # define a for loop
  for z in range(5, 10):
    print(z)

  # use a for loop over a collection
  num = [11,12,13,14,15,16] 
  for n in num:
      print(n)
    
  # use the break and continue statements


  #using the enumerate() function to get index 
  num = [11,12,13,14,15,16] 
  for i,n in enumerate(num):
     print(i, n)

if __name__ == "__main__":
  main()
