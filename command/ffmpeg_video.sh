# 用ffmpeg实现视频剪切
# -i表示源文件；-vcodec copy表示使用与原视频相同的视频解码器；-acodec copy表示使用与原视频相同的音频解码器；
# -ss表示开始时间；-to表示结束时间；-y表示若存在则覆盖。
ffmpeg -i ./1.mp4 -vcodec copy -acodec copy -ss 00:10:00 -to 00:10:50 ./1_clip.mp4 -y




# ffmpeg转换视频格式
ffmpeg -i 1.webm 1.mp4
