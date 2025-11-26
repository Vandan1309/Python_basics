
#
#
#Practical 1
#
#
lines=[]

print("Enter the multiline input: ")
while True:
    string=input()
   
    if string.upper()=='END':
        break
    lines.append(string)

for i in lines:
    print(f"{i.upper()}")
#
#
#Practical 2
#
#
pstring=input("Enter the Parent string: ").lower()
currentchildstring=""
longestchildstring=""

for ch in pstring:
    if ch==" ":
        continue
    if ch in currentchildstring:
        currentchildstring = currentchildstring[currentchildstring.index(ch)+1 :]
    currentchildstring += ch
    if len(currentchildstring) > len(longestchildstring):
        longestchildstring=currentchildstring
         
print(longestchildstring)

#
#
#
#Practical 3
#
#
#
tree = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": None
    },
    "right": {
        "value": 3,
        "left": None,
        "right":{
            "value": 3,
            "left": None,
            "right": None
            }
    }
}

def is_balanced(tree):
    # Helper function that returns (is_balanced, height)
    def check_balance(node):
        if node is None:
            return True, 0  # A null tree is balanced, height = 0

        left_balanced, left_height = check_balance(node.get("left"))
        right_balanced, right_height = check_balance(node.get("right"))

        # Current node is balanced if:
        # - both subtrees are balanced
        # - height difference is at most 1
        balanced = (
            left_balanced and
            right_balanced and
            abs(left_height - right_height) <= 1
        )

        height = 1 + max(left_height, right_height)

        return balanced, height

    balanced, _ = check_balance(tree)
    return balanced

print("Is tree balanced?", is_balanced(tree))  # Output: False









#
#
#
#Practical 4
#
#
#
from functools import lru_cache

@lru_cache(maxsize=128)  # Cache up to 128 distinct results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# First call computes and caches results
print(fibonacci(10))

# Subsequent calls with the same argument use cached results
print(fibonacci(10))

# Get cache statistics
print(fibonacci.cache_info())
#
#
#
#Practical 5
#
#
#
string=input("Enter the string")
letters=space=digit=0
for ch in string:
    if ch==" ":
        space+=1
    if ch.isnumeric():
        digit+=1
    if ch.isalpha():
        letters+=1
        
print(f"Space: {space}, Digits: {digit}, Letters: {letters}")
#
#
#
#Practical 6
#
#
#
conductedclasses=int(input("Enter the number of classes conducted"))
attendedclasses=int(input("Enter the number of classes attended"))
print("The percentage of classes attended is: ", (attendedclasses/conductedclasses)*100)
       
