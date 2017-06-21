#strip方法
#strip方法返回除去俩侧(不包括内部)空格的字符串
#假如用户在输入用户名时在俩侧加入空格可以用这个方法进行判断
print("  adsadasd     ".strip())
#也可以指定需要去除的字符，将他们列为参数
print("***sdadsd**asdasd!*".strip("*!"))

#translate
#translate方法和replace方法一样，可以替换字符串中的某些部分，但是和前者不同的是，translate方法只处理单个字符，他的优势在于可以同时进行多个替换，有些时候效率比replace高
#使用这个方法的方式有很多(比如替换换行符或者其他因平台而异的特殊字符)
#使用translate前，需要完成一张转换表，转换表中以某字符替代某字符的对应关系，使用string模块里面的maketrans函数
#maketrans接受俩个参数：两个等长的字符串，表示第一个字符串中的每个字符都用第二个字符串中相同位置的字符替换。
table=str.maketrans("csa","kzb")
print("this is an icrediable test".translate(table))



