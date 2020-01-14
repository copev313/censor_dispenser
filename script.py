# CENSOR DISPENSOR PROJECT
#Completed as part of Codecademy - Python Challenge Project
#This project censors specified words from emails / text documennts.

#By: E.Cope (Jan. 2020)

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(text, word):
    
    word_length = len(word)
    
    while word in text:
      index = text.find(word)
      censored_txt = text[:index] + '[*****]'
      theRest = text[index+word_length:]
    
      text = censored_txt + theRest
  
    return text
    
#TEST-2 Censors a phrase: 'learning algorithms' from email_one
#print(censor(email_one, 'learning algorithms'))
#-----------------------------------------------------------

def censor_list(text, word_list):
    
    for word in word_list:
      
      word_length = len(word)
    
      while word in text:
        index = text.find(word)
        censored_txt = text[:index] + '[*****]'
        theRest = text[index+word_length:]
    
        text = censored_txt + theRest
  
  return text  
 
#TEST-3 Censors a list of phrases from emails
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#print(email_two)
#print(censor_list(email_two, proprietary_terms))
#---------------------------------------------------------

def censor_neg(text, word_list):
    
    negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
    
    #first censor words from word_list
    for word in word_list:
      
      word_length = len(word)
    
      while word in text:
        index = text.find(word)
        censored_txt = text[:index] + '[*****]'
        theRest = text[index+word_length:]
        text = censored_txt + theRest
      
      #now censor negative words
      count = 0
      for neg in negative_words:
        
        if (count >= 1):
          word_length = len(neg)
    
          while neg in text:
            index = text.find(neg)
            censored_txt = text[:index] + '[*****]'
            theRest = text[index+word_length:]
            text = censored_txt + theRest
              
        elif neg in text:
          count +=1
      
  
    return text 

#TEST-4 Censors second occurance of specified words
#print(email_three)
#print(censor_neg(email_three, proprietary_terms))
#----------------------------------------------------------------
