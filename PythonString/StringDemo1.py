#字符串
#一、基本字符串的操作
#所有标准的序列操作(索引、分片、乘法、判断成员资格、求长度、取最大值、取最小值)对字符串同样适用，但是，字符串不可变，分片赋值等改变值得操作是不合法的

#二、字符串格式化
#字符串格式化使用字符串格式化操作符，即%来实现。
#使用方法是 格式化字符串 % value
#value需要使用元组或者字典，这俩歌可以格式化一个以上的值，列表只能充当一个值
#%s部分被称为转换说明符，标记了需要插入转换值的位置，s表示值会被格式化成字符串
format="hello,%s,%s a,test"
value=('this','is')
print(format % value)

#格式化实数(浮点数)
format1="Pi with three decimal:%.3f"
from math import pi
print(format1 % pi)

#模版字符串
#string模块提供另外一种格式化值的方法:模版字符串，他的工作方式类似于UNIX Shell里的变量替换,使用$代替%,调用substitute方法
from string import Template
s = Template('$x,glorious $x !')
print(s.substitute(x='slurm'))
#如果替换的字段是单词的一部分，那么参数名就必须用括号括起来，从而准确指明结尾
s1=Template("It's ${b}CY")
print(s1.substitute(b='Challenger'))
#可以使用$$插入美元符号
s2=Template("It's $$ ${b}CY")
print(s2.substitute(b='Challenger'))
#除了关键参数 还可以使用字典变量提供值/名称对
s2=Template("name is $name,age is $age")
d={}
d['name']='Challenger'
d['age']=24
print(s2.substitute(d))

