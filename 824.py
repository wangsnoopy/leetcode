class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # start vowal, append 'ma' at the end
        # start with consonant, remove the first letter to the end and add 'ma'
        # first leeter get 1 'a', second get two 'a' and so on

        vowel = 'aeiouAEIOU'
        # split the sentence by " "
        sentence = sentence.split()
        for i in range(len(sentence)):
            word = sentence[i]
            # check the first if it is vowel
            if sentence[i][0] in vowel:
                sentence[i] += 'ma' + 'a'* (i + 1)
            else:
                first = sentence[i][0]
                sentence[i] = word[1:] + first + 'ma' + 'a'*(i + 1)
        return ' '.join(sentence)