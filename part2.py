#!/usr/bin/python
import re


def get_filtered(cnt_list):
    pass


def main():
    cnt_list_res = []
    cnt_list = []
    hash_tag_list_res = []
    hash_tag_list = []
    for i in range(0, 5):
        hash_tag_list_res.append([])
    for i in range(0, 5):
        cnt_list_res.append([])
    with open('part-r-00000') as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.strip()
            (hour, hash_tag, cnt) = re.split('\s+', line)
            hash_tag_list.append(hash_tag)
            cnt_list.append(int(cnt))
        for i in range(0, len(cnt_list)):
            idx = i % 5
            cnt_list_res[idx].append(cnt_list[i])
        for i in range(0, len(hash_tag_list)):
            idx = i % 5
            hash_tag_list_res[idx].append(hash_tag_list[i])
        with open('buffer', 'w') as res_file:
            res_file.write('cnt_list\n')
            res_file.write(str(cnt_list_res))
            res_file.write('\n')
            res_file.write('word_list\n')
            res_file.write(str(hash_tag_list_res))
            res_file.write('\n')

if __name__ == '__main__':
    main()
