[TOC]

##一、文件管理常用命令

### 文件目录结构

/：根目录

/home：家目录

/etc：系统配置文件

/bin：可执行的二进制命令



### 常用的Linux命令

| 序号 | 命令              | 作用                     |
| ---- | ----------------- | ------------------------ |
| 01   | ls                | 查看当前文件夹下的内容   |
| 02   | pwd               | 查看当前所在文件夹       |
| 03   | cd [dir_name]     | 切换文件夹               |
| 04   | touch [file_name] | 如果文件不存在，新建文件 |
| 05   | mkdir [dir_name]  | 创建目录                 |
| 06   | rm [file_name]    | 删除指定的文件名         |
| 07   | clear             | 清屏                     |



###终端命令模式

```bash
command [-options] [parameter]
```

- command：命令名
- [-options]：选项，可以对命令进行控制
- [parameter]：传给命令的参数

> 查阅命令帮助信息
>
> command --help
>
> man command
>
> | Tab   | Fuction                  |
> | ----- | ------------------------ |
> | space | display the next page    |
> | enter | display the next line    |
> | b     | go to the  previous page |
> | f     | go to the next page      |
> | q     | quit                     |
> | /word | search for 'word'        |



### 终端实用技巧

1. 自动补全：在敲出`文件`/`目录`/`命令`的前几个字母之后按tab：
   - 没有歧义，自动补全
   - 存在歧义，再按`tab`，提示可能存在的命令
2. 曾经使用过的命令：
   - 上下键切换曾经使用过的命令
   - 想要推出选择并且不执行当前选中的命令，按`ctrl+c`



### 01.ls命令说明

#####Linux下文件和目录的特点

- 以`.`开头的文件为隐藏文件，需要用参数-a才能显示
- `.`代表当前目录
- `..`代表上一级目录

#####ls常用选项

| 参数 | 含义                                     |
| ---- | ---------------------------------------- |
| -a   | 显示指定目录下所有的文件（包括隐藏文件） |
| -l   | 显示文件的详细信息                       |
| -h   | 人性化地显示文件信息                     |

##### ls通配符的使用

| 通配符 | 含义                             |
| ------ | -------------------------------- |
| *      | 任意个数字符                     |
| ？     | 代表任意一个字符，必须是一个字符 |
| []     | 表示可以匹配字符组中的任意一个   |
| [abc]  | 匹配a/b/c中的任意一个            |
| [a-f]  | 匹配从a到f范围内的任意一个字符   |



### 02.cd命令说明

#####cd

Linux所有的目录和文件名都是 大小写敏感的

|       |                                          |
| ----- | ---------------------------------------- |
| cd    | 切换到当前用户的主目录（/home/用户目录） |
| cd ~  | 切换到当前用户的主目录（/home/用户目录） |
| cd .  | 保持当前目录不变                         |
| cd .. | 切换到上级目录                           |
| cd -  | 可以在最近两次目录之间来回切换           |

##### 相对路径和绝对路径

- 相对路径：最前面没有/或者~，表示相对当前目录所在的目录位置
- 绝对路径：最前面有/或者~,表示从genmulu/家目录开始的具体位置



### 03.创建和删除操作

##### touch

- 如果文件不存在，创建一个空白文件
- 如果文件存在，修改文件的末次修改时间

##### mkdir

- -p 连续创建目录

```
mkdir -p a/b/c/d
```

- 新建目录的名称不能与当前目录下的文件重名

##### rm

> 文件删除后不能回复
>
> 可以使用通配符

|      |                                      |
| ---- | ------------------------------------ |
| -f   | 强制删除，忽略不存在的文件，不会提示 |
| -r   | 删除文件夹必须要这个参数             |



###04.拷贝和移动文件

| 序号 | 命令             | 扩展 | 作用                            |
| ---- | ---------------- | ---- | ------------------------------- |
| 01   | tree [dir_name]  | tree | 以树状图列出文件目录结构        |
| 02   | cp source target | copy | 复制文件或目录                  |
| 03   | mv source target | move | 移动文件或目录/文件或目录重命名 |

##### tree

| 选项 | 含义                   |
| ---- | ---------------------- |
| -d   | 只显示目录，不显示文件 |

##### cp

| 选项 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| -i   | 覆盖文件前提示                                               |
| -r   | 若给出的源文件是目录文件，则cp将递归复制该目录下的所有子目录和文件 |

##### mv

| 选项 | 含义                   |
| ---- | ---------------------- |
| -i   | 覆盖文件前提示(重命名) |



### 05查看文件内容

| 序号 | 命令                     | 扩展        | 作用                                           |
| ---- | ------------------------ | ----------- | ---------------------------------------------- |
| 01   | cat filename             | concatenate | 查看文件内容、创建文件、文件合并、追加文件内容 |
| 02   | more filename            | more        | 分屏显示文件内容                               |
| 03   | grep “key_word” filename | grep        | 搜索文本内容                                   |

##### cat

| 序号 | 含义               |
| ---- | ------------------ |
| -b   | 对非空输出编号     |
| -n   | 对输出的所有行编号 |

##### more

| Tab   | Fuction                  |
| ----- | ------------------------ |
| space | display the next page    |
| enter | display the next line    |
| b     | go to the  previous page |
| f     | go to the next page      |
| q     | quit                     |
| /word | search for 'word'        |

##### grep

| 选项 | 含义                       |
| ---- | -------------------------- |
| -n   | 显示匹配行及行号           |
| -v   | 显示不包含匹配文本的所有行 |
| -i   | 忽略大小写                 |

模式查找

| 参数 | 含义                   |
| ---- | ---------------------- |
| ^a   | 行首，搜寻以a开头的行  |
| ke$  | 行尾，搜索以ke结束的行 |



### 06其他

####echo 文字内容

在终端中显示参数指定的文字，通常会和重定向联合使用

####重定向>和>>

将命令执行结果重定向到一个文件

\>表示输出，会覆盖文件原有的内容

\>>表示追加

####管道 |

将一个命令的输出通过管道作为另一个命令的输入

```
ls -lha ~| more
```

```
ls -lha ~ | grep vi
```





## 二、远程管理常用命令

### 01.关机/重启

|      |                      |          |           |
| ---- | -------------------- | -------- | --------- |
| 01   | shutdown option time | shutdown | 关机/重启 |

#### 1.1shutdown

| 选项 | 含义 |
| ---- | ---- |
| -r   | 重启 |

> 不指定选项和参数，默认1分钟后关闭电脑



###02.查看或者配置网卡信息

| 序号 | 命令        | 扩展                          | 作用                              |
| ---- | ----------- | ----------------------------- | --------------------------------- |
| 01   | ifconfig    | configure a network interface | 查看/配置计算机当前的网卡配置信息 |
| 02   | ping ip地址 | ping                          | 检测到目标ip地址的链接是否正常    |

#### 2.1网卡和IP地址

##### 网卡

- 网卡是专门负责网络通讯的硬件设备
- IP地址是设置在网卡上的地址信息

IP地址

- 每台联网的电脑上都有IP地址，是保证电脑之间正常通讯的重要设置

#### 2.2 ifconfig

```
$ipconfig | grep inet
```

#### 2.3 ping

- 用于检测当前计算机到目标计算机之间的网络是否通畅，数值越大 速度越慢。

```
#检测目标主机是否链接正常
$ ping IP
# 检测本地网卡工作正常
$ ping 127.0.0.1
```



### 03.远程登陆和复制文件

#### 3.1 ssh基础

##### 域名和端口号

**域名：**

- 由一串**用点分隔**的名字组成，是**IP地址的别名**

**端口号：**

- IP地址：通过IP地址找到网络上的计算机
- 端口号：通过**端口号**可以找到**计算机上运行的运用程序**
  - SSH服务器的默认端口号是22,
- 常见服务端口号列表：

| 服务      | 端口号 |
| --------- | ------ |
| SSH服务器 | 22     |
| Web服务器 | 80     |
| HTTPS     | 443    |
| FTP服务器 | 21     |

##### SSH客户端的简单使用

```
ssh [-p port] user@remote
```

- user是远程机器上的用户名
- remote是远程机器的地址
- port是SSH Server监听的端口，如果不指定就默认为22

> 使用`exit`退出当前用户登录

#### 3.2 scp

- scp就是source copy，是在一个Linux下用来进行远程拷贝文件的命令
- 它的地址格式与ssh 基本相同，但是指定端口的时候用的是-P

```bash
# 远程拷贝文件
scp -P 2222 KMT-2018-BLG-2758 huqr@166.111.121.192:~/binaryfit/KMT-2018-BLG-2758
scp -P port user@remote:Desktop/01.py 01.py
# 远程拷贝文件夹
scp -r demo user@remote:Desktop
scp -r user@remote:Desktop demo
```



## 三、系统相关命令

### 01.时间和日期

| 序号 | 命令 | 作用                                   |
| ---- | ---- | -------------------------------------- |
| 01   | date | 查看当前系统时间                       |
| 02   | cal  | calendar查看日历，-y可以查看一年的日历 |

###02.磁盘信息

| 序号 | 命令             | 作用                           |
| ---- | ---------------- | ------------------------------ |
| 01   | df -h            | disk free显示磁盘 剩余空间     |
| 02   | du -h [dir_name] | disk usage显示目录下的文件大小 |

> -h以人性化方式显示文件大小

### 03.进程信息

- 进程：当前正在执行的一个程序

| 序号 | 命令                | 作用                               |
| ---- | ------------------- | ---------------------------------- |
| 01   | ps au               | process status查看进程的详细情况   |
| 02   | top                 | 动态显示运行中的进程并且排序       |
| 03   | kill  [-9] 进程代号 | 终止指定代号的进程，-9表示强行终止 |

#### ps

| 选项 | 含义                                     |
| ---- | ---------------------------------------- |
| a    | 显示终端上所有的进程，包括其他用户的进程 |
| u    | 显示进程的详细状态                       |
| x    | 显示没有控制终端的进程                   |

#### top

输入q退出top

####kill [-9] 进程代号

只终止由当前用户开启的进程



## 四、其他命令

### 01.查找文件

- find通常用来在特定目录下搜索符合条件的文件

| 命令                     | 作用                                                  |
| ------------------------ | ----------------------------------------------------- |
| find [path] -name "*.py" | 查找指定文件夹下扩展名是.py的文件，包括子目录         |
| find [path] -name "1*1"  | 查找指指定文件夹下文件名包括1的文件和目录，包括子目录 |

### 02.软连接

| 命令                                        | 作用                             |
| ------------------------------------------- | -------------------------------- |
| ln -s 被连接的源文件（完整路径） 链接文件名 | 建立文件的软连接，类似于快捷方式 |

### 03.打包压缩

#### 3.1打包/解包

- tar 是Linux最常用的备份工具，可以把一系列文件打包到一个大文件中，也可以把一个大文件恢复成一系列文件

- ```bash
  # 打包
  tar -cvf 打包文件.tar 被打包的文件（空格分隔）/路径
  # 解包
  tar -xvf 打包文件.tar
  ```

- | 选项 | 作用                                                        |
  | ---- | ----------------------------------------------------------- |
  | c    | 生成档案文件，创建打包文件                                  |
  | x    | 解开档案文件                                                |
  | v    | 列出归档解档的详细过程，显示进度                            |
  | f    | 指定档案文件名称，f后面一定是.tar文件，所以需要放在选项最后 |

#### 3.2压缩/解压缩

##### gzip

tar命令中有一个选项-z可以调用gzip，从而可以方便地实现压缩和解压缩

```bash
# 压缩
tar -zcvf 打包文件.tar.gz 被压缩的文件（空格分隔）/路径
# 解压缩
tar -zxvf 打包文件.tar.gz
# 解压到指定路径
tar -zxvf 打包文件.tar.gz -C 目标路径
```

##### bzip2

tar命令中有一个选项-j可以调用gzip，从而可以方便地实现压缩和解压缩

```bash
# 压缩
tar -jcvf 打包文件.tar.gz 被压缩的文件（空格分隔）/路径
# 解压缩
tar -jxvf 打包文件.tar.gz
```

### 软件安装

#### 4.1通过apt安装/卸载软件

- apt 是Advanced Packaging Tool，是Linux的一款安装包管理工具
- 可以在终端中方便地安装/卸载/更新软件包

```bash
#安装
$sudo apt install package

#卸载
$sudo apt remove package

#更新
$sudo apt upgrade
```



## 五、Python相关

### pip

镜像源安装

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyAstronomy
```



### conda命令

| 查看帮助         | conda -h                                    |
| ---------------- | ------------------------------------------- |
| 查看conda版本    | conda --version                             |
| 安装包           | conda install package=2.0                   |
| 更新包           | conda update package                        |
| 查看已经安装的包 | conda list                                  |
| 更新包           | conda update package                        |
| 删除包           | conda remove package                        |
| 进入虚拟环境     | activate env                                |
| 创建虚拟环境     | conda create -n web python=3.7 ipykernel    |
| 删除虚拟环境     | conda remove -n env --all                   |
| 查看虚拟环境     | conda env list                              |
| 查看包           | conda list                                  |
| 修改启动项       | conda config --set auto_activate_base false |

####环境相关

```bash
# 配置指定python版本的环境
conda create -n env_name python=2.7
conda create --name env_name python=3.5 numpy scipy

# 列出所有的环境
conda env list
conda info -e
conda info --envs

# 激活环境
conda activate env_name

# 退出环境
conda decativate env_name

# 删除环境
conda remove -n env_name --all

# 环境中的包的管理
conda install pkg_name -n env_name
conda uninstall pkg_name -n env_name
conda remove pkg_name -n env_name

# 复制环境
conda create --name new_env_name --clone old_env_name

# 分享环境
# 把已有的环境分享给其他人，A电脑到B电脑
# A电脑上的操作
conda activate target_env
conda env export > target_env.yml

# 从A copy yml文件，B电脑上的操作
conda env create -f target_env.yml

```

#### 软件包相关

```bash
# 在当前环境中安装
conda install pkg_name 

# 在指定虚拟环境中安装
conda install -n env_name pkg_name

# 升级包
conda update pkg_name
conda update -n env_name pkg_name

# 搜索包
conda search pkg_name


# 指定升级渠道（源）
conda install -c conda-forge pkg_name

# 更改镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes # 搜索时显示通道地址

# 卸载包
conda remove pkg_name
conda remove -n env_name pkg_name

# 列出所有安装的包
conda list --name env_name
conda list -n env_name
conda activate env_name && conda list

# 更新所有包
conda upgrade --all
```

#### conda瘦身

```bash
# 删除没用的包
conda clean -p

# Remove cached package tarballs
conda clean -t

# 删除所有的安装包及cache
conda clean -y -all
```

#### conda 添加国内源

```bash
$ vi ~/.condarc
channels:
  - defaults
show_channel_urls: true default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
  - r
  - bioconda
  - conda-forge

custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

envs_dirs:
  - /home/luna/miniconda3/build/envs
  - /home/luna/anaconda3/envs

pkgs_dirs:
  - /home/luna/miniconda3/build/pkgs
  - /home/luna/anaconda3/pkgs

auto_activate_base: false
```

https://docs.conda.io/en/latest/



### 后台运行

后台运行 

```bash
nohup python -u binfit.py > fit4.log 2>&1 &
```

 查看运行：

```
ps -ef | grep 进程号
```

 不知道进程号的可以用:

```
ps -ef | grep python
```

 查看日志文件 :

```
tail -f xxx.log
```

- nohup：使用nohup python 来运行，可以在关闭连接后依然可以继续运行程序
- -u：python输出是会带有一定的缓冲（或者是延迟）之类的，如果不用-u，我们不一定能在第一时间看到其结果，尤其是输出日志写入文件的时候，所以一般情况下如果要把日志写入什么什么文件，就加上 -u来修饰即可
- \>：
- 2>&1：Linux中0是标准输入，1是标准输出，2是标准错误输出。2 >&1表示如果有错误输出，也得像1一样写道指定文件中。反正我觉得就是一个固定写法，**2 >&1的功能就是：不管对的错的我都要**。
- &：表示**后台运行**，不会占据当前窗口（可以通过查看进程的方式找到它）。

查看文件夹所占内存
```
du -h --max-depth=1 /work/huqr/adaptive_map_binary/
```
