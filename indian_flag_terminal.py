# We make use of obfuscated code for this
a = 10
b = 0
c = 10
  
# The string is a run length encoding of the map of India ( The first 31 are ignored)
# Alternating characters of the string determine how many spaces or exclamation marks to draw consecutively.  
s = ("TFy!QJu ROo TNn(ROo)SLq SLq ULo+UHs"
     " UJq TNn*RPn/QPbEWS_JSWQAIJO^NBELPe"
     "HBFHT}TnALVlBLOFAkHFOuFETpHCStHAUFA"
     "gcEAelclcn^r^r\\tZvYxXyT|S~Pn SPm S"
     "On TNn ULo0ULo#ULo-WHq!WFs XDt!") 
  
# Read each character of encoded string  
a = ord(s[b])  
  
while a != 0:  
    if b < 170:  
        a = ord(s[b]) 
        b += 1 # Increase the value of b by 1
        # Loop to draw the characters !, space in a line and line break  
        while a > 64:  
            a -= 1
            c += 1
            # ASCII value of 'Z' is 90  
            if c == 90:
                # Now 90/9 = 10
                # 10 is the ASCII value of new line character  
                c = c // 9
                print(end = chr(c))  
            else:
                # 33 is the ASCII value of !
                # Togging over the lower-order bit of 33 gives us 32
                # The ASCII value of space is 32
                # Thus ! is printed if b is odd and space in printed if b is even   
                print(chr(33 ^ (b & 0X01)), end = '')  
    else:  
        break