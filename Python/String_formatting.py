"""
Variables
"""

first_name = "John"
last_name = "Smith"
# print("Hi "+first_name)
print(f"Hi {first_name}")

sentence = "Hi {}"
print(sentence.format(first_name))

sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))

sentence = f"Hi {first_name} {last_name} I hope you are learning "
print(sentence)