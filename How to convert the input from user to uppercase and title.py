#2.Write a Python class that has two methods: get_String and print_String , get_String accept a string from the user and print_String prints the string in upper case.

class String:
    def get_string(self):
        self.string1 = input('Enter a string:')
    
    def print_string(self):
        print(self.string1.upper())
    
       #Additional to print string to title case, If you want to change to lower case, etc. You can only add or change .title .upper, swapcase, .capitalize
    
    def print_string_Title(self):
        print(self.string1.title())
string = String()
string.get_string()
string.print_string()
string.print_string_Title()