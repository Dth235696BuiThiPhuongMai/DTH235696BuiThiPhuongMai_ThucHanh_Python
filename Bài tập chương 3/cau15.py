ranges = [
    range(5),
    range(5, 10),
    range(5, 20, 3),
    range(20, 5, -1),
    range(20, 5, -3),
    range(10, 5),
    range(0),
    range(10, 101, 10),
    range(10, -1, -1),
    range(-3, 4),
    range(0, 10, 1)
]

labels = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)', '(k)']

for label, r in zip(labels, ranges):
    print(label, list(r))
