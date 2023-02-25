with open("books/frankenstein.txt") as f:
    file_contents = f.read ()
     #make words lower case with method: .lower()
    text = file_contents.lower()
    print (text)
   
    print ("***********EVERY WORD IS NOW LOWERCASE************")
    new_text= text.split()
    print (new_text)
    print ("EVERY STRING HAS BEEN PARSED")
    print ("NUMBER OF WORDS IN THIS TEXT: ", len (file_contents.split()))
    
    
    #thisdict = dict (words)
    #for words in thisdict:
        #print (thisdict)
    
    
    #
    
    #print {words}
    
    #words = file_contents.lower()
    #print (words)





