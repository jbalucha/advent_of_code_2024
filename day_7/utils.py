def parse_line(line):
    result_str, numbers_str = line.split(':')
    result = int(result_str.strip())
    numbers = list(map(int, numbers_str.strip().split()))
    return result, numbers