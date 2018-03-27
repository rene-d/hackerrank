# Caesar Cipher
# Encrypt a string by rotating the alphabets by a fixed value in the string.
# 
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
# 


def caesarCipher(s, k):
    # Complete this function
    def caesar():
        for c in s:
            c = ord(c)
            if 97 <= c <= 122:
                c = 97 + ((c - 97) + k) % 26
            elif 65 <= c <= 90: 
                c = 65 + ((c - 65) + k) % 26
            yield chr(c) 
    
    return ''.join(caesar())
        

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)

