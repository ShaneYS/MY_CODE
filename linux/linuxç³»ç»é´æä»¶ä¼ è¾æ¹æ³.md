1. scp 复制文件；scp -r 复制目录

2. rsync差异化传输(支持断点续传,数据同步)
rsync不用打包，可以整个文件夹传输
rsync -avz /from /to就是从服务器上下载整个文件夹

