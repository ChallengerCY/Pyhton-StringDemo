#字段宽度和精度
#转换说明符可以包括字段宽度和精度。字段宽度是转换后的值所保留的最小字符个数，精度（对于数字转换）则是结果中应该包含的小数位数
#或者(对于字符串转换来说)是转换后的值所能包含的最大字符个数
#俩个参数都是整数(首先是字段宽度，然后是精度)，通过点号(.)分隔。虽然俩个都是可选的参数，但如果只给出精度，就必须包含点号：
from math import pi
print("%10f" % pi)
print('%10.2f' % pi)
print('%.3s'% 'Challenger')
#可以使用*作为字段宽度或者精度(俩者都可以使用),此时数值会从元组参数中读出:
print('%.*s'%(5,'Challenger'))

#符号、对齐和用0填充
#在字段宽度和精度之前还可以放置一个标志，该标志可以是零，加号、减号、或空格
#010表示用0占位，输出长度为10得字符宽度
print('%010.2f'%pi)
#python3 中 表示八进制的数开头用0o表示
print(0o10)
#减号用来左对齐数字
print("%-10.2f" % pi)
#""空白意味着在正数前面加上空格，这需要在对齐正负数时会很有用
print('% d' % 10 +'\n'+ '% u' % -10)
#加号表示不管是正数还是负数
print('%+d' % 10 +'\n'+ '%+u' % -10)