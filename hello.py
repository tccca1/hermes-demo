"""Hermes Demo — 功能演示"""

def greet(name):
    """向用户打招呼"""
    return f"你好，{name}！欢迎使用 Hermes Demo。"

def add(a, b):
    """两数相加"""
    return a + b

def multiply(a, b):
    """两数相乘"""
    return a * b

def factorial(n):
    """计算阶乘"""
    if n < 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def is_even(n):
    """判断是否为偶数"""
    return n % 2 == 0


def fibonacci(n):
    """返回第 n 个斐波那契数"""
    if n < 0:
        return 0
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def calculate_statistics(numbers):
    """计算一组数字的统计信息
    返回: (平均值, 中位数, 标准差)
    """
    n = len(numbers)
    if n == 0:
        return (0, 0, 0)

    # 平均值
    mean = sum(numbers) / n

    # 中位数
    sorted_nums = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]

    # 标准差
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1)
    std_dev = variance ** 0.5

    return (mean, median, std_dev)

def is_odd(n):
    """判断是否为奇数"""
    return n % 2 == 1

def count_words(text):
    """统计文本中的单词数"""
    return len(text.split())

def average(numbers):
    """计算平均数"""
    return sum(numbers) / len(numbers)

def main():
    """主函数"""
    print(greet("世界"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"3 × 4 = {multiply(3, 4)}")
    print(f"5! = {factorial(5)}")
    print(f"判断数字 42:")
    print(f"  偶数? {is_even(42)}")
    print(f"  奇数? {is_odd(42)}")
    print(f"单词数: {count_words('Hello world this is a test')}")
    print(f"平均数: {average([1, 2, 3, 4, 5])}")

if __name__ == "__main__":
    main()
