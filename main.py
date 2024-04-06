masya= "masya"
nazar = "nazar"
#create anti semitism test
def antiSemitismTest(name) : 
    if (name == masya): 
        print(f"{name} really hates jewish people. \nFAIL")
    else: 
        print(f"{name} really likes the jewish community. \nPASS")      

#demo 

antiSemitismTest(masya)