def is_palindrome(s):
    # 将字符串转换为小写并移除空格
    s = s.lower().replace(" ", "")
    # 检查处理后的字符串是否与其反转相同
    return s == s[::-1]

