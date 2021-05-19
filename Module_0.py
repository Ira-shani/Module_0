import np

def game_core_v2(number):
    count = 1
    predict = np.random.randint(1,101)
    N = 100
    M = 100
    while number != predict:
        count += 1
        for i in range(1, N):
            for j in range(0, M):
                if predict % i == j and number % i == j:
                    if number > predict:
                        predict += i
                    elif number < predict:
                        predict -= i
                elif predict % i == j and number % i != j:
                    if number > predict:
                        predict += 1
                    elif number < predict:
                        predict -= 1
    return(count) # выход из цикла, если угадали
def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core_v2)

