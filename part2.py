#!/usr/bin/python
import re


def get_filtered(cnt_list):
    pass


def main():
    hash_tag_list = []
    cnt_list = []
    with open('part-r-00000') as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.strip()
            (hour, hash_tag, cnt) = re.split('\s+', line)
            hash_tag_list.append(hash_tag)
            cnt_list.append(int(cnt))
        with open('buffer', 'w') as res_file:
            res_file.write('cnt_list\n')
            res_file.write(str(cnt_list))
            res_file.write('\n')
            res_file.write('word_list\n')
            res_file.write(str(hash_tag_list))
            res_file.write('\n')
            
if __name__ == '__main__':
    main()
