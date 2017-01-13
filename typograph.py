import re


def replace_hyphen_on_shortdash_in_phone_number(text):
    re_phone = r'(?:\+?\d?-?\(?\d{3}\)?[\s\-\.]?)?\d{3}[\s\-\.]?\d{4}'
    for number in re.finditer(re_phone, text):
        number_start, number_end = number.span()
        text = '{}{}{}'.format(text[:number_start],
                               text[number_start:number_end].replace('-', '–'),
                               text[number_end:])
    return text


def typograph(text):
    patterns = [
        # remove windows line breaks
        (r'\n\r|\r\n', r'\n'),
        # remove redundant spaces and line breaks
        (r'([\s])\1+', r'\1'),
        # remove redundant line breaks at start of line
        (r'^[\n ]+([^\n ])', r'\1'),
        # replace quotes
        (r"""(['"])(.*)(\1)""", r'«\2»'),
        # replace hyphen on dash after punctuation
        (r'(\.{3}\s*|[!?\.,]\s*|^\s*)(-)', r'\1—'),
        # replace hyphen on dash between two words
        (r'([\w]\s+)(-)(\s+[\w])', r'\1—\3'),
        # binding of numbers followed by the words non-breaking hyphen
        (r'(\d)([^\w]|_)+([^\W\d_])', r'\1&#8209;\3'),
        # binding short words followed by the words
        (r'(\b[^\W\d]{1,2})\s+\b', r'\1&nbsp;'),
    ]

    for pattern, repl in patterns:
        text = re.sub(pattern, repl, text, flags=re.MULTILINE)
    text = replace_hyphen_on_shortdash_in_phone_number(text)
    # print(text)
    return text


if __name__ == "__main__":
    s1 = """f"sdf" 'sdf'f"""
    s2 = '- Я -е-б л - л... - П? - Н т-.- ,-'
    s3 = '123-4567f 34f (243)-234-2342 +1-(800)-545-2468 (234)'
    s4 = '4 s  5-j  2jg4_df  g 5  l'
    s5 = """ \n\n\n    \n- Я тебя люблю... - Правда? \n\n   - На самом деле нет."""
    s6 = 'q we\n\n\nr tyu'
    typograph(s6)