

def sol(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)

    return answer



if __name__ == "__main__":
    a_list = [95, 90, 99, 99, 80, 99]
    b_list = [1, 1, 1, 1, 1, 1]
    ret = sol(a_list, b_list)
    print(ret)