from constants import *


def parser_line(line):
    arr = line.split(JSON_COLON, maxsplit=1)
    if '-' in arr[0]:
        i = 1
        s = list(line)
        while line[i] == ' ':
            i += 1
        s.insert(i-1, '-')
        line = ''.join(s).replace('-', '', 1)
        output_without_spaces = whitespace(line)
        nice_out = output_without_spaces.replace('"', '').replace(',', '').replace('\n', '')
        yaml_file.write(nice_out)
        yaml_file.write('\n')
    else:
        arr[0] += JSON_COLON
        key_and_value = [arr[0].replace('"', ''), arr[1].replace('"', '').replace('\n', '').replace('[', '', 1)]
        nice_output = ''.join(key_and_value)
        nice_output_with_space = whitespace(nice_output)
        yaml_file.write(' ' + nice_output_with_space)
        yaml_file.write('\n')


def first_parser(text):
    for d in range(0, len(text)):
        if JSON_LEFTBRACE in text[d]:
            text[d+1] = '-' + text[d+1]
        if JSON_COLON in text[d]:
            parser_line(text[d])


def whitespace(text):
    i = 0
    while text[i] == ' ':
        i += 1
    j = i // 4
    text = (' ' * (j - 1)) + text[i:]
    return text


json_file = open('lab4.json', 'r', encoding='utf-8')
yaml_file = open('lab4.yaml', 'w', encoding='utf-8')

json_lines = json_file.readlines()
yaml_file.write('---\n')

first_parser(json_lines)
