# International Morse Code defines a standard encoding where 
# each letter is mapped to a series of dots and dashes, as follows: 
# "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet 
# is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",
#  ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
#  "...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
#
# Example:
#
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
#
# Explanation: 
#
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
#  
#
# Note:
# 
# - The length of words will be at most 100.
# - Each words[i] will have length in range [1, 12].
# - words[i] will only consist of lowercase letters.


# Solution-1 with chr(), e.g. chr(97) = 'a'
class Solution:
    def uniqueMorseRepresentations(self, words):
        tocode = []
        for word in words:
            temp = []
            for letter in word:
                temp.append(''.join(codes[ord(letter) - ord('a')]))
            tocode.append(''.join(temp))
        return len(set(tocode))

codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = ["gin", "zen", "gig", "msg"]        
Solution().uniqueMorseRepresentations(words) 


# Solution-2 with dictionary
from collections import defaultdict
import string
codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphabet = list(string.ascii_lowercase)
letterid = defaultdict(lambda: len(list(string.ascii_lowercase)))
codedict= dict(zip(alphabet, codes))

class Solution:
    def uniqueMorseRepresentations(self, words):
        tocode = []
        for word in words:
            temp=[]
            for letter in word:
                temp.append(codedict[letter])
            tocode.append(''.join(temp))
        return len(set(tocode))
words = ["gin", "zen", "gig", "msg"]        
Solution().uniqueMorseRepresentations(words) 