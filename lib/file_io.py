def write_file(file_name, file_content):
    text_file= open(f'{file_name}.txt', mode='w', encoding='utf-8')
    text_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as text_file:
     text_file.write(append_content)

def read_file(file_name):
    text_file=open(f'{file_name}.txt', mode='r', encoding='utf-8')
    return text_file.read()