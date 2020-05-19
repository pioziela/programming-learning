def getting_text():
    """
    The function getting_text downloads a file in which the first line contains two numbers
    that specify the number of words in the magazine text (in the second line)
    and in the third line the number of words of the replica of the original text.
    """
    with open('text_for_hash_tables.txt', "r") as text:
        line_number = 0
        for line in text:
            if line_number == 0:
                pass
            elif line_number == 1:
                words_in_second_line = list(line.rstrip().split())
            elif line_number == 2:
                words_in_third_line = list(line.rstrip().split())
            line_number += 1
    return words_in_second_line, words_in_third_line


def compare_text(oryginal_words, replica_words):
    """
    The function compare_text checks if a replica
    can be created from the original text.
    """
    for words in replica_words:
        count_of_word = replica_words.count(words)
        for words_2 in oryginal_words:
            if oryginal_words.count(words) == 0:
                return 'No'
            elif words_2 == words:
                count_of_word_2 = oryginal_words.count(words_2)
                if count_of_word > count_of_word_2:
                    return 'No'
    return 'Yes'


oryginal_text, replica_text = getting_text()
yes_or_no = compare_text(oryginal_text, replica_text)
print(yes_or_no)