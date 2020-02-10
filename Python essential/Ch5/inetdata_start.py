# 
# Example file for retrieving data from the internet
#
import urllib.request


def main():
  webUrl = urllib.request.urlopen("https://www.google.com/")
  print("The code is : " +str(webUrl.getcode()))
  data = webUrl.read()
  print(data)
if __name__ == "__main__":
  main()
