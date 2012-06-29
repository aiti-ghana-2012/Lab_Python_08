import re

# find the word pretty
def hasPretty(inp):
    return re.search(r'pretty', inp) != None
print hasPretty('i am pretty so yeah')
print hasPretty('i am not that ahhh')
    
def whichPet(inp):
    result = re.search(r'pet (cat|dog)', inp)
    if result == None:
        return None
    return result.group(1)
print whichPet('my pet cat')
print whichPet('my pet dog was cool')
print whichPet('my pet donkey')


def getAdjs(inp):
    return re.findall(r'\w+y', inp)
    #return re.findall(r'[a-zA-Z0-9_]+y', inp) # the same thing
    #return re.findall(r'\w{1,}y', inp) # the same thing
print getAdjs('the funny book was goofy')