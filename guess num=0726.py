#coding=utf-8
import random
import os
cmp_name = []
score_list=[]
old_list = []
game_times = 0
min_times = 0
total_times = 0
write_list =[]
count=[]
name_flag =0
ava_time = 0
i = 1  # 统计每次游戏中猜的轮数
count = []  #存放每次猜对时用的轮数
sum_ava = 0  #用于计算平均几次猜对的总数
flag = 0
name = ''
wanjia_list=''
def read_data_from_file():
    global score_list
    print("=======welcome to play this game ! ========")
    try:
        f1=open("score2.txt","r+")
        score_list = f1.readlines()
        if len(score_list)==0:
            with open(r"score2.txt", "w+")as f1:
                f1.writelines("name   game_times  ava_time  total_times  min_time\n")
                score_list = f1.readlines()
        f1.close()

    except (FileNotFoundError,IndexError):
        with open("score2.txt", "w+")as f1:
            f1.writelines("name   ame_times  ava_time  total_times  min_time\n")
            score_list = f1.readlines()

def name_judge():
    global name_flag,score_list,wanjia_list,name,cmp_name
    print("现在开始猜数游戏，猜数范围为 1~100，一轮只能猜10次！")
    name = input("请输入昵称： ")
    for m in score_list:
    	cmp_name = m.split()
    	if name == cmp_name[0]:
    		name_flag = 1
    		wanjia_list = m
    		print("欢迎回来 ： "+name)
    	else:
    		continue

def input_judge(num_list):  
    '''输入并判断'''
    i = 5
    while i>0: 
        try:
            num = eval(input())
        except (NameError,SyntaxError):
            print("请输入合理的数字！")
            i -= 1 
            continue
        else :
            if num not in num_list and i != 1:
                num = print("输入错误，请重新输入：",end="")
                i -= 1
                continue
            elif num in num_list:
                break
    if i == 0:
        print("你已经连续输错5次，程序自动退出！")
        exit(0)
    else :
        return num
   
def write(old_list1):
    global game_times,min_time,total_times,ava_time,write_list,count,name_flag,name
    for j in range(1, 5):
        old_list1[j] = int(old_list1[j])
    #print("count长度：%d"%len(count))

    if len(count) == 0:
        if name_flag == 0:
            min_time = 0
        else:
            min_time = old_list1[4]
    else:
        count.sort()
        if count[0]<old_list1[4] and old_list1[4]>0:
            min_time = count[0]
        elif old_list1[4] == 0:
        	min_time = count[0]
        else:
            min_time = old_list1[4]        
    new_game_times =(game_times + old_list1[1])
    new_total_times = (total_times + old_list1[3])
    ava_time = int(new_total_times/new_game_times)
    if ava_time ==10 and min_time == 0:
        ava_time = 0
    write_list = [str(new_game_times)+'\t', str(ava_time)+'\t', str(new_total_times)+'\t', str(min_time)+'\t']
    #write_list1 = name+' '.join(write_list) + '\n'
    return '  '+name + " \t" +'   '.join(write_list) + '\n'  #列表类型

def save_data():
    global cmp_name,game_times,min_time,total_times,ava_time,write_list,count,sum_ava,old_list,score_list,wanjia_list,name_flag,name
    with open("score2.txt","r") as f3:
    	score_list = f3.readlines()
    	for m in score_list:
    		cmp_name = m.split()
    		if name == cmp_name[0]:
    			wanjia_list = m
    if name_flag == 0:
        f1 = open("score2.txt", "a+")
        old_list = ["unknowname", 0,0,0,11]
        result = write(old_list)
        #new=write(old_list)
        f1.writelines(result)
        f1.close()
    else:

    	
        old_list = wanjia_list.split()
        result = write(old_list)
        #new = write(old_list)
        #result = name + "\t" +' '.join(write_list) + '\n'
        f2 = open("score2.txt", "w")
        for line1 in score_list:
            #print(line1)
            if name in line1:
                print("name in file")
                continue
            else:
                #print(result)
                f2.writelines(line1)
        f2.writelines(result)
        f2.flush()
        f2.close()

    print("你目前的总成绩为：")
    print("name,ame_times, ava_time, total_times,min_time")
    print(result)
        

def guess_number():
    global i,count,total_times,game_times,flag,name_flag
    num_list = [i for i in range(1,101)]
    while True:
        ans = random.randint(1, 100)
        while i <= 10:
            print("======第 %d 次======="%i)
            print("你猜我出的是多少：")
            num = input_judge(num_list)
            if num > ans:
                print("太大啦！！")
                i += 1
                continue
            elif num < ans:
                print("太小了")
                i += 1
                continue
            elif num == ans:
                flag = 1
                print("哇，恭喜你猜对啦！赢咯")
                print("猜了 %d 次才对" % i)
                count.append(i)
                total_times +=i
                break
        if flag == 0:
            print("10次机会用完，你输啦！！")
            total_times += 10
        game_times += 1
        print("还要继续吗？  1、继续游戏并保存本轮成绩   2、不保存成绩退出  3、保存成绩并退出")
        num_list1 =[i for i in range(1,4)]
        
        x=input_judge(num_list1)
        print(total_times,game_times)
        if x == 1:    #保存并退出，要把total_times ,garme_times,flag 置为0，name_flag =1
            if len(count) == 0:
                print("=====很遗憾你这一次没有猜中====")
            else :
                print("你本次游戏平均 %d 次猜中" % (total_times / game_times))
            save_data()
            i = 1
            flag = 0
            total_times =0
            game_times = 0
            name_flag = 1
        elif x == 2:
            print("游戏结束！")
            if len(count) == 0:
                print("=====很遗憾你这一次没有猜中====")
            else :
                print("你本次游戏平均 %d 次猜中" % (total_times / game_times))
            break
        elif x==3:
            if len(count) == 0:
                print("=====很遗憾你这一轮没有猜中====")
            else :
                print("你本次游戏平均 %d 次猜中" % (total_times / game_times))
            save_data()
            break

def main():
    read_data_from_file()
    name_judge()
    guess_number()


if __name__ == '__main__':
    main()






   
