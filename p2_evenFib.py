sequence: list[int] = [2, 1]
evenSeq: list[int] = []
current: int = 0

while(current < 4000000):
    if(sequence[0] % 2 == 0): evenSeq.append(sequence[0])
    current = (sequence[0] + sequence[1])
    sequence.insert(0, current)

print(sum(evenSeq))
