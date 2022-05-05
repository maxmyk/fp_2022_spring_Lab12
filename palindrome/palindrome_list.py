"""
Palindrome class realization.
"""

from arraystack import ArrayStack


class Palindrome:
    """
    Palindrome class
    """
    @staticmethod
    def read_file(path):
        """
        Returns a list of words (strings) in
        the order in which they are specified
        in the input file (without additional
        information).
        """
        with open(path, 'r') as file:
            contents = file.read()
            return list(dict.fromkeys([
                word for elem in [
                    line.split(' /')[0].split(' adv')[0].split(
                        ' noun')[0].split(' adj')[0].split(
                        ' predic')[0].split(' excl')[0].split(
                        ' insert')[0].split(' :v')[0].split(
                        ' part')[0].split(' verb')[0].split(
                        ' :rare')[0].split(' :coll')[0].split(
                        '/A')[0].split(' conj')[0].split(
                        ' +cs=')[-1].strip('#').strip(' \\').split()
                    for line in contents.split('\n')
                    if line != ''
                ]
                for word in elem
                if word
            ]))

    @staticmethod
    def write_to_file(path, words):
        """
        Writes palindrome words to a file.
        Each word is written on a new line.
        """
        with open(path, 'w') as output_file:
            output_file.write('\n'.join(words))

    def find_palindromes(self, dict_path, out_path):
        """
        Returns a list of words that are palindromes;
        calls the read_file and write_to_file functions.
        """
        data = self.read_file(dict_path)
        words = []
        for elem in data:
            orig_word = ArrayStack()
            rev_word = ArrayStack()
            word_len = len(elem)
            if word_len != 1:
                word_len //= 2
                for letter in elem:
                    orig_word.push(letter)
                for _ in range(word_len):
                    rev_word.push(orig_word.pop())
                pal_flag = False
                if orig_word._size != rev_word._size:
                    orig_word.pop()
                for _ in range(word_len):
                    let1 = rev_word.pop()
                    let2 = orig_word.pop()
                    if let1 != let2:
                        pal_flag = False
                        break
                    else:
                        pal_flag = True
                if pal_flag and elem not in words:
                    words.append(elem)
            elif elem not in words:
                words.append(elem)
        self.write_to_file(out_path, words)
        return words


if __name__ == '__main__':
    palindrome = Palindrome()
    print(palindrome.find_palindromes(
        "palindrome/base.lst", "palindrome/palindrome_uk.txt"))
    print(palindrome.find_palindromes(
        "palindrome/words.txt", "palindrome/palindrome_en.txt"))
