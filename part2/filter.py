#!/usr/bin/python
import re


def get_filtered(cnt_list):
    pass


def main():
    hash_tag_list = []
    with open('result') as f:
        lines = f.read().splitlines()
        for line in lines:
            line = line.strip('(').strip(')')
            (hour, hash_tag, cnt) = re.split('\W+', line)
            hash_tag_list.append(hash_tag)

    get_filtered_list(cnt_list)

if __name__ == '__main__':
    main()
