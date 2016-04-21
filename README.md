# Game of Thrones I

## The challenge

King Robert rules 7 kingdoms. He finds out from a raven that the Dothraki are on the war path against him. The Dothraki need to cross the treacherous Byss river enter his realm. There is only one bridge that connects both sides of the river, and it is sealed by a huge door.

![door](game-of-thrones.png)

The king wants to lock the door so that the Dothraki cannot enter. But, to lock the door he needs a key that is an [anagram](https://en.wikipedia.org/wiki/Anagram) of a [palindrome](https://en.wikipedia.org/wiki/Palindrome) string.

The king has already solved a series of enigmas and obtained a string composed of lowercase English letters. He needs your help to figure out whether or not any anagram of that string can be a palindrome that he can use.

*Constraints*
1  ≤ length of string ≤ 106
Each character of the string is a lowercase English letter.

*Input Format*
A single line which contains the input string

*Output Format*
A single line which contains "YES" or "NO" (uppercase, without quotes).

Sample Input  #00:
```
aaabbbb
```

Sample Output #00
```
YES
```

Explanation  #00
A palindrome permutation of the given string is bbaaabb.

Sample Input #01
```
cdefghmnopqrstuvw
```

Sample Output #01
```
NO
```

Explanation #01
You can verify that the given string has no palindrome permutation.

