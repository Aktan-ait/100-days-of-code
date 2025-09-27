from collections import deque

def word_ladder(start, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return []
    q = deque([[start]])
    visited = {start}
    while q:
        path = q.popleft()
        last = path[-1]
        if last == end:
            return path
        for i in range(len(last)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch == last[i]: continue
                nxt = last[:i] + ch + last[i+1:]
                if nxt in word_set and nxt not in visited:
                    visited.add(nxt)
                    q.append(path + [nxt])
    return []

# Example usage:
words = {"hit","hot","dot","dog","cog","lot","log"}
print(word_ladder("hit","cog", words))  # one shortest path
