# Java 流(Stream)、文件(File)和IO | 菜鸟教程

> 来源: https://www.runoob.com/java/java-files-io.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java 流(Stream)、文件(File)和IO
Java 中的流（Stream）、文件（File）和 IO（输入输出）是处理数据读取和写入的基础设施，它们允许程序与外部数据（如文件、网络、系统输入等）进行交互。
java.io 包是 Java 标准库中的一个核心包，提供了用于系统输入和输出的类，它包含了处理数据流（字节流和字符流）、文件读写、序列化以及数据格式化的工具。
java.io 是处理文件操作、流操作以及低级别 IO 操作的基础包。
java.io 包中的流支持很多种格式，比如：基本类型、对象、本地化字符集等等。
一个流可以理解为一个数据的序列。输入流表示从一个源读取数据，输出流表示向一个目标写数据。
Java 的控制台输入由 System.in 完成。
为了获得一个绑定到控制台的字符流，你可以把 System.in 包装在一个 BufferedReader 对象中来创建一个字符流。
下面是创建 BufferedReader 的基本语法：
BufferedReader 对象创建后，我们便可以使用 read() 方法从控制台读取一个字符，或者用 readLine() 方法读取一个字符串。

## 从控制台读取多字符输入
从 BufferedReader 对象读取一个字符要使用 read() 方法，它的语法如下：
每次调用 read() 方法，它从输入流读取一个字符并把该字符作为整数值返回。 当流结束的时候返回 -1。该方法抛出 IOException。
下面的程序示范了用 read() 方法从控制台不断读取字符直到用户输入 q 。

## BRRead.java 文件代码：
以上实例编译运行结果如下:

```

输入字符, 按下 'q' 键退出。

runoob

r

u

n

o

o

b

q

q

```

## 从控制台读取字符串
从标准输入读取一个字符串需要使用 BufferedReader 的 readLine() 方法。
它的一般格式是：
下面的程序读取和显示字符行直到你输入了单词"end"。

## BRReadLines.java 文件代码：
以上实例编译运行结果如下:

```

Enter lines of text.

Enter 'end' to quit.

This is line one

This is line one

This is line two

This is line two

end

end

```
JDK 5 后的版本我们也可以使用 Java Scanner 类来获取控制台的输入。
JDK 5 后的版本我们也可以使用 Java Scanner 类来获取控制台的输入。
在此前已经介绍过，控制台的输出由 print( ) 和 println() 完成。这些方法都由类 PrintStream 定义，System.out 是该类对象的一个引用。
PrintStream 继承了 OutputStream类，并且实现了方法 write()。这样，write() 也可以用来往控制台写操作。
PrintStream 定义 write() 的最简单格式如下所示：
该方法将 byteval 的低八位字节写到流中。
下面的例子用 write() 把字符 "A" 和紧跟着的换行符输出到屏幕：

## WriteDemo.java 文件代码：
运行以上实例在输出窗口输出 "A" 字符
注意： write() 方法不经常使用，因为 print() 和 println() 方法用起来更为方便。
如前所述，一个流被定义为一个数据序列。输入流用于从源读取数据，输出流用于向目标写数据。
下图是一个描述输入流和输出流的类层次图。

## 字节流（处理二进制数据）
字节流用于处理二进制数据，例如文件、图像、视频等。
InputStream
抽象类 (输入流)
所有字节输入流的超类，处理字节的输入操作。
OutputStream
抽象类 (输出流)
所有字节输出流的超类，处理字节的输出操作。
FileInputStream
从文件中读取字节数据。
FileOutputStream
将字节数据写入文件。
BufferedInputStream
为字节输入流提供缓冲功能，提高读取效率。
BufferedOutputStream
为字节输出流提供缓冲功能，提高写入效率。
ByteArrayInputStream
将内存中的字节数组作为输入源。
ByteArrayOutputStream
将数据写入到内存中的字节数组。
DataInputStream
允许从输入流中读取 Java 原生数据类型（如 int 、 float 、 boolean ）。
DataOutputStream
允许向输出流中写入 Java 原生数据类型。
ObjectInputStream
从输入流中读取序列化对象。
ObjectOutputStream
将对象序列化并写入输出流中。
PipedInputStream
用于在管道中读取字节数据，通常与 PipedOutputStream 配合使用。
PipedOutputStream
用于在管道中写入字节数据，通常与 PipedInputStream 配合使用。
FilterInputStream
字节输入流的包装类，用于对其他输入流进行过滤处理。
FilterOutputStream
字节输出流的包装类，用于对其他输出流进行过滤处理。
SequenceInputStream
将多个输入流串联为一个输入流进行处理。

## 字符流（处理文本数据）
字符流用于处理文本数据，例如读取和写入字符串或文件。
抽象类 (输入流)
所有字符输入流的超类，处理字符的输入操作。
抽象类 (输出流)
所有字符输出流的超类，处理字符的输出操作。
FileReader
从文件中读取字符数据。
FileWriter
将字符数据写入文件。
BufferedReader
为字符输入流提供缓冲功能，支持按行读取，提高读取效率。
BufferedWriter
为字符输出流提供缓冲功能，支持按行写入，提高写入效率。
CharArrayReader
将字符数组作为输入源。
CharArrayWriter
将数据写入到字符数组。
StringReader
将字符串作为输入源。
StringWriter
将数据写入到字符串缓冲区。
PrintWriter
便捷的字符输出流，支持自动刷新和格式化输出。
PipedReader
用于在管道中读取字符数据，通常与 PipedWriter 配合使用。
PipedWriter
用于在管道中写入字符数据，通常与 PipedReader 配合使用。
LineNumberReader
带行号的缓冲字符输入流，允许跟踪读取的行号。
PushbackReader
允许在读取字符后将字符推回流中，以便再次读取。

## 辅助类（其他重要类）
辅助类提供对文件、目录以及随机文件访问的支持。
用于表示文件或目录，并提供文件操作，如创建、删除、重命名等。
RandomAccessFile
支持文件的随机访问，可以从文件的任意位置读写数据。
提供对系统控制台的输入和输出支持。
下面将要讨论的两个重要的流是 FileInputStream 和 FileOutputStream 。

## FileInputStream
该流用于从文件读取数据，它的对象可以用关键字 new 来创建。
有多种构造方法可用来创建对象。
可以使用字符串类型的文件名来创建一个输入流对象来读取文件：
也可以使用一个文件对象来创建一个输入流对象来读取文件。我们首先得使用 File() 方法来创建一个文件对象：
创建了 InputStream 对象，就可以使用下面的方法来读取流或者进行其他的流操作。
int read()
读取一个字节的数据，返回值为 0 到 255 之间的整数。如果到达流的末尾，返回 -1。
int data = inputStream.read();
int read(byte[] b)
从输入流中读取字节，并将其存储在字节数组 b 中，返回实际读取的字节数。如果到达流的末尾，返回 -1。
byte[] buffer = new byte[1024]; int bytesRead = inputStream.read(buffer);
int read(byte[] b, int off, int len)
从输入流中读取最多 len 个字节，并将它们存储在字节数组 b 的 off 偏移位置，返回实际读取的字节数。如果到达流的末尾，返回 -1。
byte[] buffer = new byte[1024]; int bytesRead = inputStream.read(buffer, 0, buffer.length);
long skip(long n)
跳过并丢弃输入流中的 n 个字节，返回实际跳过的字节数。
long skippedBytes = inputStream.skip(100);
int available()
返回可以读取的字节数（不阻塞）。
int availableBytes = inputStream.available();
void close()
关闭输入流并释放与该流相关的所有资源。
inputStream.close();
void mark(int readlimit)
在流中的当前位置设置标记， readlimit 是可以读取的字节数上限。
inputStream.mark(1024);
void reset()
将流重新定位到上次标记的位置，如果没有标记或标记失效，抛出 IOException 。
inputStream.reset();
boolean markSupported()
检查当前输入流是否支持 mark() 和 reset() 操作。
boolean isMarkSupported = inputStream.markSupported();
除了 InputStream 外，还有一些其他的输入流，更多的细节参考下面链接：
- ByteArrayInputStream
- DataInputStream

## FileOutputStream
该类用来创建一个文件并向文件中写数据。
如果该流在打开文件进行输出前，目标文件不存在，那么该流会创建该文件。
有两个构造方法可以用来创建 FileOutputStream 对象。
使用字符串类型的文件名来创建一个输出流对象：
也可以使用一个文件对象来创建一个输出流来写文件。我们首先得使用File()方法来创建一个文件对象：
创建 OutputStream 对象完成后，就可以使用下面的方法来写入流或者进行其他的流操作。
void write(int b)
将指定的字节写入输出流， b 的低 8 位将被写入流中。
outputStream.write(255);
void write(byte[] b)
将字节数组 b 中的所有字节写入输出流。
byte[] data = "Hello".getBytes(); outputStream.write(data);
void write(byte[] b, int off, int len)
将字节数组 b 中从偏移量 off 开始的 len 个字节写入输出流。
byte[] data = "Hello".getBytes(); outputStream.write(data, 0, data.length);
void flush()
刷新输出流并强制写出所有缓冲的数据，确保数据被立即写入目标输出。
outputStream.flush();
void close()
关闭输出流并释放与该流相关的所有资源。关闭后不能再写入。
outputStream.close();
除了 OutputStream 外，还有一些其他的输出流，更多的细节参考下面链接：
- ByteArrayOutputStream
- DataOutputStream
下面是一个演示 InputStream 和 OutputStream 用法的例子：

## fileStreamTest.java 文件代码：
上面的程序首先创建文件test.txt，并把给定的数字以二进制形式写进该文件，同时输出到控制台上。
以上代码由于是二进制写入，可能存在乱码，你可以使用以下代码实例来解决乱码问题：

## fileStreamTest2.java 文件代码：
还有一些关于文件和I/O的类，我们也需要知道：
- File Class(类)
- FileReader Class(类)
- FileWriter Class(类)

## Java中的目录
File类中有两个方法可以用来创建文件夹：
- mkdir( ) 方法创建一个文件夹，成功则返回true，失败则返回false。失败表明File对象指定的路径已经存在，或者由于整个路径还不存在，该文件夹不能被创建。
- mkdirs() 方法创建一个文件夹和它的所有父文件夹。
下面的例子创建 "/tmp/user/java/bin"文件夹：

## CreateDir.java 文件代码：
编译并执行上面代码来创建目录 "/tmp/user/java/bin"。
注意： Java 在 UNIX 和 Windows 自动按约定分辨文件路径分隔符。如果你在 Windows 版本的 Java 中使用分隔符 (/) ，路径依然能够被正确解析。
一个目录其实就是一个 File 对象，它包含其他文件和文件夹。
如果创建一个 File 对象并且它是一个目录，那么调用 isDirectory() 方法会返回 true。
可以通过调用该对象上的 list() 方法，来提取它包含的文件和文件夹的列表。
下面展示的例子说明如何使用 list() 方法来检查一个文件夹中包含的内容：

## DirList.java 文件代码：
以上实例编译运行结果如下：

```

bin 是一个目录

lib 是一个目录

demo 是一个目录

test.txt 是一个文件

README 是一个文件

index.html 是一个文件

include 是一个目录

```
删除文件可以使用 java.io.File.delete() 方法。
以下代码会删除目录 /tmp/java/ ，需要注意的是当删除某一目录时，必须保证该目录下没有其他文件才能正确删除，否则将删除失败。

```

/tmp/java/

|-- 1.log

|-- test

```

## DeleteFileDemo.java 文件代码：

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