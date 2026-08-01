# Java 开发环境配置 | 菜鸟教程

> 来源: https://www.runoob.com/java/java-environment-setup.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java 开发环境配置
在本章节中我们将为大家介绍如何搭建Java开发环境。
- Windows 上安装开发环境
- Linux 上安装开发环境
- Java IDE 介绍

## window系统安装java
首先我们需要下载 java 开发工具包 JDK，下载地址： https://www.oracle.com/java/technologies/downloads/ ，在下载页面中根据自己的系统选择对应的版本，本文以 Window 64位系统为例：
下载后 JDK 的安装根据提示进行，还有安装 JDK 的时候也会安装 JRE，一并安装就可以了。
安装JDK，安装过程中可以自定义安装目录等信息，例如我们选择安装目录为 C:\Program Files (x86)\Java\jdk1.8.0_91 。
1.安装完成后，右击"我的电脑"，点击"属性"，选择"高级系统设置"；
2.选择"高级"选项卡，点击"环境变量"；
然后就会出现如下图所示的画面：
在 "系统变量" 中设置 3 项属性，JAVA_HOME、PATH、CLASSPATH(大小写无所谓),若已存在则点击"编辑"，不存在则点击"新建"。
注意： 如果使用 1.5 以上版本的 JDK，不用设置 CLASSPATH 环境变量，也可以正常编译和运行 Java 程序。
注意： 如果使用 1.5 以上版本的 JDK，不用设置 CLASSPATH 环境变量，也可以正常编译和运行 Java 程序。
变量设置参数如下：
- 变量名： JAVA_HOME
- 变量值： C:\Program Files (x86)\Java\jdk1.8.0_91 // 要根据自己的实际路径配置
- 变量名： CLASSPATH
- 变量值： .;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar; //记得前面有个"."
- 变量名： Path
- 变量值： %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;

## JAVA_HOME 设置
注意： 在 Windows10 中，Path 变量里是分条显示的，我们需要将 %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin; 分开添加，否则无法识别： %JAVA_HOME%\bin;

%JAVA_HOME%\jre\bin; 更多内容可参考： Windows 10 配置Java 环境变量
注意： 在 Windows10 中，Path 变量里是分条显示的，我们需要将 %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin; 分开添加，否则无法识别：

```

%JAVA_HOME%\bin;

%JAVA_HOME%\jre\bin;

```
更多内容可参考： Windows 10 配置Java 环境变量

## CLASSPATH 设置
这是 Java 的环境配置，配置完成后，你可以启动 Eclipse 来编写代码，它会自动完成java环境的配置。

## 测试JDK是否安装成功
1、"开始"->"运行"，键入"cmd"；
2、键入命令: java -version 、 java 、 javac 几个命令，出现以下信息，说明环境变量配置成功；

## Linux，UNIX，Solaris，FreeBSD环境变量设置
环境变量PATH应该设定为指向Java二进制文件安装的位置。如果设置遇到困难，请参考shell文档。
例如，假设你使用bash作为shell，你可以把下面的内容添加到你的 .bashrc文件结尾: export PATH=/path/to/java:$PATH

## 流行 Java 开发工具
正所谓工欲善其事必先利其器，我们在开发 Java 语言过程中同样需要一款不错的开发工具，目前市场上的 IDE 很多，本文为大家推荐以下下几款 Java 开发工具：
- JetBrains 的 IDEA， 现在很多人开始使用了，功能很强大，下载地址： https://www.jetbrains.com/idea/download/
JetBrains 的 IDEA， 现在很多人开始使用了，功能很强大，下载地址： https://www.jetbrains.com/idea/download/
- VSCode : VSCode（全称：Visual Studio Code）是一款由微软开发且跨平台的免费源代码编辑器。 下载地址： https://code.visualstudio.com/ 安装教程： https://www.runoob.com/w3cnote/vscode-tutorial.html
VSCode : VSCode（全称：Visual Studio Code）是一款由微软开发且跨平台的免费源代码编辑器。
下载地址： https://code.visualstudio.com/
安装教程： https://www.runoob.com/w3cnote/vscode-tutorial.html
- Netbeans: 开源免费的 Java IDE，下载地址： https://www.netbeans.org/index.html
Netbeans: 开源免费的 Java IDE，下载地址： https://www.netbeans.org/index.html
- Eclipse: 另一个免费开源的 Java IDE，下载地址： https://www.eclipse.org/downloads/packages/ 选择 Eclipse IDE for Java Developers ：
Eclipse: 另一个免费开源的 Java IDE，下载地址： https://www.eclipse.org/downloads/packages/
选择 Eclipse IDE for Java Developers ：

## 使用 IntelliJ IDEA创建第一个 Java 应用
- 1、启动 IntelliJ IDEA。
- 2、在欢迎屏幕中单击"新建项目"。
- 3、在"新建项目"向导中，从左侧列表中选择"Java"。
- 4、为项目命名（例如 HelloWorld）并根据需要更改默认位置。
- 5、在本教程中，我们不会使用版本控制系统，因此请禁用"创建 Git 存储库"选项。
- 6、确保在构建系统中选择了 IntelliJ。
要在 IntelliJ IDEA 中开发 Java 应用程序，您需要 Java SDK (JDK)。
如果 IntelliJ IDEA 中已定义所需的 JDK，请从 JDK 列表中选择它。
如果您的计算机上安装了 JDK，但未在 IDE 中定义，请选择"添加 JDK"并指定 JDK 主目录的路径（例如，/Library/Java/JavaVirtualMachines/jdk-20.0.1.jdk）。
创建包和类，在项目工具窗口中，右键单击 src 文件夹，选择新建，然后选择 Java 类。
在名称字段中，输入 com.example.helloworld.HelloWorld 并点击确定，IntelliJ IDEA 将创建 com.example.helloworld 包和 HelloWorld 类。
写个输出 Hello World 的代码
执行代码，并输出结果：

## 使用 Eclipse 运行第一个 Java 程序
视频演示如下所示：
HelloWorld.java 文件代码：

## 5  篇笔记 写笔记
- Python / 数据科学 Python 教程 Python2.x 教程 FastAPI 教程 Flask 教程 Django 教程 NumPy 教程 Pandas 教程 SciPy 教程 Matplotlib 教程 Dash 教程 Jupyter Notebook 教程 Pillow 教程 量化交易 R 教程 Julia 教程
- Python 教程
- Python2.x 教程
- FastAPI 教程
- Flask 教程
- Django 教程
- NumPy 教程
- Pandas 教程
- SciPy 教程
- Matplotlib 教程
- Jupyter Notebook 教程
- Pillow 教程
- Julia 教程
- AI / 智能开发 AI Agent（智能体） AI（人工智能） Codex 教程 Vibe Coding 教程 Claude Code OpenCode Skills（技能） Ollama 教程 Hermes Agent Pi Agent AI 数学基础 TensorFlow 教程 PyTorch 教程 Scikit-learn 教程 机器 教程 LangChain 自然语言处理 NLP OpenCV 教程 Selenium 教程 Playwright 教程
- AI Agent（智能体）
- AI（人工智能）
- Codex 教程
- Vibe Coding 教程
- Claude Code
- OpenCode
- Skills（技能）
- Ollama 教程
- Hermes Agent
- Pi Agent
- TensorFlow 教程
- PyTorch 教程
- Scikit-learn 教程
- LangChain
- 自然语言处理 NLP
- OpenCV 教程
- Selenium 教程
- Playwright 教程
- 前端开发 HTML 教程 HTML5 教程 CSS 教程 CSS3 教程 JavaScript 教程 HTML DOM 教程 TypeScript 教程 AJAX 教程 JSON 教程 Tailwind CSS 教程 Bootstrap4 教程 Bootstrap5 教程 Foundation 教程 Vue.js 教程 Vue3 教程 React 教程 Next.js 教程 AngularJS 教程 Angular 教程 jQuery 教程 jQuery UI 教程 jQuery EasyUI 教程 ECharts 教程 Chart.js 教程 Highcharts 教程 Google 地图 教程 SVG 教程 Font Awesome 教程
- HTML5 教程
- JavaScript 教程
- HTML DOM 教程
- TypeScript 教程
- Tailwind CSS 教程
- Bootstrap4 教程
- Bootstrap5 教程
- Foundation 教程
- Vue.js 教程
- React 教程
- Next.js 教程
- AngularJS 教程
- Angular 教程
- jQuery 教程
- jQuery UI 教程
- jQuery EasyUI 教程
- ECharts 教程
- Chart.js 教程
- Highcharts 教程
- Google 地图 教程
- Font Awesome 教程
- 后端开发 Node.js 教程 Electron 教程 PHP 教程 Java 教程 Go 教程 Rust 教程 C# 教程 Servlet 教程 JSP 教程 ASP 教程 AppML 教程 VBScript 教程 Swagger 教程 RESTful API 教程 Docker 教程 Linux 教程 ZooKeeper 教程
- Node.js 教程
- Electron 教程
- Servlet 教程
- AppML 教程
- VBScript 教程
- Swagger 教程
- RESTful API 教程
- Docker 教程
- Linux 教程
- ZooKeeper 教程
- 数据库 SQL 教程 MySQL 教程 PostgreSQL 教程 SQLite 教程 MongoDB 教程 Redis 教程 Memcached 教程
- MySQL 教程
- PostgreSQL 教程
- SQLite 教程
- MongoDB 教程
- Redis 教程
- Memcached 教程
- 移动开发 Android 教程 Flutter 教程 Ionic 教程 jQuery Mobile 教程 Swift 教程 Kotlin 教程
- Android 教程
- Flutter 教程
- Ionic 教程
- jQuery Mobile 教程
- Swift 教程
- Kotlin 教程
- DevOps / 工程化 Git 教程 SVN 教程 CMake 教程 Maven 教程 VS Code 教程 Obsidian 教程 PyCharm 教程 Eclipse 教程 Markdown 教程
- CMake 教程
- Maven 教程
- VS Code 教程
- Obsidian 教程
- PyCharm 教程
- Eclipse 教程
- Markdown 教程
- 编程语言 C 教程 C++ 教程 Zig 教程 Scala 教程 Ruby 教程 Perl 教程 Lua 教程 Dart 教程 汇编语言 教程 Verilog 教程
- Scala 教程
- Verilog 教程
- 计算机基础 计算机组成原理 数据结构与算法 C 语言数据结构与算法 设计模式 Python 设计模式 正则表达式 HTTP 教程 TCP/IP 教程 网络协议 W3C 教程
- C 语言数据结构与算法
- Python 设计模式
- TCP/IP 教程
- XML / Web Service XML 教程 DTD 教程 XML DOM 教程 XSLT 教程 XPath 教程 XQuery 教程 XLink 教程 XPointer 教程 XML Schema 教程 XSL-FO 教程 Web Service 教程 WSDL 教程 SOAP 教程 RSS 教程 RDF 教程
- XML DOM 教程
- XPath 教程
- XQuery 教程
- XLink 教程
- XPointer 教程
- XML Schema 教程
- XSL-FO 教程
- Web Service 教程
- .NET ASP.NET 教程 MVC 教程 Razor 教程 Web Forms 教程 Web Pages 教程 PowerShell 教程
- ASP.NET 教程
- Razor 教程
- Web Forms 教程
- Web Pages 教程
- PowerShell 教程
- 网站建设 网站建设指南 浏览器信息 网站主机教程 网站品质