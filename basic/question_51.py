text = "A man a plan a canal Panama"
# Slightly harder palindrome problem
t = text.strip().lower().replace(" ", "")
if t == t[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")