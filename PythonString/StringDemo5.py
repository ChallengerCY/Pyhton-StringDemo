#四、字符串方法
#find方法
#find方法可以在一个较长的字符串中查找子字符串，它返回子串所在位置的最左端索引，如果没有则返回-1
print("ChalllengerCY".find("lll"))
print("zxcvb".find("a"))
#也可以使用find建立一个垃圾邮件过滤器
subject='$$$Get rich now!!!$$$'
print(subject.find("$$$"))
#这个方法还可以接收可选的起始点和结束点参数
print(subject.find("$$$",1))
print(subject.find("$$$",1,5))

#join方法
#join方法是非常重要的字符串方法，它是split方法的逆方法，用来连接序列中的元素
#被连接的序列元素必须是字符串方法
seq=['1','2','3','4','5']
sep='+'
print(sep.join(seq))
url=['','usr','bin','env']
sep2='/'
print(sep2.join(url))
print("C:"+'\\'.join(url))

#lower方法
#lower方法返回字符串的小写字母版,适用于编写不区分大小写的代码
print("SADADAD".lower())

#replace方法
#replace方法返回某个字符串的所有匹配项均被替换之后得到字符串
#这个方法用于“查找并替换功能”
print("This is a test".replace('is','eez'))

#split方法
#用于将字符串分割成序列,如果不提供任何分隔符，程序会把所有空格作为分隔符(空格，制表，换行)
print('1+2+3+4+5'.split('+'))
print("Using name password".split())