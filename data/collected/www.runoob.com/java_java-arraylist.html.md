# Java ArrayList | 菜鸟教程

> 来源: https://www.runoob.com/java/java-arraylist.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java ArrayList
Java 集合框架
ArrayList 类是一个可以动态修改的数组，与普通数组的区别就是它是没有固定大小的限制，我们可以添加或删除元素。
ArrayList 继承了 AbstractList ，并实现了 List 接口。
ArrayList 类位于 java.util 包中，使用前需要引入它，语法格式如下：

```

import java.util.ArrayList; // 引入 ArrayList 类

ArrayList objectName =new ArrayList<>();　 // 初始化

```
- E : 泛型数据类型，用于设置 objectName 的数据类型， 只能为引用数据类型 。
- objectName : 对象名。
ArrayList 是一个数组队列，提供了相关的添加、删除、修改、遍历等功能。
ArrayList 类提供了很多有用的方法，添加元素到 ArrayList 可以使用 add() 方法:
以上实例，执行输出结果为：

```
[Google, Runoob, Taobao, Weibo]
```
访问  ArrayList 中的元素可以使用 get() 方法：
注意 ：数组的索引值从 0 开始。
以上实例，执行输出结果为：
如果要修改  ArrayList 中的元素可以使用 set() 方法， set(int index, E element) 方法的第一个参数是索引（index），表示要替换的元素的位置，第二个参数是新元素（element），表示要设置的新值：
以上实例，执行输出结果为：

```

[Google, Runoob, Wiki, Weibo]
```
如果要删除  ArrayList 中的元素可以使用 remove() 方法：
以上实例，执行输出结果为：

```

[Google, Runoob, Taobao]
```
如果要计算  ArrayList 中的元素数量可以使用 size() 方法：
以上实例，执行输出结果为：
我们可以使用 for 来迭代数组列表中的元素：
以上实例，执行输出结果为：

```

Google

Runoob

Taobao

Weibo
```
也可以使用 for-each 来迭代元素：
以上实例，执行输出结果为：

```

Google

Runoob

Taobao

Weibo
```
ArrayList 中的元素实际上是对象，在以上实例中，数组列表元素都是字符串 String 类型。
如果我们要存储其他类型，而  只能为引用数据类型，这时我们就需要使用到基本类型的包装类。
基本类型对应的包装类表如下：
Character
此外，BigInteger、BigDecimal 用于高精度的运算，BigInteger 支持任意精度的整数，也是引用类型，但它们没有相对应的基本类型。

```
ArrayList li=new ArrayList<>();     // 存放整数元素

ArrayList li=new ArrayList<>();   // 存放字符元素
```
以下实例使用 ArrayList 存储数字(使用 Integer 类型):
以上实例，执行输出结果为：

```

10

15

20

25
```

## ArrayList 排序
Collections 类也是一个非常有用的类，位于 java.util 包中，提供的 sort() 方法可以对字符或数字列表进行排序。
以下实例对字母进行排序：
以上实例，执行输出结果为：

```

Google

Runoob

Taobao

Weibo

Wiki
```
以下实例对数字进行排序：
以上实例，执行输出结果为：

```

8

12

15

20

33

34
```

## Java ArrayList 方法
Java ArrayList 常用方法列表如下：
将元素插入到指定位置的 arraylist 中
addAll()
添加集合中的所有元素到 arraylist 中
删除 arraylist 中的所有元素
复制一份 arraylist
contains()
判断元素是否在 arraylist
通过索引值获取 arraylist 中的元素
indexOf()
返回 arraylist 中元素的索引值
removeAll()
删除存在于指定集合中的 arraylist 里的所有元素
remove()
删除 arraylist 里的单个元素
返回 arraylist 里元素数量
isEmpty()
判断 arraylist 是否为空
subList()
截取部分 arraylist 的元素
替换 arraylist 中指定索引的元素
对 arraylist 元素进行排序
toArray()
将 arraylist 转换为数组
toString()
将 arraylist 转换为字符串
ensureCapacity ()
设置指定容量大小的 arraylist
lastIndexOf()
返回指定元素在 arraylist 中最后一次出现的位置
retainAll()
保留 arraylist 中在指定集合中也存在的那些元素
containsAll()
查看 arraylist 是否包含指定集合中的所有元素
trimToSize()
将 arraylist 中的容量调整为数组中的元素个数
removeRange()
删除 arraylist 中指定索引之间存在的元素
replaceAll()
将给定的操作内容替换掉数组中每一个元素
removeIf()
删除所有满足特定条件的 arraylist 元素
forEach()
遍历 arraylist 中每一个元素并执行特定操作
更多 API 方法可以查看： https://www.runoob.com/manual/jdk11api/java.base/java/util/ArrayList.html
Java 集合框架

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