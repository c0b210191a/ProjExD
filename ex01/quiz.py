import random
import datetime


def shutudai(quiz):
    print("問題：")
    print(quiz)

def kaito(n):
    ans = input("解答せよ：")
    i = quiz_list.index(n)
    if ans in ans_list[i]:
         print("正解")
    else:
         print("不正解")

if __name__ == "__main__":
    quiz_list = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオからみてどんな関係？"]
    ans_list = [["マスオ","ますお",],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
    quiz = random.choice(quiz_list)
    shutudai(quiz)
    kaito(quiz)