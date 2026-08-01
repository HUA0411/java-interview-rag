# Java HashMap | 菜鸟教程

> 来源: https://www.runoob.com/java/java-hashmap.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java HashMap
Java 集合框架
HashMap 是一个散列表，它存储的内容是键值对(key-value)映射。
HashMap 实现了 Map 接口，根据键的 HashCode 值存储数据，具有很快的访问速度，最多允许一条记录的键为 null，不支持线程同步。
HashMap 是无序的，即不会记录插入的顺序。
HashMap 继承于AbstractMap，实现了 Map、Cloneable、java.io.Serializable 接口。
HashMap 的 key 与 value 类型可以相同也可以不同，可以是字符串（String）类型的 key 和 value，也可以是整型（Integer）的 key 和字符串（String）类型的 value。
HashMap 中的元素实际上是对象，一些常见的基本类型可以使用它的包装类。
基本类型对应的包装类表如下：
Character
HashMap 类位于 java.util 包中，使用前需要引入它，语法格式如下：

```
import java.util.HashMap; // 引入 HashMap 类
```
以下实例我们创建一个 HashMap 对象 Sites， 整型（Integer）的 key 和字符串（String）类型的 value：

```
HashMap Sites = new HashMap();
```
HashMap 类提供了很多有用的方法，添加键值对(key-value)可以使用 put() 方法:
执行以上代码，输出结果如下：

```
{1=Google, 2=Runoob, 3=Taobao, 4=Zhihu}
```
以下实例创建一个字符串（String）类型的 key 和字符串（String）类型的 value：
执行以上代码，输出结果如下：

```
{four=Zhihu, one=Google, two=Runoob, three=Taobao}
```
我们可以使用 get(key) 方法来获取 key 对应的 value:
执行以上代码，输出结果如下：
我们可以使用 remove(key) 方法来删除 key 对应的键值对(key-value):
执行以上代码，输出结果如下：

```
{1=Google, 2=Runoob, 3=Taobao}
```
删除所有键值对(key-value)可以使用 clear 方法：
执行以上代码，输出结果如下：
如果要计算 HashMap 中的元素数量可以使用 size() 方法：
执行以上代码，输出结果如下：

## 迭代 HashMap
可以使用 for-each 来迭代 HashMap 中的元素。
如果你只想获取 key，可以使用 keySet() 方法，然后可以通过 get(key) 获取对应的 value，如果你只想获取 value，可以使用 values() 方法。
执行以上代码，输出结果如下：

```

key: 1 value: Google

key: 2 value: Runoob

key: 3 value: Taobao

key: 4 value: Zhihu

Google, Runoob, Taobao, Zhihu,

```

## Java HashMap 方法
Java HashMap 常用方法列表如下：
删除 hashMap 中的所有键/值对
复制一份 hashMap
isEmpty()
判断 hashMap 是否为空
计算 hashMap 中键/值对的数量
将键/值对添加到 hashMap 中
putAll()
将所有键/值对添加到 hashMap 中
putIfAbsent()
如果 hashMap 中不存在指定的键，则将指定的键/值对插入到 hashMap 中。
remove()
删除 hashMap 中指定键 key 的映射关系
containsKey()
检查 hashMap 中是否存在指定的 key 对应的映射关系。
containsValue()
检查 hashMap 中是否存在指定的 value 对应的映射关系。
replace()
替换 hashMap 中是指定的 key 对应的 value。
replaceAll()
将 hashMap 中的所有映射关系替换成给定的函数所执行的结果。
获取指定 key 对应对 value
getOrDefault()
获取指定 key 对应对 value，如果找不到 key ，则返回设置的默认值
forEach()
对 hashMap 中的每个映射执行指定的操作。
entrySet()
返回 hashMap 中所有映射项的集合集合视图。
keySet ()
返回 hashMap 中所有 key 组成的集合视图。
values()
返回 hashMap 中存在的所有 value 值。
添加键值对到 hashMap 中
compute()
对 hashMap 中指定 key 的值进行重新计算
computeIfAbsent()
对 hashMap 中指定 key 的值进行重新计算，如果不存在这个 key，则添加到 hashMap 中
computeIfPresent()
对 hashMap 中指定 key 的值进行重新计算，前提是该 key 存在于 hashMap 中。
更多 API 方法可以查看： https://www.runoob.com/manual/jdk11api/java.base/java/util/HashMap.html
Java 集合框架
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