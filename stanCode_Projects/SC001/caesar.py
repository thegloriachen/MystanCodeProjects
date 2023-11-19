"""
File: caesar.py
Name: Gloria
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program demonstrates the idea of caesar cipher.
    Users will be asked to input a number to produce shifted ALPHABET as the cipher table.
    And then user will also asked to input the ciphered string, after that, the deciphered string will be output.
    """
    secret_number = int(input("Secret number:"))
    new_alphabet = input("What's the ciphered string?")
    ans = ""
    # for loop
    for i in range(len(new_alphabet)):
        ch = new_alphabet[i]
        # 若為空白或不為alpha，則保留原字元
        if ch == " " or not ch.isalpha():
            ans = ans + ch
        else:
            # 須符合case-insensitive條件，若input有小寫字，則判斷為大寫
            if ch.islower():
                ch = ch.upper()
            else:
                ch = new_alphabet[i]
            # 尋找該alpha在英文字母的位置，並執行解密
            j = ALPHABET.find(ch)
            if j+secret_number > 25:     # 若加了secret number大於原先字串位置數字，超過部分需自字串的第一位開始計算
                j = j-26+secret_number
                ch = ALPHABET[j]
            else:
                ch = ALPHABET[j+secret_number]
            ans = ans + ch
    print("The deciphered string is: " + ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
