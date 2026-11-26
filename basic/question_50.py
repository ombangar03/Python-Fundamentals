# palindrome checking

# A palindrome is a word that reads the same forward and backward.

"""Examples:
- madam → Palindrome
- level → Palindrome
- python → Not a palindrome
- racecar → Palindrome"""

text = input("Enter the text: ").strip().lower()

# palindrome = ""


if text[::-1] == text:
    print("Its a palindrome")
else:
    print("Not a palindrome")


# text = "python"

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")