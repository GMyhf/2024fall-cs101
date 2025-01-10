# 计概课前准备

笔者这几天看到计概群中出现了各种各样的问题，基本上是第一次配置的小白会出现的很多经典问题。也看到明明是同一个问题且已经被解决的事情被很多人反复提问……笔者觉得确实需要一篇比较长的内容来帮助各位完全不了解的新手搭配出一套自己使用得很舒服方便的代码环境。

以下内容均来自于笔者亲身经历或亲眼所见，希望对大家有所帮助
> PS: 由于笔者没有mac，所以接下来都是Windows系统下的操作

## 注意事项

1. 请尽量不要在电脑路径中出现中文和空格，包括但不限于
    - 用户名，即C:/Users文件夹下面你的用户名
    - 文件夹
    - 代码文件的文件名

    中文不能出现是因为部分软件或编译器，比如g++，对utf-8字符可能存在一定的支持问题，同时由于这些软件可能会在C盘你的用户文件夹或其它文件夹中建立一些缓存或临时文件，所以只有安装路径中文是不够的。
    > PS: 我知道这些内容都可以自定义来保证软件绝对不会用到含有中文的路径，但知道这些的一开始就不会使用中文路径吧（

    而空格不能出现是因为你在有的时候用到文件路径的时候，比如在powershell中，空格是用于分割命令和命令的参数的，所以如果你忘了写引号或其他原因，很有可能导致出错。

2. 区分语言、编译器和IDE
    - 编程语言，如python, c++等，是人类可以理解的一种控制计算机工作的方式。
    - 编仪器，是用于把你写的代码翻译成电脑可以读懂且运行的程序。编仪器本身也是个程序。
    - IDE，集成开发环境。说白了就是一个具有代码补全、代码上色、调用编译器帮你编译等等功能的记事本（文本文档）罢了。

    > PS: 写这个是因为真的有人混淆了🤔

3. 选择什么IDE？
    **强烈不推荐使用IDLE，其它的各有优劣。**
    笔者在使用了Pycharm、Spyder、Visual Studio、IDEA、Mathematica、TexWorks，Typora等等之后全删掉用了VSCode搭建了上面所有语言的环境，所以笔者肯定推荐使用VSCode，当然其它的IDE也可以，具体可以询问任课老师以及按照机房有的来选择。
    > PS: 暂不能给你明确的答复，需要你自己衡量（doge）

4. 很多配置都涉及到环境变量？环境变量是什么？
    举个例子，按win+R，输入powershell并回车，你发现打开了powershell；输入edge或chrome并回车，打开了浏览器；但输入yuanshen并回车却打不开。
    同样地，在cmd或powershell中输入a.exe，你会发现除非你把路径设置到a.exe所在的文件夹，或者把a.exe的完整路径整个输入，是无法运行a.exe的。
    这是因为系统并不会主动去查你电脑里哪个犄角旮旯里放着这个文件，所以有时候无法简单地运行你想要的程序。
    而环境变量中写入的文件路径是系统会去查的路径，也就是放在环境变量里的程序是可以在任何地方方便而直接地调用的，比如python。
    > PS: 其实这里只涉及到环境变量中的PATH

5. 以下内容中出现卡顿或打不开，除非特殊说明，否则请尝试使用clash，详见WallessPKU。

## Python环境

### Python vs Anaconda

相信大家多少都对python有很多库可以帮助你实现功能有所了解，包括内置的，如functools；以及用户写的，如numpy。这些库有很多是未来的学习生活中会使用到的。而什么是anaconda？说白了就是一套提前安装好了很多常用库的一个打包好的python，比较方便，但不推荐使用，因为考试的时候OJ上没有这些库，故就不提供anaconda的下载方式了。

### Python with VSCode

#### 一、下载Python

1. 进入官网下载python，<https://www.python.org/>。鼠标悬停到Downloads上，随后点击下载官网最新版。或者点进Downloads，选择一个你喜欢的版本下载。
2. 运行下载的程序。勾选Add Python 3.x to PATH，让下载器帮你把python加入环境变量。
3. 点击Customize installation。Optional Features建议不变，直接点击next。
4. 修改安装位置，点击browse选择文件夹或者手敲路径，建议不要放在C盘。
5. 点击install等待下载。
6. 点击Disable path length limit，防止因为路径过长而无法运行python程序。这是因为windows系统对最长的文件路径是有一个奇怪的上限的，并且这个上限是被留存在Windows API中已经被各种软件所使用了。当然win 10之后，微软官方已经删除了许多软件和程序中的这个限制，但为了保持兼容性还没彻底删除。详见<https://learn.microsoft.com/zh-cn/windows/win32/fileio/maximum-file-path-limitation>
7. 打开powershell，输入python后回车，即可验证是否安装成功。若提示找不到python，可以先重启电脑保证环境变量成功被加入。若仍然失败，需要手动加入环境变量。
修改环境变量：
    - 直接在底部任务栏上的搜索框，搜索“编辑系统环境变量”
    - 点击“环境变量”，找到Path，选中后点击编辑
    - 点击新建，把python所在的文件夹路径输入，如：![pythonEnvPath](https://raw.githubusercontent.com/Usercyk/images/main/pythonEnvPath.png)
    - 一路点击确定或应用即可，如果没成功，重启电脑保证环境变量修改成功。

#### 二、下载VSCode

1. 官网下载VSCode，<https://code.visualstudio.com/>。
2. 运行下载器，类似上面的安装方式，不过要注意：
    - 尽量不要选择C盘
    - 添加到PATH
    - 注册为受支持的文件类型编辑器

    可选的选项有：
    - 创建桌面快捷方式：即创建桌面图标
    - 将“通过Code打开”添加到Windows资源管理器文件上下文菜单：右键文件时右键菜单里的操作
    - 将“通过Code打开”添加到Windows资源管理器文件上下文菜单：右键文件夹空白位置时菜单里的操作
3. 打开powershell，输入code回车，应该可以直接打开VSCode。

> PS: 看这个安装过程是不是很简单

#### 三、配置VSCode

1. 下载简体中文插件，点击插件图标。

    ![VSCodeExtensionPic](https://raw.githubusercontent.com/Usercyk/images/main/VSCodeExtensionPic.png)

    在输入框中输入chinese，下载插件。

    ![ChineseExtension](https://raw.githubusercontent.com/Usercyk/images/main/ChineseExtension.png)
2. 创建工作区Workspace
    在VSCode中，存在一个内置的用于分割不同配置、语言、插件等的划分系统，称为工作区。每个工作区中可以有和别的工作区不同的配置以及插件，这也和python的虚拟环境不谋而合。
    创建方式：
    - 点击左上角文件，关闭工作区。这一步实际上进入了一个默认的工作区。
    - 点击左上角文件，将工作区另存为，起一个你喜欢的名字并保存在你喜欢的位置上，不妨叫做PythonWS。
    - 点击左侧边栏最上面的图标（资源管理器），添加一个你喜欢的文件夹，之后就是在这个文件夹下进行工作。
3. 下载必要的Python插件
    Python, Pylance, Python Debugger, Python Indent, Code Runner, isort, autopep8。
4. 可选Python插件
    Qt for Python, Jupyter相关, autoDocstring, Better Comments。
5. 安装插件的过程中可能会弹出很多提示之类的，不用理这些，建议关掉VSCode后重启。
6. 终端-新建终端，输入：

    ```powershell
    python -m venv my_env
    ```

    即让python创建一个venv(virtual environment)，名字叫my_env。Python不同的虚拟环境之间安装的包是可以不同的，防止不同项目之间互相污染。随后关闭终端（点击垃圾桶图标）。
7. 在工作区文件夹（PythonWS）下随便新建一个.py文件，插件就会启动，点击右下角![VSCodeChoosePythonInterpreter](https://raw.githubusercontent.com/Usercyk/images/main/VSCodeChoosePythonInterpreter.png)，**选择虚拟环境中的那个python**。
8. 终端-新建终端，输入：

    ```powershell
    pip install autopep8
    ```

    这是让插件和vscode可以自动读取autopep8库运行的结果，从而帮你把你写的代码格式修改为PEP-8中的要求，即更好看。快捷键shift+alt+F可以帮你整理你的python代码。
9. 找到插件Code Runner，修改其设置，启用Run In Terminal选项。
10. 运行python代码时，第一次可能需要在右上角的三角运行框中选择Run Code，之后可以直接点击三角来运行。

    ![ChooseRunCode](https://raw.githubusercontent.com/Usercyk/images/main/ChooseRunCode.png)
    > PS: 其它的几个选项也可以运行/调试Python，但是很丑（

## C/Cpp环境

### C/Cpp with VSCode

#### 一、下载MinGW-w64

1. 官方github仓库：<https://github.com/niXman/mingw-builds-binaries/releases>，下载需要的版本，笔者选择了x86_64-14.2.0-release-posix-seh-ucrt-rt_v12-rev0.7z
2. 解压到你喜欢的位置，随后把bin文件夹添加到环境变量中，如
![MinGWEnvPath](https://raw.githubusercontent.com/Usercyk/images/main/MinGWEnvPath.png)
3. 打开powershell，输入

    ```powershell
    gcc -v
    ```

    没报错就成功了，否则先重启，仍不行则检查环境变量是否正确。

> PS: 比python下载简单多了

#### 二、配置VSCode

1. 下载方式见前
2. 下载Code Runner和C/C++ Extension Pack插件
3. 配置完成了！点击右上角三角选择使用Run Code运行即可，类似前面Python配置运行方式。
4. 中文输出乱码：
    - 打开Code Runner设置，编辑executorMap，将其中c和c++两项改为

    ```json
    "code-runner.executorMap": {
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt -fexec-charset=gbk && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt -fexec-charset=gbk && $dir$fileNameWithoutExt",
    }
    ```

    这会让GCC使用GBK编码进行编译，如果仍乱码，改成`utf-8`试试。

5. （可选）修改编译exe位置：
    - 打开Code Runner设置，编辑executorMap，将其中c和c++两项改为

    ```json
    "code-runner.executorMap": {
        "c": "cd $dir && gcc $fileName -D LOCAL -o .\\build\\$fileNameWithoutExt -fexec-charset=gbk && .\\build\\$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -D LOCAL -o .\\build\\$fileNameWithoutExt -fexec-charset=gbk && .\\build\\$fileNameWithoutExt",
    }
    ```

    这会让编译的exe文件保存至`build`文件夹下，使得项目显得比较顺眼。

> PS: 这个配置真的很简单吧
