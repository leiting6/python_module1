#! _*_ coding: utf-8 _*_
# @Time: 4/14/2018
# @Author: LiuLeiting
# @Mail: leiting.liu@qq.com
# @File: three-menu_version1.py.py
menu = { '北京':{ '海淀':{ '五道口':{ 'soho':{}, '网易':{}, 'google':{} }, '中关村':{ '爱奇艺':{}, '汽车之家':{}, 'youku':{}, }, '上地':{ '百度':{}, }, },
        '昌平':{ '沙河':{ '老男孩':{}, '北航':{}, }, '天通苑':{}, '回龙观':{}, }, '朝阳':{}, '东城':{}, },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

while True:
    for i in menu:
        print(i)

    choice = input(">:").strip()
    if not choice:
        continue
    if choice in menu:
# 进入第二层
        while True:
            for k in menu[choice]:
                print(k)
            choice2 = input(">>:").strip()
            if not choice2:
                continue
            if choice2 in menu[choice]:
# 进入第三层
                while True:
                    for k in menu[choice][choice2]:
                        print(k)
                    choice3 = input(">>>:").strip()
                    if not choice3:
                        continue
                    if choice3 in menu[choice][choice2]:
                        print(menu[choice][choice2][choice3])
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit(">>> bye,bye!")
                    else:
                        print("节点不存在！")
            elif choice2 == 'b':
                break
            elif choice3 == 'q':
                exit(">> bye,bye!")
            else:
                print("节点不存在！")

