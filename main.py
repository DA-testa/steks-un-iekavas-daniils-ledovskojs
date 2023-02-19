# python 3
# 221RDB300 Daniils Ledovskojs 2. grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))
            

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1  
            opening_brackets_stack.pop()  
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
    return "Success"

def main():
    text = input()
    
    if text == "F":
        way_to_file = input("way to file:")
        with open("input.txt", "r") as f:
            text2 = f.read()
            mismatch = find_mismatch(text2)
            if mismatch == 'Success':
                print("Succes")
            else:
                print(mismatch)

    else:
        if "I" in text:
            text2 = input()
            mismatch = find_mismatch(text2)
            print(mismatch)
   



if __name__ == "__main__":
    main()
