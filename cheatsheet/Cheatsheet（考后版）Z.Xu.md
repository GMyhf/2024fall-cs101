# Cheatsheet（考后版）

Compiled by 徐至晟，光华

注：本人考前没有准备Cheatsheet，考试时不需要。以下归纳一些不太熟练的语法点。

#### C++ map 与 Python 字典

参考资料：

1.https://blog.csdn.net/weixin_46369610/article/details/120349280

2.[Python3 字典 | 菜鸟教程](https://www.runoob.com/python3/python3-dictionary.html)

3.Bing 搜索 AI回答

4.[std::map - C++中文 - API参考文档](https://www.apiref.com/cpp-zh/cpp/container/map.html)



功能：实现键(key)=>值(value)的映射C++ map 迭代器遍历时，按key从小到大顺序

##### C++ map 库部分函数

```c++
m.insert(pair<int, string>(1, "stu1"));
m[2]="stu2"
if (m.find(1)!=m.end()) cout<<"found";//find(key)返回迭代器，若不与end()相同则存在这一个键
m.erase(it);
m.erase(1);//erase可以是删除一个迭代器或者键
```

##### Python 字典部分函数与方法

```python
# python dict
d = {key1 : value1, key2 : value2, key3 : value3 }
emptyDict=dict()

len(d)
dict.get(key, default=None)#返回key对应的value，不存在返回default的值，避免报错
key in d
dict.pop(key[,default])
dict.popitem()#删除最后一对
```

#### Python格式化输出

```python
name="Alice"
a=10
pi=3.14159
print("Hello %s%.2f%d"%(name,pi,a))

print("{0} {1} {1} {0}".format("Li Hua",20))
#Li Hua 20 20 Li Hua
print("{name} {age}".format(name="Li Hua",age=20))
#Li Hua 20
```

