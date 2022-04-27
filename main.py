#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webvtt 
from retrying import retry
import translators as ts
from tqdm import tqdm
import sys


@retry(wait_random_min=1000, wait_random_max=6000)
def trans(text):
    return ts.baidu(text, to_language="cn")


def main():
    captions = []
    if len(sys.argv) == 1:
        print("{} vtt".format(argv[0]))
        return

    for cap in tqdm(webvtt.WebVTT().read(sys.argv[1])):
        text = cap.text + "\n" + trans(cap.text)
        cap.text = text
        print(cap.text)
        captions.append(cap)

    if len(sys.argv) <= 2:
        webvtt.WebVTT(sys.argv[1], captions).save()
    else:
        webvtt.WebVTT(sys.argv[2], captions).save()


if __name__ == '__main__':
    main()
