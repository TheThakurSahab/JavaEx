# Write your solution below:
a_string = "ABC"
print("a_string is: ",a_string)
print(a_string) # This should print ABC.


b_string = "DEF"

print("b_string's second character is: (should be E)")
# Write your solution below:
print(b_string[1])

c_string = "GHI"
# Write your solution below:

print("Your solution should have printed G, H, and I.")
for character in c_string:
    print(character)

# Modify the following function:
def are_reverses(string_1, string_2):
    for i in range(len(string_1)):
        i_2 = len(string_2) - i - 1
        if string_1[i] != string_2[i_2]:
            return False
    return True

print('Are "ABC" and "CBA" reverses of each other? (Should be True.)')
are_reverses("ABC", "CBA")

print('Are "CBA" and "AAA" reverses of each other? (Should be False.)')
are_reverses("CBA", "AAA")