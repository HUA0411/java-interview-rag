# Java 面试题:基础篇

## 1. 什么是 Java 的 JVM、JRE、JDK?

- JVM(Java Virtual Machine):Java 虚拟机,是 Java 程序运行的核心环境,负责将字节码解释/编译为机器码执行。
- JRE(Java Runtime Environment):Java 运行环境,包含 JVM 和核心类库,只能运行 Java 程序,不能编译。
- JDK(Java Development Kit):Java 开发工具包,包含 JRE + 编译器(javac) + 调试工具等开发工具,既能编译也能运行。

关系:JDK ⊃ JRE ⊃ JVM。一次编译,到处运行(Write Once, Run Anywhere),靠的就是 JVM。

## 2. Java 的基本数据类型有哪些?

8 种基本类型:
- 整数型:byte(1字节)、short(2字节)、int(4字节)、long(8字节)
- 浮点型:float(4字节)、double(8字节)
- 字符型:char(2字节)
- 布尔型:boolean(理论上1位)

包装类:Byte、Short、Integer、Long、Float、Double、Character、Boolean。

## 3. == 和 equals() 的区别?

- == 比较的是内存地址(引用是否指向同一个对象);基本类型比较的是值。
- equals() 是 Object 的方法,默认也是比较地址,但 String 等类重写了它,改为比较内容。
- 例:`new String("abc") == new String("abc")` 为 false,`equals` 为 true。

## 4. HashMap 的底层原理?

- 底层是数组 + 链表 + 红黑树(JDK 8+)。
- put 流程:计算 key 的 hash 值 → 定位数组下标 → 若该位置为空直接放;若冲突,尾插法挂到链表;链表长度 ≥ 8 且数组长度 ≥ 64 时转红黑树。
- 扩容:默认容量 16,负载因子 0.75,当元素数超过 容量×0.75 时扩容为原来的 2 倍。
- 线程不安全:并发 put 可能丢失数据,多线程用 ConcurrentHashMap。

## 5. 什么是 Java 的反射?

反射是指在运行状态下,动态获取类的完整结构(字段、方法、构造器)并调用其成员的能力。

用途:框架中大量使用,如 Spring 的 IoC 就是通过反射创建 Bean、注入依赖;JDBC 的 Class.forName() 加载驱动。

注意:反射性能比直接调用差,且破坏封装性。

## 6. 什么是线程和进程?如何创建线程?

- 进程:操作系统资源分配的基本单位,有独立内存空间。
- 线程:CPU 调度的基本单位,是进程内的执行单元,共享进程内存。

创建线程的 3 种方式:
1. 继承 Thread 类,重写 run()。
2. 实现 Runnable 接口(推荐,避免单继承限制)。
3. 实现 Callable 接口 + FutureTask,可以有返回值。

## 7. synchronized 和 ReentrantLock 的区别?

- synchronized 是 JVM 关键字,自动加锁解锁;ReentrantLock 是 JDK 类,需手动 lock/unlock。
- ReentrantLock 更灵活:支持公平锁、可中断、可超时、支持多个 Condition 条件变量。
- ReentrantLock 底层基于 AQS(AbstractQueuedSynchronizer);synchronized 底层是 Monitor 锁,JDK 6 后有锁升级(偏向锁→轻量级锁→重量级锁)。

## 8. 什么是 JVM 内存区域(运行时数据区)?

- 程序计数器:当前线程执行的字节码行号指示器。
- 虚拟机栈:存放局部变量、操作数栈等,线程私有,栈溢出 → StackOverflowError。
- 本地方法栈:执行 native 方法。
- 堆:对象实例分配的主要区域,线程共享,GC 主要回收这里。分新生代、老年代。
- 方法区(元空间):类信息、常量、静态变量。JDK 8 后改为元空间,使用本地内存。

## 9. 什么是垃圾回收(GC)?常见的垃圾回收器?

- 判定对象可回收:引用计数法(有循环引用问题)、可达性分析(GC Roots 出发,不可达则回收)。
- 新生代回收算法:复制算法(Minor GC, Eden 区与两个 Survivor 区)。
- 老年代回收算法:标记-清除、标记-整理。
- 常见收集器:Serial、Parallel、CMS(并发标记清除,关注停顿)、G1(JDK 9+ 默认,把堆分为 Region,可预测停顿时间)、ZGC(超低延迟,JDK 15 可商用)。

## 10. Spring 的 IoC 和 AOP 是什么?

- IoC(控制反转):对象的创建和依赖注入交给 Spring 容器管理,而不是自己 new。核心是 DI(依赖注入),常用 @Autowired / 构造器注入。
- AOP(面向切面编程):把日志、事务、权限等横切逻辑抽离,通过动态代理织入业务方法前后。Spring AOP 基于 JDK 动态代理(接口)或 CGLIB(类)。

## 11. Spring 事务的传播行为有哪些?

常用 3 种:
- REQUIRED(默认):有事务就加入,没有就新建。
- REQUIRED_NEW:总是新建事务,与已有事务互不影响(如记录日志)。
- NESTED:嵌套事务,内层回滚不影响外层(基于保存点)。

失效场景:方法非 public、自调用(同类方法内部调用不走代理)、异常被 catch 没抛出、异常类型不是 RuntimeException(默认只回滚运行时异常,需 rollbackFor=Exception.class)。

## 12. MySQL 索引为什么用 B+ 树?

- B+ 树矮胖,层级少(3 层可存千万级数据),IO 次数少。
- 非叶子节点只存键不存数据,单页能存更多索引项。
- 叶子节点用链表串起来,天然支持范围查询和排序。
- 对比:哈希索引不支持范围查询;B 树(不是 B+树)数据分散在每层,范围查询要回溯。

## 13. 什么是事务的 ACID?

- 原子性(Atomicity):要么全成功要么全失败。
- 一致性(Consistency):事务前后数据保持业务一致。
- 隔离性(Isolation):并发事务互不干扰。
- 持久性(Durability):提交后数据永久保存。

隔离级别(从低到高):读未提交 → 读已提交 → 可重复读(MySQL 默认)→ 串行化。
并发问题:脏读(读未提交)、不可重复读、幻读(可重复读下 InnoDB 用 MVCC + 间隙锁解决)。

## 14. Redis 为什么快?有哪些数据类型?

- 纯内存操作;单线程避免锁竞争和上下文切换(6.0 后网络 IO 多线程);IO 多路复用(epoll)。
- 数据类型:String、Hash、List、Set、ZSet(有序集合,跳表实现)。
- 常见场景:缓存、分布式锁(setnx + 过期时间)、计数器(incr)、消息队列(List 或 Stream)、排行榜(ZSet)。

## 15. 什么是缓存穿透、击穿、雪崩?

- 穿透:查一个不存在的 key,每次都打到数据库。解决:缓存空值、布隆过滤器。
- 击穿:热点 key 过期瞬间大量请求打到 DB。解决:互斥锁、逻辑过期。
- 雪崩:大量 key 同时过期,或 Redis 宕机,导致 DB 被打垮。解决:过期时间加随机值、多级缓存、限流降级。

## 16. 什么是 TCP 三次握手和四次挥手?

- 三次握手:SYN → SYN+ACK → ACK。确认双方收发能力,防止过期连接请求。
- 四次挥手:FIN → ACK → FIN → ACK。因为 TCP 全双工,两端各自关闭,所以比握手多一次。
- 为什么四次:服务端收到 FIN 先回 ACK,等自己数据发完再发 FIN。

## 17. RESTful API 设计规范要点?

- 使用名词表示资源:/users、/orders,不用动词。
- HTTP 方法表达操作:GET 查、POST 增、PUT 改、DELETE 删。
- 状态码语义化:200 成功、201 创建、400 参数错误、401 未认证、403 无权限、404 不存在、500 服务器错误。
- 版本化:/api/v1/users。

## 18. 什么是分布式事务?常见解决方案?

- 场景:微服务跨库操作,本地事务无法保证一致性。
- 方案:
  1. 2PC/XA(两阶段提交):强一致,性能差,不适合高并发。
  2. TCC(补偿事务):Try-Confirm-Cancel,业务侵入大。
  3. 本地消息表 + 消息队列(最终一致性):事务写库 + 发消息,消费方幂等处理。
  4. Seata 框架(AT 模式)。

## 19. 什么是消息队列?为什么用?

- 作用:异步处理(注册后发短信)、削峰填谷(秒杀)、系统解耦(订单服务与库存服务不直接调用)。
- 常见:RabbitMQ(Erlang,功能全)、Kafka(高吞吐,日志)、RocketMQ(阿里,金融级)。
- 可靠投递:确认机制(ACK)、重试、死信队列;消费幂等(唯一 ID)。

## 20. 如何排查线上 CPU 飙高的问题?

1. top 找到占用高的进程 PID。
2. top -Hp PID 找到占用高的线程 TID。
3. printf '%x' TID 转成十六进制。
4. jstack PID | grep -A 线程号 查看线程堆栈,定位业务代码。
5. 常见原因:死循环、频繁 GC、正则回溯、日志过多。
