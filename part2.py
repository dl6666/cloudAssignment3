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
        cnt_list0 = []
        cnt_list1 = []
        cnt_list2 = []
        cnt_list3 = []
        cnt_list4 = []
        word_list0 = []
        word_list1 = []
        word_list2 = []
        word_list3 = []
        word_list4 = []
        for i in range(0, len(hash_tag_list)):
            if (i % 5) == 0:
                word_list0.append(hash_tag_list[i])
            if (i % 5) == 1:
                word_list1.append(hash_tag_list[i])
            if (i % 5) == 2:
                word_list2.append(hash_tag_list[i])
            if (i % 5) == 3:
                word_list3.append(hash_tag_list[i])
            if (i % 5) == 4:
                word_list4.append(hash_tag_list[i])
        for i in range(0, len(cnt_list)):
            if (i % 5) == 0:
                cnt_list0.append(cnt_list[i])
            if (i % 5) == 1:
                cnt_list1.append(cnt_list[i])
            if (i % 5) == 2:
                cnt_list2.append(cnt_list[i])
            if (i % 5) == 3:
                cnt_list3.append(cnt_list[i])
            if (i % 5) == 4:
                cnt_list4.append(cnt_list[i])
        with open('buffer', 'w') as res_file:
            res_file.write('cnt_list0\n')
            res_file.write(str(cnt_list0))
            res_file.write('\n')
            res_file.write('cnt_list1\n')
            res_file.write(str(cnt_list1))
            res_file.write('\n')
            res_file.write('cnt_list2\n')
            res_file.write(str(cnt_list2))
            res_file.write('\n')
            res_file.write('cnt_list3\n')
            res_file.write(str(cnt_list3))
            res_file.write('\n')
            res_file.write('cnt_list4\n')
            res_file.write(str(cnt_list4))
            res_file.write('\n')
            res_file.write('word_list0\n')
            res_file.write(str(word_list0))
            res_file.write('\n')
            res_file.write('word_list1\n')
            res_file.write(str(word_list1))
            res_file.write('\n')
            res_file.write('word_list2\n')
            res_file.write(str(word_list2))
            res_file.write('\n')
            res_file.write('word_list3\n')
            res_file.write(str(word_list3))
            res_file.write('\n')
            res_file.write('word_list4\n')
            res_file.write(str(word_list4))
            res_file.write('\n')

if __name__ == '__main__':
    main()
