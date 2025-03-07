import re

#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
def match_string(s):
    pattern = r"^ab*$"
    if re.match(pattern, s):
        return True
    else:
        return False

test_strings = ["a", "ab", "abb", "abbb", "ba", "abc", "b", "aaa"]

for s in test_strings:
    if match_string(s):
        print(f"'{s}' matches the pattern.")
    else:
        print(f"'{s}' does not match the pattern.")

#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
print()
def match_string1(s):
    pattern = r"^ab{2,3}$"
    if re.match(pattern, s):
        return True
    else:
        return False

test_strings = ["a", "ab", "abb", "abbb", "ba", "abc", "b", "aaa"]

for s in test_strings:
    if match_string1(s):
        print(f"'{s}' matches the pattern.")
    else:
        print(f"'{s}' does not match the pattern.")

print()

#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
def find_sequences(s):
    pattern = r"[a-z]+(?:_[a-z]+)*"
    matches = re.findall(pattern, s)
    return matches

test_string = "this_is_a_test example_one_two_three test123 not_a_match abc_xyz def_ghi_jkl"

matches = find_sequences(test_string)
print("Matched sequences:", matches)

print()

#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def find_sequences2(s):
    pattern = r"[A-Z]+(?:[a-z]+)*"
    matches = re.findall(pattern, s)
    return matches

test_string = "This is a test Example one Twothree Test123 456 a1"

matches = find_sequences2(test_string)
print("Matched sequences:", matches)

print()

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
txt = "adddfb affff ab asb add"
print(re.findall(r"a.*b", txt))
print()

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.
text = "I don't know, what text to write here..."
print(re.sub(r"[ ,.]", ":", text))
print()

#7 Write a python program to convert snake case string to camel case string.
text = "snake_case_string_to_camel"
print(re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text))
print()

#8 Write a Python program to split a string at uppercase letters.
text = "CamelCaseStringExample"
print(re.sub(r"([A-Z])", r" \1", text))
print()

#9 Write a Python program to insert spaces between words starting with capital letters.
text = "CamelCaseStringExample"
x = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
print(x)
print()

#10 Write a Python program to convert a given camel case string to snake case.
text = "CamelCaseStringExample"
x = re.sub(r"([a-z])([A-Z])", r"\1_\2", text)
x = x.lower()
print(x)

