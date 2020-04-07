
class Palindrome:
    def __init__(self):
        return
    def set_query_string(self):
        self.query_string = str.lower(input("Please enter a word: "))

    def is_palindrome(self):
        if ''.join(reversed(self.query_string)) == self.query_string:
            return True
        else:
            return False

    def show_result(self, boolean):
        if boolean:
            print(self.query_string, "is a palindrome!")
        else:
            print(self.query_string, "is not a palindrome")


    
def init():
    self = Palindrome()
    self.active = True
    def is_active():
        if str.lower(input("Do you wish to continue? (Y/N) ")) == 'n':
            return False
        else:
            return True
    while self.active:
        self.set_query_string()
        self.show_result(self.is_palindrome())
        self.active = is_active()

init()
