# Java 包(package) | 菜鸟教程

> 来源: https://www.runoob.com/java/java-package.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java 包(package)
为了更好地组织类，Java 提供了包机制，用于区别类名的命名空间。
- 1、把功能相似或相关的类或接口组织在同一个包中，方便类的查找和使用。
1、把功能相似或相关的类或接口组织在同一个包中，方便类的查找和使用。
- 2、如同文件夹一样，包也采用了树形目录的存储方式。同一个包中的类名字是不同的，不同的包中的类的名字是可以相同的，当同时调用两个不同包中相同类名的类时，应该加上包名加以区别。因此，包可以避免名字冲突。
2、如同文件夹一样，包也采用了树形目录的存储方式。同一个包中的类名字是不同的，不同的包中的类的名字是可以相同的，当同时调用两个不同包中相同类名的类时，应该加上包名加以区别。因此，包可以避免名字冲突。
- 3、包也限定了访问权限，拥有包访问权限的类才能访问某个包中的类。
3、包也限定了访问权限，拥有包访问权限的类才能访问某个包中的类。
Java 使用包（package）这种机制是为了防止命名冲突，访问控制，提供搜索和定位类（class）、接口、枚举（enumerations）和注释（annotation）等。
包语句的语法格式为：
例如,一个Something.java 文件它的内容
那么它的路径应该是 net/java/util/Something.java 这样保存的。 package(包) 的作用是把不同的 java 程序分类保存，更方便的被其他 java 程序调用。
一个包（package）可以定义为一组相互联系的类型（类、接口、枚举和注释），为这些类型提供访问保护和命名空间管理的功能。
以下是一些 Java 中的包：
- java.lang -打包基础的类
- java.io -包含输入输出功能的函数
开发者可以自己把一组类和接口等打包，并定义自己的包。而且在实际开发中这样做是值得提倡的，当你自己完成类的实现之后，将相关的类分组，可以让其他的编程者更容易地确定哪些类、接口、枚举和注释等是相关的。
由于包创建了新的命名空间（namespace），所以不会跟其他包中的任何名字产生命名冲突。使用包这种机制，更容易实现访问控制，并且让定位相关类更加简单。
创建包的时候，你需要为这个包取一个合适的名字。之后，如果其他的一个源文件包含了这个包提供的类、接口、枚举或者注释类型的时候，都必须将这个包的声明放在这个源文件的开头。
包声明应该在源文件的第一行，每个源文件只能有一个包声明，这个文件中的每个类型都应用于它。
如果一个源文件中没有使用包声明，那么其中的类，函数，枚举，注释等将被放在一个无名的包（unnamed package）中。
让我们来看一个例子，这个例子创建了一个叫做animals的包。通常使用小写的字母来命名避免与类、接口名字的冲突。
在 animals 包中加入一个接口（interface）：

## Animal.java 文件代码：
接下来，在同一个包中加入该接口的实现：

## MammalInt.java 文件代码：
然后，编译这两个文件，并把他们放在一个叫做animals的子目录中。

用下面的命令来运行：

```

$ mkdir animals

$ cp Animal.class  MammalInt.class animals

$ java animals/MammalInt

Mammal eats

Mammal travel

```

## import 关键字
为了能够使用某一个包的成员，我们需要在 Java 程序中明确导入该包。
在 Java 中， import 关键字用于导入其他类或包中定义的类型，以便在当前源文件中使用这些类型。
import 关键字用于引入其他包中的类、接口或静态成员，它允许你在代码中直接使用其他包中的类，而不需要完整地指定类的包名。
在 java 源文件中 import 语句必须位于 Java 源文件的头部，其语法格式为：
import 语句位于 package 语句之后：
如果在一个包中，一个类想要使用本包中的另一个类，那么该包名可以省略。
可以使用 import语句来引入一个特定的类：

```

import com.runoob.MyClass;
```
这样，你就可以在当前源文件中直接使用 MyClass 类的方法、变量或常量。
也可以使用通配符 * 来引入整个包或包的子包：

```

import com.runoob.mypackage.*;
```
这样，你可以导入 com.runoob.mypackage 包中的所有类，从而在当前源文件中使用该包中的任何类的方法、变量或常量。注意，使用通配符 * 导入整个包时，只会导入包中的类，而不会导入包中的子包。
在导入类或包时，你需要提供类的完全限定名或包的完全限定名。完全限定名包括包名和类名的组合，以点号 . 分隔。
下面的 payroll 包已经包含了 Employee 类，接下来向 payroll 包中添加一个 Boss 类。Boss 类引用 Employee 类的时候可以不用使用 payroll 前缀，Boss 类的实例如下。

## Boss.java 文件代码：
如果 Boss 类不在 payroll 包中又会怎样？Boss 类必须使用下面几种方法之一来引用其他包中的类。
使用类全名描述，例如：
用 import 关键字引入，使用通配符 * ：
使用 import 关键字引入 Employee 类：
类文件中可以包含任意数量的 import 声明。import 声明必须在包声明之后，类声明之前。

## package 的目录结构
类放在包中会有两种主要的结果：
- 包名成为类名的一部分，正如我们前面讨论的一样。
- 包名必须与相应的字节码所在的目录结构相吻合。
下面是管理你自己 java 中文件的一种简单方式：
将类、接口等类型的源码放在一个文本中，这个文件的名字就是这个类型的名字，并以.java作为扩展名。例如：
接下来，把源文件放在一个目录中，这个目录要对应类所在包的名字。
现在，正确的类名和路径将会是如下样子：
- 类名 ->  vehicle.Car
类名 ->  vehicle.Car
- 路径名 ->   vehicle\Car.java (在 windows 系统中)
路径名 ->   vehicle\Car.java (在 windows 系统中)
通常，一个公司使用它互联网域名的颠倒形式来作为它的包名.例如：互联网域名是 runoob.com，所有的包名都以 com.runoob 开头。包名中的每一个部分对应一个子目录。
例如：有一个 com.runoob.test 的包，这个包包含一个叫做 Runoob.java 的源文件，那么相应的，应该有如下面的一连串子目录：
编译的时候，编译器为包中定义的每个类、接口等类型各创建一个不同的输出文件，输出文件的名字就是这个类型的名字，并加上 .class 作为扩展后缀。

例如：
现在，我们用-d选项来编译这个文件，如下：

```

$javac -d . Runoob.java

```
这样会像下面这样放置编译了的文件：

```

.\com\runoob\test\Runoob.class

.\com\runoob\test\Google.class

```
你可以像下面这样来导入所有 \com\runoob\test\ 中定义的类、接口等：

```

import com.runoob.test.*;

```
编译之后的 .class 文件应该和 .java 源文件一样，它们放置的目录应该跟包的名字对应起来。但是，并不要求 .class 文件的路径跟相应的 .java 的路径一样。你可以分开来安排源码和类的目录。

```

\sources\com\runoob\test\Runoob.java

\classes\com\runoob\test\Google.class

```
这样，你可以将你的类目录分享给其他的编程人员，而不用透露自己的源码。用这种方法管理源码和类文件可以让编译器和java 虚拟机（JVM）可以找到你程序中使用的所有类型。
类目录的绝对路径叫做 class path 。设置在系统变量 CLASSPATH 中。编译器和 java 虚拟机通过将 package 名字加到 class path 后来构造 .class 文件的路径。
\classes 是 class path，package 名字是 com.runoob.test,而编译器和 JVM 会在  \classes\com\runoob\test 中找 .class 文件。
一个 class path 可能会包含好几个路径，多路径应该用分隔符分开。默认情况下，编译器和 JVM 查找当前目录。JAR 文件按包含 Java 平台相关的类，所以他们的目录默认放在了 class path 中。

## 设置 CLASSPATH 系统变量
用下面的命令显示当前的CLASSPATH变量：
- Windows 平台（DOS 命令行下）：C:\> set CLASSPATH
- UNIX 平台（Bourne shell 下）：# echo $CLASSPATH
- Windows 平台（DOS 命令行下）：C:\> set CLASSPATH=
- UNIX 平台（Bourne shell 下）：# unset CLASSPATH; export CLASSPATH
设置CLASSPATH变量:
- Windows 平台（DOS 命令行下）： C:\> set CLASSPATH=C:\users\jack\java\classes
- UNIX 平台（Bourne shell 下）：# CLASSPATH=/home/jack/java/classes; export CLASSPATH

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