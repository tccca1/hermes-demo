def greet(name):
    """向用户打招呼"""
    return f"你好，{name}！欢迎使用 Hermes Demo。"

def add(a, b):
    """两数相加"""
    return a + b

if __name__ == "__main__":
    print(greet("世界"))
    print(f"1 + 2 = {add(1, 2)}")
