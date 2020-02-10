#
# Example file for working with conditional statements
#

def main():
  x, y = 100, 100
  
  # conditional flow uses if, elif, else  
  if (x<y):
   st="X is less than Y"
  elif (x==y):
    st = "X is equal to Y"
  else:
   st="X is grater than Y"
  print(st)
  # conditional statements let you use "a if C else b"
  st = "x is less than y" if (x < y) else "x is greater than or equal to y"
  print (st)

if __name__ == "__main__":
  main()
