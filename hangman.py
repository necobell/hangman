def hangman(word):
    wrong = 0       #誤答回数
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)      #答えの各アルファベット
    board = ["__"] * len(word) #ヒントのアルファベット数、位置
    win = False
    print("ハングマンへようこそ!")
    while wrong < len(stages) - 1:  #間違った回数< 間違え可能回数
        print("\n")                 #1回ごと空行
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:    #解答に文字が含まれていたら
            cind = rletters.index(char) #答えた文字の位置
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1      #誤答回数+1
        print((" ".join(board)))
        e = wrong + 1                  #描写するハングマンの行+1
        print("\n".join(stages[0: e]))  #描写するハングマンの行
        if "__" not in board:           #勝ちの処理
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:     #負けの処理
        print("\n".join(stages[0:wrong]))
        print("あなたの負け! 正解は {}.".format(word))

hangman("cat")      # cat が答え.好きに変えれる