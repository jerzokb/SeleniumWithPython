class Main:
    textToCheck1 = "O, ty z Katowic, Iwo? Tak, Zyto."
    textToCheck2 = "O, z Katowic, Iwo? Nie, Zyto."
    intToCheck1 = 12321
    intToCheck2 = 12343

    list = [textToCheck1, textToCheck2, intToCheck1, intToCheck2]

    def is_this_text_palindrome(self):
        reverse_str = ""
        no_comma = self.replace(",", "")
        no_dot = no_comma.replace(".", "")
        no_question = no_dot.replace("?", "")
        no_spaces = no_question.replace(" ", "")
        str_length = len(no_spaces)

        i = (str_length - 1)
        while i >= 0:
            reverse_str = reverse_str + no_spaces[i]
            i -= 1

        if no_spaces.lower() == reverse_str.lower():
            return True
        else:
            return False

    for el in list:
        isTextPalindrome = is_this_text_palindrome(str(el))
        if isTextPalindrome:
            print("This is " + str(isTextPalindrome) + ". This \"" + str(el) + "\" is a palindrome")
        else:
            print("This is " + str(isTextPalindrome) + ". This \"" + str(el) + "\" is not a palindrome")