draws = None
cards = []
hit = []
card = []

for line in open("4.in"):
    line = line.strip()
    if draws is None:
        draws = [int(x) for x in line.split(",")]
    else:
        if line:
            card.append([int(x) for x in line.split()])
        else:
            if card:
                cards.append(card)
            card = []
cards.append(card)

for _ in cards:
    hit.append([[False for _ in range(5)] for _ in range(5)])

finished = [False for _ in range(len(cards))]
for num in draws:
    for i in range(len(cards)):
        for x in range(5):
            for y in range(5):
                if cards[i][x][y] == num:
                    hit[i][x][y] = True

        won = False
        for x in range(5):
            ok = True
            for y in range(5):
                if not hit[i][x][y]:
                    ok = False
            if ok:
                won = True
        for y in range(5):
            ok = True
            for x in range(5):
                if not hit[i][x][y]:
                    ok = False
            if ok:
                won = True

        if won:
            if finished[i]:
                continue
            sum = 0
            for x in range(5):
                for y in range(5):
                    if not hit[i][x][y]:
                        sum += cards[i][x][y]
            # First and last value this prints are p1 and p2.
            print(num * sum)
            finished[i] = True
