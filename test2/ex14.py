from collections import defaultdict, OrderedDict


def sort_display(word_count):
    # using this line of code we sort based on value t[1], if we use t[0] we would sort based on key
    print(OrderedDict(sorted(word_count.items(), key=lambda t: t[1])))


def count1(words_list):
    word_count = defaultdict(int)
    for word in words_list:
        try:
            word_count[int(word)] += 1
        except ValueError:
            continue
    sort_display(word_count)


if __name__ == "__main__":
    my_string = "We are having 3 numbers of 5 pieces and each of them are having 3 stars. We also add an 1 to the end " \
                "of 5 to make " \
                "it equal with 7 or 3 ?"
    words = my_string.split(" ")
    count1(words)
