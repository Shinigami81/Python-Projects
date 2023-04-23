import random
num=random.randint(0,8)
domanda=input("Ask me whatever you want:\n")
def palla_8():
    if num == 0:
        return "Yes, of course."
    elif num == 1:
        return "It's definitely like that."
    elif num == 2:   
        return "no doubt."  
    elif num == 3:
        return "Confusing question, please try again."
    elif num == 4:
        return "Ask me later."        
    elif num == 5:
        return "I better not tell you."    
    elif num == 6:
        return "My sources say no."
    elif num == 7:
        return "I doubt about it."    
    elif num == 8:
        return "Are you crazy ?"
           

print(palla_8())
