from numpy import zeros


def game():
    text1 = input().strip().lower()
    text1 = list(text1)
    text2 = input().strip().lower()
    text2 = list(text2)

    if len(text1) <= len(text2):
        sword = text1
        lword = text2

    else:
        sword = text2
        lword = text1

    game_array = zeros((len(sword)+2, len(lword)+2))

    # print(game_array)
    for i in range(2, len(lword)+2):
        game_array[0, i] = ord(lword[i-2])

    for i in range(2, len(sword)+2):
        game_array[i, 0] = ord(sword[i-2])

    for j in range(2, len(sword)+2):
        # print(game_array[j:j+1, 0])
        for i in range(2, len(lword)+2):
            if game_array[j:j+1, 0] == game_array[0, i]:
                game_array[j, i] = (game_array[j-1, i-1]+1)

            else:
                game_array[j, i] = max(game_array[j-1, i], game_array[j, i-1])

    # print(game_array)
    print(int(game_array[-1, -1]))


while True:
    game()
