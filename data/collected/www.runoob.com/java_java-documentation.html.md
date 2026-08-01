# Java 文档注释 | 菜鸟教程

> 来源: https://www.runoob.com/java/java-documentation.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java 文档注释
Java 支持三种注释方式：
前两种分别是 // 和 /* */ ，第三种被称作文档注释，它以 /** 开始，以 */ 结束。
前两种注释内容可以参考： Java 注释
文档注释允许你在程序中嵌入关于程序的信息。
你可以使用 javadoc 工具软件来生成信息，并输出到 HTML 文件中。
文档注释，使你更加方便的记录你的程序信息。

## javadoc 标签
javadoc 工具软件识别以下标签：
标识一个类的作者
@author description
@deprecated
指名一个过期的类或成员
@deprecated description
{@docRoot}
指明当前文档根目录的路径
Directory Path
@exception
标志一个类抛出的异常
@exception exception-name explanation
{@inheritDoc}
从直接父类继承的注释
Inherits a comment from the immediate surperclass.
插入一个到另一个主题的链接
{@link name text}
{@linkplain}
插入一个到另一个主题的链接，但是该链接显示纯文本字体
Inserts an in-line link to another topic.
说明一个方法的参数
@param parameter-name explanation
@return explanation
指定一个到另一个主题的链接
@see anchor
说明一个序列化属性
@serial description
@serialData
说明通过writeObject( ) 和 writeExternal( )方法写的数据
@serialData description
@serialField
说明一个ObjectStreamField组件
@serialField name type description
标记当引入一个特定的变化时
@since release
和 @exception标签一样.
The @throws tag has the same meaning as the @exception tag.
{@value}
显示常量的值，该常量必须是static属性。
Displays the value of a constant, which must be a static field.
@version
@version info
在开始的 /** 之后，第一行或几行是关于类、变量和方法的主要描述。
之后，你可以包含一个或多个各种各样的 @ 标签。每一个 @ 标签必须在一个新行的开始或者在一行的开始紧跟星号 * 。
多个相同类型的标签应该放成一组。例如，如果你有三个 @see 标签，可以将它们一个接一个的放在一起。
下面是一个类的稳定注释的实例：

## javadoc 输出什么
javadoc 工具将你 Java 程序的源代码作为输入，输出一些包含你程序注释的HTML文件。
每一个类的信息将在独自的HTML文件里。javadoc 也可以输出继承的树形结构和索引。
由于 javadoc 的实现不同，工作也可能不同，你需要检查你的 Java 开发系统的版本等细节，选择合适的 Javadoc 版本。
下面是一个使用说明注释的简单实例。注意每一个注释都在它描述的项目的前面。
在经过 javadoc 处理之后，SquareNum 类的注释将在 SquareNum.html 中找到。

## SquareNum.java 文件代码：
如下，使用 javadoc 工具处理 SquareNum.java 文件：

```

$ javadoc SquareNum.java

Loading source file SquareNum.java...

Constructing Javadoc information...

Standard Doclet version 1.5.0_13

Building tree for all the packages and classes...

Generating SquareNum.html...

SquareNum.java:39: warning - @return tag cannot be used\

in method with void return type.

Generating package-frame.html...

Generating package-summary.html...

Generating package-tree.html...

Generating constant-values.html...

Building index for all the packages and classes...

Generating overview-tree.html...

Generating index-all.html...

Generating deprecated-list.html...

Building index for all classes...

Generating allclasses-frame.html...

Generating allclasses-noframe.html...

Generating index.html...

Generating help-doc.html...

Generating stylesheet.css...

1 warning

$

```

## 1  篇笔记 写笔记
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