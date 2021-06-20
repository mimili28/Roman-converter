import re
class RomanConverter():

    def __init__(self):
        self.numbers = {"I":1,"V":5, "X":10, "L":50,"C":100, "D":500, "M":1000}
        self.roman_letters = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                  (90, 'XC'),  (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                  (5, 'V'), (4, 'IV'), (1, 'I')]
    
    def convert(self, roman_num):
        if (self.validate(roman_num)):
            prev = 0 
            ans = 0
            n = len(roman_num)
            for i in range(n-1, -1, -1):
        
                # If greater than or equal to previous,
                # add to answer
                if self.numbers[roman_num[i]] >= prev:
                    ans += self.numbers[roman_num[i]]
        
                # If smaller than previous
                else:
                    ans -= self.numbers[roman_num[i]]
        
                # Update previous
                prev = self.numbers[roman_num[i]]
            return ans 
        else:
            return 'Invalid number'    
    
    def validate(self,string):
        return(bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",string)))

    def to_roman_convert(self, number):
        output = []
        if (isinstance(number, int) and number > 0):
           for value, letter in self.roman_letters:
                n = number // value               
                output.extend([letter] * n)    
                number -= n * value               
           return "".join(output)
        else:
            raise ValueError("Invalid number")
            

        