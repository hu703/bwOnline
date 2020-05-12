## datetime模块

`datetime`模块是专门用来处理时间的标准库模块.

模块名是`datetime`, 这个模块的内部定义多个类.

------

`datetime`模块下有个类`datetime`既可以操作日期, 也可以操作时间. 主要研究这个类

### 1.1获取当前日期和时间

```python
# 导入 datetime 模块下的类 datetime
from datetime import datetime

# 调用 datetime 的类方法 now 获取当前日期和时间, 返回的是一个 datetime 对象
now = datetime.now()
print(now)
print(isinstance(now, datetime))
```

![](images/9-1.png)

------

### 1.2指定日期和时间

使用类`datetime`创建对象, 可以传入指定的日期和时间

```python
from datetime import datetime
# 年月日时分秒, 时分秒可选,默认都是0
that_time = datetime(2028, 10, 11, 12, 11, 20)

print(that_time)
```

传递值的时候不能超出范围, 否则会抛异常.

![](images/9-2.png)

------

### 1.3 `datetime`的一些常用属性和方法

#### 1.类属性

`min`: python 所能处理的最小日期和时间
`max`: python 所能处理的最大日期和时间

```python
from datetime import datetime

print(datetime.max)
print(datetime.min)
```

![](images/9-3.png)

------

#### 2.实例属性(只读)

`year, month, day, hour, minute, second, microsecond`

`microsecond`:是微秒

```python
from datetime import datetime

now = datetime.now()

msg = "现在是: %d 年 %d 月 %d 日 %d:%d:%d %d" \
      % (now.year, now.month, now.day,
         now.hour, now.minute, now.second,
         now.microsecond)

print(msg)
```

![](images/9-4.png)

------

#### 3.类方法

`now(), today()` 2 个方法都是返回当前日期和时间

------

#### 4.实例方法

`weekday()`:返回是星期几(0-6)
`isoweekday()`:也是返回星期几(1-7)

```python
from datetime import datetime

now = datetime.now()

print(now.weekday())
print(now.isoweekday())
```

![](images/9-5.png)

------

### 1.4`datetime`支持的 `+ - 比较`操作

`datetime`实例可以和一个`timedelta`对象进行 `+ -`操作

`timedelta`表示日期和时间的一个变化量

```python
from datetime import datetime, timedelta

now = datetime.now()

print(now)
# 表示3天后的时间
later = now + timedelta(days=3)
print(later)

# 表示3天前的时间
pre = now - timedelta(days=3)
print(pre)

# 两个日期进行比较大小
print(now > pre)
print(now < later)
```

![](images/9-6.png)

------

### 1.5`timestamp`(时间戳)

在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。

注意:python 的这里是用 s 来表示的, 别的语言大部分是 ms.

```python
from datetime import datetime

now = datetime.now()

# 把日期和时间转成时间戳. 注意返回值是浮点数
print(now.timestamp())

# 把时间戳转换成 datetime

that_dt = datetime.fromtimestamp(2849839789)
print(that_dt)
```

![](images/9-7.png)



