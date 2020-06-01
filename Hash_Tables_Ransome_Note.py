def getting_text():
    """
    The function downloads a file in which the first line contains two numbers
    that specify the number of words in the magazine text (in the second line)
    and in the third line the number of words of the replica of the original text.
    """
    with open('text_for_hash_tables.txt', "r") as text:
        for line_number, line in enumerate(text, start=1):
            if line_number == 2:
                words_in_second_line = list(line.rstrip().split())
            elif line_number == 3:
                words_in_third_line = list(line.rstrip().split())
    return words_in_second_line, words_in_third_line


def compare_text(oryginal_words, replica_words):
    """
    The function checks if a replica
    can be created from the original text.
    """
    words_number_in_replica = len(replica_words)
    compatibility_counter = 0
    for replica_word in replica_words:
        count_of_word = replica_words.count(replica_word)
        count_of_word_2 = oryginal_words.count(replica_word)
        if count_of_word_2 >= count_of_word:
            compatibility_counter += 1
        else:
            pass
    if compatibility_counter == words_number_in_replica:
        return 'Yes'
    else:
        return 'No'


oryginal_text, replica_text = getting_text()
yes_or_no = compare_text(oryginal_text, replica_text)
print(yes_or_no)