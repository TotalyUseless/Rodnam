__author__ = "james"

"""
1. Get name and remove any characters
2. Get greatest prime factor of first letter
3. Capitalize all letters divisible by the factor
4. Insert (position * 13) + 100 after every letter
5. Insert symbol of last digit of every new 3-digit number
6. Insert letter at position before every single digit
7. Mirror every letter (position * 26) % 27
"""

class pwGenerate:
    def __init__(self, pw):
        self.original = pw
        self.password = ""
        self.lowerCases = 'abcdefghijklmnopqrstuvwxyz'
        self.upperCases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alphabet  = self.lowerCases + self.upperCases
        self.spec = list('!@#$%^&*()')
        self.numbers = [str(n) for n in list(range(0,10))]
        self.encrypt()
    def getFactor(self, n):
        primes = []
        d = 2
        while d * d <= n:
            while (n % d) == 0:
                primes.append(d)
                n //= d
            d += 1
        if n > 1:
            primes.append(n)
        return max(primes)
    def encrypt(self):
        pw = self.original
        pw = [char for char in pw if char in self.alphabet]
        pw = "".join(pw).lower()
        first_index = self.lowerCases.index(pw[0]) + 1
        primeFactor = self.getFactor(first_index)
        pw_hold = list(pw)
        pw_new = []
        for position in range(0,len(pw_hold)):
            letter_index = self.lowerCases.index(pw_hold[position]) + 1
            if letter_index % primeFactor == 0:
                pw_hold[position] = pw_hold[position].upper()
            number_insert = str((letter_index * 13) + 100)
            pw_new.append(pw_hold[position])
            pw_new += list(number_insert)
            char_insert = int(number_insert[2]) - 1
            pw_new.append(self.spec[char_insert])
        pw_new_two = []
        for position in range(0,len(pw_new)):
            if pw_new[position] in self.numbers:
                insert_pos = int(pw_new[position]) - 1
                pw_new_two.append(self.lowerCases[insert_pos])
            pw_new_two.append(pw_new[position])
        for position in range(0,len(pw_new_two)):
            current_char =  pw_new_two[position]
            if current_char in self.alphabet:
                if current_char in self.lowerCases:
                    letterSpace = (((self.lowerCases.index(current_char) + 1) * 26) % 27) -1
                    pw_new_two[position] = self.lowerCases[letterSpace]
                else:
                    letterSpace = (((self.upperCases.index(current_char) + 1) * 26) % 27) - 1
                    pw_new_two[position] = self.upperCases[letterSpace]
            else:
                continue
        self.password = "".join(pw_new_two)

hotmail_pw = pwGenerate('hotmail').password
facebook_pw = pwGenerate('facebook').password
twitter_pw = pwGenerate('twitter').password
exxon_pw = pwGenerate('exxon').password
netflix_pw = pwGenerate('netflix').password

print("{}\n{}\n{}\n{}".format(hotmail_pw,facebook_pw,twitter_pw,exxon_pw,netflix_pw))


