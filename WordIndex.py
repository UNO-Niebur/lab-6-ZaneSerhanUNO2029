#WordIndex.py
#Name: Zane Serhan
#Date: 2/28/2026
#Assignment: Lab6 WordIndex

def main():
  while True:

    filename = input("Enter filename (gettysberg.txt or fish.txt): ")
    if filename == "gettysberg.txt" or filename == "fish.txt":
      textFile = open(filename, 'r')
  
      words = {} #create an empty dictionary
      lineNum = 0
      for line in textFile:
        lineNum = lineNum + 1
        wordList = line.split()
        for w in wordList:
          w = w.lower()
          w = w.replace("," , "")
          w = w.replace("." , "")
          w = w.replace("!" , "")
          if w in words:
            if lineNum not in words[w]:
              words[w].append(lineNum)
          else:
            words[w] = [lineNum]

      for word in words:
        print(word, words[word])

      break
    else:
      print("Error: Invalid filename. Please try again with gettysberg.txt or fish.txt.")
 

if __name__ == '__main__':
  main()
