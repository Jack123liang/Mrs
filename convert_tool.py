import os

def list_to_mrs(input_path, output_path):
    try:
        with open(input_path, 'r') as f:
            lines = f.readlines()
        
        # 过滤空行和注释，并确保每一行都有 DOMAIN, 前缀（针对 domain 类型）
        rules = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                if ',' not in line:
                    rules.append(f"DOMAIN,{line}")
                else:
                    rules.append(line)
        
        # 模拟 Mihomo 的简单 MRS 封装（这里直接输出处理后的文本或调用轻量转换逻辑）
        # 注意：由于 MRS 是二进制，最简单的办法还是通过 Python 调用内核的 compile
        # 但为了避开之前的错误，我们用 Python 专门控制进程
        import subprocess
        result = subprocess.run(
            ['./mihomo', 'rule-set', 'compile', '/dev/stdin', output_path],
            input='\n'.join(rules).encode(),
            capture_output=True,
            timeout=5
        )
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# 自动处理目录下所有文件
if __name__ == "__main__":
    # 这里只是占位，逻辑已集成到下方的 YAML 中
    pass

