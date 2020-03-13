def brute_force(s, idx):
    s = s[:idx]
    s = s.replace(" ", "%20")
    return s

def execute(s, idx):
    return brute_force(s, idx)

if __name__ == "__main__":
    print(execute("hello world ", 11))
    print(execute("hello world   ", 11))
    print(execute("hello world kazuki  ", 18))
    
