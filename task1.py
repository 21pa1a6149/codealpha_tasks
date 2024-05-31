import random
class hangGame:
    def __init__(self) -> None:
        with open("hangman game words.txt","r") as file:
                word = file.read().splitlines()
        self.w = list(random.choice(word))
        print("WELCOME TO HANGMAN GAME")
        
    def begin(self):
        self.leng = len(self.w)
        self.list = []
        for i in range(self.leng):
            self.list.append("_")
        print(''.join(self.w))    
        print(" ".join(self.list))   
    
    def guess(self): 
        c=0
        j=0
        while(c<5 and j<self.leng):
            
            g = (input("Guess the word:")).lower()
            if(g in self.w):   
                     
                for i in range(0,self.leng):
                    
                    if (self.w[i].lower()==g):
                        
                        self.list.pop(i)
                        self.list.insert(i,g)
                        j+=1
                print(" ".join(self.list))
                      
            else:
                c+=1  
                print(f"more {5-c} chances left")  
                
                
        if(c==5):
            print("Game over")
            print("You lose")
            print(''.join(self.w))
        else:
            print("Game over")
            print("you win")
            print(''.join(self.w))                
            
hg = hangGame()  
hg.begin() 
hg.guess()         
 # type: ignore