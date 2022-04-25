#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webvtt 
import translators as ts
import sys



def main():
    captions = []
    if len(sys.argv) == 1:
        print("{} vtt".format(argv[0]))
        return

    for cap in webvtt.WebVTT().read(sys.argv[1]):
        text = cap.text + "\n" + ts.google(cap.text)
        cap.text = text
        captions.append(cap)

    if len(sys.argv) <= 2:
        webvtt.WebVTT(sys.argv[1], captions).save()
    else:
        webvtt.WebVTT(sys.argv[2], captions).save()


if __name__ == '__main__':
    main()
