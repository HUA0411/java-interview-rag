# Java Number & Math 类 | 菜鸟教程

> 来源: https://www.runoob.com/java/java-number.html

## 菜鸟教程 -- 学的不仅是技术，更是梦想！

## Java 面向对象

## Java 高级教程

## Java Number & Math 类

## Java Number
一般地，当需要使用数字的时候，我们通常使用内置数据类型，如： byte、int、long、double 等。
然而，在实际开发过程中，我们经常会遇到需要使用对象，而不是内置数据类型的情形。为了解决这个问题，Java 语言为每一个内置数据类型提供了对应的包装类。
所有的包装类 （Integer、Long、Byte、Double、Float、Short） 都是抽象类 Number 的子类。
单精度浮点型包装类
双精度浮点型包装类
BigInteger
不可变任意精度整数
BigDecimal
不可变任意精度有符号十进制数
这种由编译器特别支持的包装称为装箱，所以当内置数据类型被当作对象使用的时候，编译器会把内置类型装箱为包装类。相似的，编译器也可以把一个对象拆箱为内置类型。
Number 类属于 java.lang 包。
Number 是一个抽象类，主要作用是为各种数值类型提供统一的转换方法：
下面是一个使用 Integer 对象的实例：

## Test.java 文件代码：
以上实例编译运行结果如下：
当 x 被赋为整型值时，由于x是一个对象，所以编译器要对x进行装箱。然后，为了使x能进行加运算，所以要对x进行拆箱。
Java 5+ 支持自动转换：

## Java Math 类
Math 类是 Java 提供的数学工具类，位于 java.lang 包中，包含执行基本数值运算的静态方法。
Java 的 Math 包含了用于执行基本数学运算的属性和方法，如初等指数、对数、平方根和三角函数。
Math 的方法都被定义为 static 形式，通过 Math 类可以在主函数中直接调用。

## Test.java 文件代码：
以上实例编译运行结果如下：

```

90 度的正弦值：1.0

0度的余弦值：1.0

60度的正切值：1.7320508075688767

1的反正切值： 0.7853981633974483

π/2的角度值：90.0

3.141592653589793

```

## 1. 指数对数运算

## 2. 随机数生成

## Number & Math 类方法
下面的表中列出的是 Number & Math 类常用的一些方法：
xxxValue() 将 Number 对象转换为xxx数据类型的值并返回。
compareTo() 将number对象与参数比较。
equals() 判断number对象是否与参数相等。
valueOf() 返回一个 Number 对象指定的内置数据类型
toString() 以字符串形式返回值。
parseInt() 将字符串解析为int类型。
abs() 返回参数的绝对值。
ceil() 返回大于等于( >= )给定参数的的最小整数，类型为双精度浮点型。
floor() 返回小于等于（<=）给定参数的最大整数 。
rint() 返回与参数最接近的整数。返回类型为double。
round() 它表示 四舍五入 ，算法为 Math.floor(x+0.5) ，即将原来的数字加上 0.5 后再向下取整，所以，Math.round(11.5) 的结果为12，Math.round(-11.5) 的结果为-11。
min() 返回两个参数中的最小值。
max() 返回两个参数中的最大值。
exp() 返回自然数底数e的参数次方。
log() 返回参数的自然数底数的对数值。
pow() 返回第一个参数的第二个参数次方。
sqrt() 求参数的算术平方根。
sin() 求指定double类型参数的正弦值。
cos() 求指定double类型参数的余弦值。
tan() 求指定double类型参数的正切值。
asin() 求指定double类型参数的反正弦值。
acos() 求指定double类型参数的反余弦值。
atan() 求指定double类型参数的反正切值。
atan2() 将笛卡尔坐标转换为极坐标，并返回极坐标的角度值。
toDegrees() 将参数转化为角度。
toRadians() 将角度转换为弧度。
random() 返回一个随机数。

## Math 的 floor,round 和 ceil 方法实例比较
Math.floor
Math.round
Math.ceil

## floor,round 和 ceil 实例：
以上实例执行输出结果为：

```

Math.floor(1.4)=1.0

Math.round(1.4)=1

Math.ceil(1.4)=2.0

Math.floor(1.5)=1.0

Math.round(1.5)=2

Math.ceil(1.5)=2.0

Math.floor(1.6)=1.0

Math.round(1.6)=2

Math.ceil(1.6)=2.0

Math.floor(-1.4)=-2.0

Math.round(-1.4)=-1

Math.ceil(-1.4)=-1.0

Math.floor(-1.5)=-2.0

Math.round(-1.5)=-1

Math.ceil(-1.5)=-1.0

Math.floor(-1.6)=-2.0

Math.round(-1.6)=-2

Math.ceil(-1.6)=-1.0

```

## 6  篇笔记 写笔记
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