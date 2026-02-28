#WordCount.py
#Name: Zane Serhan
#Date: 2/28/2026
#Assignment: Lab6 WordCount

def main():
  while True:

    filename = input("Enter filename (gettysberg.txt or fish.txt): ")
    if filename == "gettysberg.txt" or filename == "fish.txt":
      textFile = open(filename, 'r')
  
      lineCount = 0
      wordCount = 0
      charCount = 0

      for line in textFile:
        lineCount = lineCount + 1
        words = line.split()
        for w in words:
          wordCount = wordCount + 1
        charCount += len(line)

      print("Lines:", lineCount)
      print("Words", wordCount)
      print("Characters including Spaces/Newlines:", charCount )
      
      break

    else:
      print("Error: Invalid filename. Please try again with gettysberg.txt or fish.txt.")
    

if __name__ == '__main__':
  main()
