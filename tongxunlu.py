print('欢迎进入通讯录程序\n1:查询联系人资料\n2:插入新的联系人\n3:删除已有联系人\n4:退出通讯录程序\n')

mingdan=dict()
while 1:
    get=int(input('请输入相关的指令代码：'))
    if get == 4:
        print('感谢使用通讯录程序')
        break
    elif get == 2:
        name=input('请输入联系人姓名：')
        if name not in mingdan:
            mingdan[name]=input('请输入用户联系电话：')
        else:
            print('您输入的姓名在通讯录中已存在-->>%s'%(name+mingdan[name]))
            x=input('是否修改用户资料（YES/NO）：')
            if x == 'YES':
                mingdan[name]=input('请输入用户联系电话：')
    elif get == 1:
        name=input('请输入联系人姓名：')
        if name not in mingdan:
            print('没有这个联系人')
        else:
            print(name+'：'+mingdan[name])
    elif get == 3:
        name=input('请输入联系人姓名：')
        if name not in mingdan:
            print('没有这个联系人')
        else:
            del mingdan[name]
            print('联系人已删除')