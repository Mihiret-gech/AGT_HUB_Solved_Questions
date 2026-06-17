class Solution:
    def countCharacters(self, words, chars):
        total = 0

        for word in words:
            t = list(chars)

            for ch in word:
                if ch in t:
                    t.remove(ch)
                else:
                    break
            else:
                total += len(word)

        return total
