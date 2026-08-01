# Java LinkedList | 菜鸟教程

> 来源: https://www.runoob.com/java/java-linkedlist.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java LinkedList
Java 集合框架
链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是并不会按线性的顺序存储数据，而是在每一个节点里存到下一个节点的地址。
链表可分为单向链表和双向链表。
一个单向链表包含两个值: 当前节点的值和一个指向下一个节点的链接。
一个双向链表有三个整数值: 数值、向后的节点链接、向前的节点链接。
Java LinkedList（链表） 类似于 ArrayList，是一种常用的数据容器。
与 ArrayList 相比，LinkedList 的增加和删除的操作效率更高，而查找和修改的操作效率较低。
以下情况使用 ArrayList :
- 频繁访问列表中的某一个元素。
- 只需要在列表末尾进行添加和删除元素操作。
以下情况使用 LinkedList :
- 你需要通过循环迭代来访问列表中的某些元素。
- 需要频繁的在列表开头、中间、末尾等位置进行添加和删除元素操作。
LinkedList 继承了 AbstractSequentialList 类。
LinkedList 实现了 Queue 接口，可作为队列使用。
LinkedList 实现了 List 接口，可进行列表的相关操作。
LinkedList 实现了 Deque 接口，可作为队列使用。
LinkedList 实现了 Cloneable 接口，可实现克隆。
LinkedList 实现了 java.io.Serializable 接口，即可支持序列化，能通过序列化去传输。
LinkedList 类位于 java.util 包中，使用前需要引入它，语法格式如下：

```

// 引入 LinkedList 类

import java.util.LinkedList;

LinkedList list = new LinkedList();   // 普通创建方法

或者

LinkedList list = new LinkedList(Collection c); // 使用集合创建链表
```
创建一个简单的链表实例：
以上实例，执行输出结果为：

```
[Google, Runoob, Taobao, Weibo]
```
更多的情况下我们使用 ArrayList 访问列表中的随机元素更加高效，但以下几种情况 LinkedList 提供了更高效的方法。
在列表开头添加元素：
以上实例，执行输出结果为：

```
[Wiki, Google, Runoob, Taobao]
```
在列表结尾添加元素：
以上实例，执行输出结果为：

```
[Google, Runoob, Taobao, Wiki]
```
在列表开头移除元素：
以上实例，执行输出结果为：

```
[Runoob, Taobao, Weibo]
```
在列表结尾移除元素：
以上实例，执行输出结果为：

```
[Google, Runoob, Taobao]
```
获取列表开头的元素：
以上实例，执行输出结果为：
获取列表结尾的元素：
以上实例，执行输出结果为：
我们可以使用 for 配合 size() 方法来迭代列表中的元素：
size() 方法用于计算链表的大小。
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
public boolean add(E e)
链表末尾添加元素，返回是否成功，成功为 true，失败为 false。
public void add(int index, E element)
向指定位置插入元素。
public boolean addAll(Collection extends E> c)
将一个集合的所有元素添加到链表后面，返回是否成功，成功为 true，失败为 false。
public boolean addAll(int index, Collection extends E> c)
将一个集合的所有元素添加到链表的指定位置后面，返回是否成功，成功为 true，失败为 false。
public void addFirst(E e)
元素添加到头部。
public void addLast(E e)
元素添加到尾部。
public boolean offer(E e)
向链表末尾添加元素，返回是否成功，成功为 true，失败为 false。
public boolean offerFirst(E e)
头部插入元素，返回是否成功，成功为 true，失败为 false。
public boolean offerLast(E e)
尾部插入元素，返回是否成功，成功为 true，失败为 false。
public void clear()
public E removeFirst()
删除并返回第一个元素。
public E removeLast()
删除并返回最后一个元素。
public boolean remove(Object o)
删除某一元素，返回是否成功，成功为 true，失败为 false。
public E remove(int index)
删除指定位置的元素。
public E poll()
删除并返回第一个元素。
public E remove()
删除并返回第一个元素。
public boolean contains(Object o)
判断是否含有某一元素。
public E get(int index)
返回指定位置的元素。
public E getFirst()
返回第一个元素。
public E getLast()
返回最后一个元素。
public int indexOf(Object o)
查找指定元素从前往后第一次出现的索引。
public int lastIndexOf(Object o)
查找指定元素最后一次出现的索引。
public E peek()
返回第一个元素。
public E element()
返回第一个元素。
public E peekFirst()
public E peekLast()
public E set(int index, E element)
设置指定位置的元素。
public Object clone()
public Iterator descendingIterator()
返回倒序迭代器。
public int size()
返回链表元素个数。
public ListIterator listIterator(int index)
返回从指定位置开始到末尾的迭代器。
public Object[] toArray()
返回一个由链表元素组成的数组。
public T[] toArray(T[] a)
返回一个由链表元素转换类型而成的数组。
更多 API 方法可以查看： https://www.runoob.com/manual/jdk11api/java.base/java/util/LinkedList.html
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