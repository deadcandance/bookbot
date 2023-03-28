with open ("books/frankenstein.txt", "a+") as myfile:
    myfile.write ("\n""FUCK YOU"*100)
  
with open ("books/frankenstein.txt") as myfile:
    print(myfile.read())
    
    
    