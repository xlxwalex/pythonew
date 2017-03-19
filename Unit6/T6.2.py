#6.2
def main():
    num=[]
    n=input("请输入一组数字(或者直接按回车结束程序):")
    while n!="":
        num.append(eval(n))
        n=input("请输入一组数字(或者直接按回车结束程序):")
    else:
        print("正在处理，请稍等")
        judge(num)

def judge(n):
    if len(n) == len(set(n)):
        print("鉴定完毕，没有重复的元素")
    else:
        print("有重复的元素，总共有{}个".format(len(n)-len(set(n))))
main()
