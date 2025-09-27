import random

def train_markov(text):
    words = text.split()
    model = {}
    for i in range(len(words)-1):
        w = words[i]
        nxt = words[i+1]
        model.setdefault(w, []).append(nxt)
    return model

def generate(model, start, length=50):
    cur = start
    result = [cur]
    for _ in range(length-1):
        choices = model.get(cur)
        if not choices:
            break
        cur = random.choice(choices)
        result.append(cur)
    return " ".join(result)

# Example: train from a file
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read().replace("\n", " ")
model = train_markov(text)
start = random.choice(list(model.keys()))
print(generate(model, start, 40))
