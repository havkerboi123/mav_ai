def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    #can store 2 lists/vectors, one for the last occurrence of each character which is -1 at the start
    #second list is for the maximum difference between 2 occurrences of that character

    last_occurrence = [-1] * 128  
    max_length = 0  #Initializing maximum length of substring without repeating characters
    start = 0  #Initializing start index of current substring

    for i, char in enumerate(s):
        #If there aren't 2 occurrences of any character then max difference between two occurrences = length of string
        if last_occurrence[ord(char)] >= start:
            start = last_occurrence[ord(char)] + 1 
        last_occurrence[ord(char)] = i  
        #Min of (max difference between 2 occurrences of a character) is the answer
        max_length = max(max_length, i - start + 1)  

    
    return max_length
    pass

# Example test cases
print(length_of_longest_substring("abcabcbb"))  # Expected output: 3
print(length_of_longest_substring("bbbbb"))     # Expected output: 1
print(length_of_longest_substring("pwwkew"))    # Expected output: 3
