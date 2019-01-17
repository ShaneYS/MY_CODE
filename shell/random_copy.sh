#!/bin/bash
# 随机复制：A文件夹中有10000个文件，从中随机复制100个到B文件夹中

cd /A
n = 0
for f in $(ls | sort -R); do
    if [[! -f /B/$f ]]; then
        cp $f /B
        ((n++ >= 100)) && break
    fi
done
