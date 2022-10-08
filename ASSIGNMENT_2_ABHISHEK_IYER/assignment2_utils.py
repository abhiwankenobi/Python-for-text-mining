def clean_text_general(text, chars_to_remove={'\n', ',', '.', '"'}):
    for char in chars_to_remove:
        text = text.replace(char,'')
    return text