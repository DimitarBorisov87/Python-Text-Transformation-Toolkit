print("🧠 Welcome to the Text Transformation Toolkit!")
print("Choose a transformation:")
print("1. Reverse Text")
print("2. Convert to Uppercase")
print("3. Convert to Lowercase")
print("4. Title Case")
print("5. Count Vowels")
print("6. Remove All Spaces")
print("7. Replace Vowels with '*'")
print("8. Check if Palindrome")
print("9. Word Frequency Counter")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get the input string
text = input("Enter the text: ")

# Step 4: Apply the selected transformation
if choice == 1:
    # TODO: Reverse the text using slicing or a loop
    new_text = text[::-1]
    print(new_text)

elif choice == 2:
    # TODO: Convert the text to uppercase using string methods
    print(text.upper())

elif choice == 3:
    # TODO: Convert the text to lowercase using string methods
    print(text.lower())

elif choice == 4:
    # TODO: Convert the text to title case (capitalize each word)
    new_text = text.capitalize()
    print(new_text)

elif choice == 5:
    # TODO: Count how many vowels are in the text (a, e, i, o, u)
    vowels_counter = 0
    vowels_list = ["a", "e", "i", "o", "u"]
    for char in text:
        if char in vowels_list:
            vowels_counter += 1
    print(vowels_counter)

elif choice == 6:
    # TODO: Remove all spaces from the string using replace() or join()
    text = text.replace(" ", "")
    print(text)

elif choice == 7:
    # TODO: Replace all vowels with "*" using a loop or comprehension
    vowels_list = ["a", "e", "i", "o", "u"]

    for char in text:
        if char in vowels_list:
            text = text.replace(char, "*")
    print(text)

elif choice == 8:
    # TODO: Check if the text is a palindrome (ignoring case and spaces)

    text_lower = text.lower().replace(" ", "")

    i = 0
    j = len(text_lower) - 1
    is_palindrome = True

    while i < j:
        if text_lower[i] != text_lower[j]:
            is_palindrome = False
            break

        i += 1
        j -= 1

    if is_palindrome:
        print("Yes")
    else:
        print("No")

elif choice == 9:
    # TODO: Count the frequency of each word and display the result
    from collections import Counter

    word_frequency = Counter(text.split())
    print(word_frequency)

else:
    print("❌ Invalid choice! Please restart the program.")
