1. 安装：pip install virtualenv

2. 创建虚拟环境：

（1）virtualenv myenv
     创建目录myenv，其中包含：lib/包含虚拟环境后续安装的包；include/包含支持python的类库；bin/可执行文件

（2）virtualenv -p /usr/bin/python2 myenv
     virtualenv -p /usr/bin/python3 myenv
     指定虚拟环境使用的python版本（可用which python,whereis python查看）

（3）virtualenv --system-site-packages myenv
     创建环境时继承系统全局软件包（默认不含全局软件包）
     全局软件包位置：/usr/bin/python_version/site-packages

3. 进入环境：source myenv/bin/activate
   注销环境：deactivate
   删除环境：rm -rf myenv

4. 导出环境配置：pip freeze > requirements.txt
   恢复环境配置：pip install -r requirements.txt
