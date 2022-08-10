def rle_encode(data):
    encoding = ' '
    prev_char = ''
    count = 1

    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else: 
            count += 1
    else: encoding += str(count) + prev_char
    return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


with open ('text_for_encoding.txt', 'r') as file:
    new_text = file.read() 

encode_text = rle_encode(new_text)
print(f'{new_text} - закодированный {encode_text}')

with open ('text_encoding.txt', 'w') as file:
    file.write(encode_text)

with open ('text_for_decoding.txt', 'r') as file:
    new_text_2 = file.read() 

decode_text = rle_decode(new_text_2)
print(f'{new_text_2} - раскодированный {decode_text}')

with open ('text_decode.txt', 'w') as file:
    file.write(decode_text)