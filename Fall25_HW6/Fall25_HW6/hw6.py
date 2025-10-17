import re


def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: string
    """
    pattern = r'^[a-zA-Z]{1,10}\.[1-7][0-9]{2}[a-zA-Z]*@(vought\.com|godolkin\.edu|fbsa\.gov)$'

    if re.fullmatch(pattern, searchstring):
        return "valid"
    else:
        return "invalid"


def problem2(searchstring):
    """
    Extract author and book.

    :param searchstring: string
    :return: tuple
    """
    pattern = r'([A-Z][a-z]*(?: [A-Z][a-z]*)?)\s+wrote\s+(?:([A-Z0-9][a-zA-Z0-9]*(?:\s+[A-Z0-9][a-zA-Z0-9]*){0,2})|books)'

    match = re.search(pattern, searchstring)
    if match:
        author = match.group(1).strip()
        book = match.group(2) if match.group(2) else "books"
        return (author, book.strip())
    else:
        return ("noauthor", "noname")


def problem3(searchstring):
    """
    Replace Boy/Girl or boy/girl with Man/Woman or man/woman respectively.

    :param searchstring: string
    :return: string
    """
    pattern = r'([A-Z][a-z]*)\s+(Boy|Girl|boy|girl)'

    def replace_match(match):
        preceding_word = match.group(1)
        target_word = match.group(2)

        if target_word.lower() == 'boy':
            replacement = 'Man' if target_word[0].isupper() else 'man'
        else:
            replacement = 'Woman' if target_word[0].isupper() else 'woman'

        return f"{preceding_word} {replacement}"

    result = re.sub(pattern, replace_match, searchstring)

    if result == searchstring:
        return "nomatch"
    else:
        return result


if __name__ == '__main__':

    print("\nProblem 1:")
    testcase11 = "starlight.123@vought.com"
    print(
        "Student answer: ",
        problem1(testcase11),
        "\tAnswer correct?",
        problem1(testcase11) == "valid",
    )

    testcase12 = "hughie.250supe@fbsa.gov"
    print(
        "Student answer: ",
        problem1(testcase12),
        "\tAnswer correct?",
        problem1(testcase12) == "valid",
    )

    testcase13 = "marie.100@godolkin.edu"
    print(
        "Student answer: ",
        problem1(testcase13),
        "\tAnswer correct?",
        problem1(testcase13) == "valid",
    )

    testcase14 = "a-train.123@vought.com"
    print(
        "Student answer: ",
        problem1(testcase14),
        "\tAnswer correct?",
        problem1(testcase14) == "invalid",# hyphen in name
    )

    testcase15 = "homelander.800@vought.com"
    print(
        "Student answer: ",
        problem1(testcase15),
        "\tAnswer correct?",
        problem1(testcase15) == "invalid",# out of range
    )

    testcase16 = "blacknoir.567*abc@godolkin.edu"
    print(
        "Student answer: ",
        problem1(testcase16),
        "\tAnswer correct?",
        problem1(testcase16) == "invalid",  # non-letters after id
    )

    testcase17 = "noir.123@vought.co"
    print(
        "Student answer: ",
        problem1(testcase17),
        "\tAnswer correct?",
        problem1(testcase17) == "invalid",
    )

    testcase18 = "starlight.144@vought.comasdf"
    print(
        "Student answer: ",
        problem1(testcase18),
        "\tAnswer correct?",
        problem1(testcase18) == "invalid",
    )


    print("\nProblem 2:")
    testcase21 = "George Orwell wrote 1984"
    print(
        "Student answer: ",
        problem2(testcase21),
        "\tAnswer correct?",
        problem2(testcase21) == ("George Orwell", "1984"),
    )

    testcase22 = "In the 1930s, a Mystery writer wrote Mary Westmacotts. Later it was found that Agatha Christie wrote The Westmacott Novels"
    print(
        "Student answer: ",
        problem2(testcase22),
        "\tAnswer correct?",
        problem2(testcase22) == ("Agatha Christie", "The Westmacott Novels"),
    )

    testcase23 = "Roxette wrote books"
    print(
        "Student answer: ",
        problem2(testcase23),
        "\tAnswer correct?",
        problem2(testcase23) == ("Roxette", "books"),
    )

    testcase24 = "Erin Morgenstern wrote The Starless Sea Book and The Night Circus"
    print(
        "Student answer: ",
        problem2(testcase24),
        "\tAnswer correct?",
        problem2(testcase24) == ("Erin Morgenstern", "The Starless Sea"),
    )

    testcase25 = "Haruki Murakami wrote 1Q84"
    print(
        "Student answer: ",
        problem2(testcase25),
        "\tAnswer correct?",
        problem2(testcase25) == ("Haruki Murakami", "1Q84"),
    )

    testcase26 = "Khaled Hosseini wrote sad books"
    print(
        "Student answer: ",
        problem2(testcase26),
        "\tAnswer correct?",
        problem2(testcase26) == ("noauthor", "noname"),
    )

    testcase27 = "Haruki Murakami wrote Norwegian Wood"
    print(
        "Student answer: ",
        problem2(testcase27),
        "\tAnswer correct?",
        problem2(testcase27) == ("Haruki Murakami", "Norwegian Wood"),
    )

    print("\nProblem 3:")
    testcase31 = "Crimson Girl, report to Brink Hall!"
    print(
        "Student answer: ",
        problem3(testcase31),
        "\tAnswer correct?",
        problem3(testcase31) == "Crimson Woman, report to Brink Hall!",
    )

    testcase32 = "There is a girl in Dorm C Tech Boy"
    print(
        "Student answer: ",
        problem3(testcase32),
        "\tAnswer correct?",
        problem3(testcase32) == "There is a girl in Dorm C Tech Man",
    )

    testcase33 = "There is a boy that needs help"
    print(
        "Student answer: ",
        problem3(testcase33),
        "\tAnswer correct?",
        problem3(testcase33) == "nomatch",
    )
