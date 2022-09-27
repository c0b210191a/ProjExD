import random
import datetime

def quiz(aps,apl,apd):
    print("対象文字")
    print(aps)
    #print("欠損文字")
    #print(apl)
    print("表示文字")
    print(apd)
    

def kaito(apl):
    st = datetime.datetime.now()
    ans_num = input("欠損文字はいくつあるでしょうか？")
    if ans_num == len(apl):
        print("正解です。それでは、具体的な欠損文字を一つずつ入力してください。")
        ans_lst = []
        for i in range(len(apl)):
            ans_alp = input(f"{i+1}つ目の文字を入力してください")
            if ans_alp in apl and ans_alp not in ans_lst:
                ans_lst.append(ans_alp)
                pass
            else:
                print("不正解です。またチャレンジしてください")
                break
    else:
        print("不正解です。またチャレンジしてください")
    ed = datetime.datetime.now()
    print((ed-st).seconds)

if __name__ =="__main__":
    alp_lst = []
    for i in range(65,91):
        alp_lst.append(chr(i))

    alp_sam = random.sample(alp_lst,10)   #対象文字
    alp_los = random.sample(alp_sam,random.randint(1,4))   #欠損文字
    alp_dis = []   #表示文字
    for i in alp_sam:
        if i in alp_los:
            pass
        else:
            alp_dis.append(i)

    quiz(alp_sam,alp_los,alp_dis)
    kaito(alp_los)