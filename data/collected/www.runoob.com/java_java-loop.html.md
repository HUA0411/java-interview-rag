# Java 循环结构 – for, while 及 do…while | 菜鸟教程

> 来源: https://www.runoob.com/java/java-loop.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java 循环结构 - for, while 及 do...while
顺序结构的程序语句只能被执行一次。
如果您想要同样的操作执行多次，就需要使用循环结构。
Java中有三种主要的循环结构：
- while 循环
- do…while 循环
在 Java5 中引入了一种主要用于数组的增强型 for 循环。

## while 循环
while是最基本的循环，它的结构为：
只要布尔表达式为 true，循环就会一直执行下去。

## Test.java 文件代码：
以上实例编译运行结果如下：

```

value of x : 10

value of x : 11

value of x : 12

value of x : 13

value of x : 14

value of x : 15

value of x : 16

value of x : 17

value of x : 18

value of x : 19

```

## do…while 循环
对于 while 语句而言，如果不满足条件，则不能进入循环。但有时候我们需要即使不满足条件，也至少执行一次。
do…while 循环和 while 循环相似，不同的是，do…while 循环至少会执行一次。

```

do {

//代码语句

}while(布尔表达式);

```
注意： 布尔表达式在循环体的后面，所以语句块在检测布尔表达式之前已经执行了。

如果布尔表达式的值为 true，则语句块一直执行，直到布尔表达式的值为 false。

## Test.java 文件代码：
以上实例编译运行结果如下：

```

value of x : 10

value of x : 11

value of x : 12

value of x : 13

value of x : 14

value of x : 15

value of x : 16

value of x : 17

value of x : 18

value of x : 19

```
虽然所有循环结构都可以用 while 或者 do...while表示，但 Java 提供了另一种语句 —— for 循环，使一些循环结构变得更加简单。
for循环执行的次数是在执行前就确定的。语法格式如下：
关于 for 循环有以下几点说明：
- 最先执行初始化步骤。可以声明一种类型，但可初始化一个或多个循环控制变量，也可以是空语句。
- 然后，检测布尔表达式的值。如果为 true，循环体被执行。如果为false，循环终止，开始执行循环体后面的语句。
- 执行一次循环后，更新循环控制变量。
- 再次检测布尔表达式。循环执行上面的过程。

## Test.java 文件代码：
以上实例编译运行结果如下：

```

value of x : 10

value of x : 11

value of x : 12

value of x : 13

value of x : 14

value of x : 15

value of x : 16

value of x : 17

value of x : 18

value of x : 19

```

## Java 增强 for 循环
Java5 引入了一种主要用于数组的增强型 for 循环。
Java 增强 for 循环语法格式如下:
声明语句： 声明新的局部变量，该变量的类型必须和数组元素的类型匹配。其作用域限定在循环语句块，其值与此时数组元素的值相等。
表达式： 表达式是要访问的数组名，或者是返回值为数组的方法。

## Test.java 文件代码：
以上实例编译运行结果如下：

```

10,20,30,40,50,

James,Larry,Tom,Lacy,

```

## break 关键字
break 主要用在循环语句或者 switch 语句中，用来跳出整个语句块。
break 跳出最里层的循环，并且继续执行该循环下面的语句。
break 的用法很简单，就是循环结构中的一条语句：

## Test.java 文件代码：
以上实例编译运行结果如下：

## continue 关键字
continue 适用于任何循环控制结构中。作用是让程序立刻跳转到下一次循环的迭代。
在 for 循环中，continue 语句使程序立即跳转到更新语句。
在 while 或者 do…while 循环中，程序立即跳转到布尔表达式的判断语句。
continue 就是循环体中一条简单的语句：

```

continue;

```

## Test.java 文件代码：
以上实例编译运行结果如下：

```

10

20

40

50

```

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