#!/bin/bash
# 随机复制：A文件夹中有10000个文件，从中随机复制100个到B文件夹中
# 随机移动：cp --> mv

cd A
n=0 # shell中空格不能随便加
for f in $(ls | sort -R); do
    if [[ ! -f B$f ]]; then
        cp $f B
        ((n++ >= 99)) && break
    fi
done
