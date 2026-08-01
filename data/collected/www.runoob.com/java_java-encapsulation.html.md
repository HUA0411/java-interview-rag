# Java 封装 | 菜鸟教程

> 来源: https://www.runoob.com/java/java-encapsulation.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程
在面向对象程式设计方法中，封装（英语：Encapsulation）是指一种将抽象性函式接口的实现细节部分包装、隐藏起来的方法。
封装可以被认为是一个保护屏障，防止该类的代码和数据被外部类定义的代码随机访问。
要访问该类的代码和数据，必须通过严格的接口控制。
封装最主要的功能在于我们能修改自己的实现代码，而不用修改那些调用我们代码的程序片段。
适当的封装可以让程式码更容易理解与维护，也加强了程式码的安全性。
- 1. 良好的封装能够减少耦合。
1. 良好的封装能够减少耦合。
- 2. 类内部的结构可以自由修改。
2. 类内部的结构可以自由修改。
- 3. 可以对成员变量进行更精确的控制。
3. 可以对成员变量进行更精确的控制。
- 4. 隐藏信息，实现细节。
4. 隐藏信息，实现细节。

## 实现Java封装的步骤
1. 修改属性的可见性来限制对属性的访问（一般限制为private），例如：
这段代码中，将 name 和 age 属性设置为私有的，只能本类才能访问，其他类都访问不了，如此就对信息进行了隐藏。
2. 对每个值属性提供对外的公共方法访问，也就是创建一对赋取值方法，用于对私有属性的访问，例如：
采用 this 关键字是为了解决实例变量（private String name）和局部变量（setName(String name)中的name变量）之间发生的同名的冲突。
让我们来看一个java封装类的例子：

## EncapTest.java 文件代码：
以上实例中public方法是外部类访问该类成员变量的入口。
通常情况下，这些方法被称为getter和setter方法。
因此，任何要访问类中私有成员变量的类都要通过这些getter和setter方法。
通过如下的例子说明EncapTest类的变量怎样被访问：

## RunEncap.java 文件代码：
以上代码编译运行结果如下:

```

Name : James Age : 20

```
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