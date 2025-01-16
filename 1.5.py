import time
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 函数执行时间为 {end_time - start_time:.4f} 秒")
        return result
    return wrapper
@timing_decorator
def calculate_sum(a, b):
    print(f"计算 {a} 和 {b} 的和")
    return a + b

@timing_decorator
def read_and_write_sum(filename_input, filename_output):
    try:
        with open(filename_input, 'r') as file:
            a, b = map(int, file.read().split())
            print(f"从文件中读取数字：a = {a}, b = {b}")
            result = calculate_sum(a, b)
            with open(filename_output, 'w') as file:
                file.write(str(result))
            print(f"结果写入 {filename_output}")
    except FileNotFoundError:
        print(f"文件 {filename_input} 未找到。")
    except Exception as e:
        print(f"发生错误：{e}")

# 示例用法：
calculate_sum(5, 3)
read_and_write_sum('input.txt', 'output.txt')