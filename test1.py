#构建一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 1
        yield n
        
#定义一个筛选奇数的函数
def is_palindrome(n):
    return n == int(str(n)[::-1])                         #筛选回数的函数

#定义一个生成器，不断返回下一个数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it)     # 返回序列的第一个数
        yield n
        it = filter(is_palindrome(n), it) # 构造新序列
        
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break