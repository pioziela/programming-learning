"""
pobranie pliku w którym pierwsza linia zawiera dwie liczby, które określają ilość
słów w tekście z czasopisma (w drugiej linni) i w trzeciej linii ilość słów repliki oryginalnego tekstu.
"""
with open('text_for_hash_tables.txt', "r") as text:
    for line_number in range(0, 3):
        line = text.readline()
        if line_number == 1:
            words_in_second_line = list(line.rstrip().split())
        elif line_number == 2:
            words_in_third_line = list(line.rstrip().split())


def compare_text(oryginal_words, replica_words):
    """funkcja sprawdzająca czy z tekstu oryginalnego można stworzyć jego replikę"""
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


yes_or_no = compare_text(words_in_second_line, words_in_third_line)
print(yes_or_no)