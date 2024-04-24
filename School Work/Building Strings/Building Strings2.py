def text_block(text: str) -> str:
    
    length = len(text)
    out = ''

    for c  in (text):
        out += c * length + f'\n'

    return out

print(text_block('HaHa'))