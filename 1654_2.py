import sys
input = sys.stdin.readline()
k, n = map(int, int(input().split()))
lan = [int(input()) for _ in range(k)]
end = max(lan)


def lan_length(a):
    count = 0
    for item in lan:
        count += item//a
    return count


def binary_search(start, end, n):
    if start > end:
        return end
    mid = (start+end)//2
    length = lan_length(mid)
    if length > n:
        return binary_search(mid + 1, end, n)
    else:
        return binary_search(start, mid - 1, n)


print(binary_search(1, end, n))
