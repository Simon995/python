student = [{'姓名':'小明','电话':'666666','QQ':'222222','邮箱':'123@qq.com'}]
student1 = ['姓名','电话','QQ','邮箱']
while True:
    print('学籍管理系统')
    print('-'*50)
    print('1:新增学生',
          '2:显示全部',
          '3:查询学生',
          '4:退出系统')
    print('-'*50)
    dic={}
    
    sr = input('请输入所要执行的序号:')
    if sr == '4':
        print('程序退出中……！')
        break
    if sr.isdigit():#判断输入是否为数字
        sr = int(sr)
        if 0<sr<4:#判断输入是否超出范围
            if sr == 1:
                name = input('输入姓名:')
                tel = input('输入电话:')
                QQ = input('输入QQ:')
                mail = input('输入邮箱:')
                dic['姓名'] = name
                dic['电话'] = tel
                dic['QQ'] = QQ
                dic['邮箱'] = mail
                student.append(dic)#将字典添加到列表
                print('用户添加成功！')
            if sr == 2:
                for i in student1:
                    print(i.ljust(5), end='\t\t\t')#ljust左对齐
                print()
                for g in student:
                    for h in g.values():
                        print(h.ljust(5),end='\t\t\t')
                    print()
                continue
            if sr == 3:
                cz = input('请输入所查询的姓名:')
                for a in range(0,len(student)):#查看student中字典存在个数
                    if student[a]['姓名'] == cz:#当输入的姓名和字典中的姓名一样就往下执行
                        print('姓名:{} 电话:{} QQ:{} 邮箱:{}'.format(student[a]['姓名'],student[a]['电话'],
                                                               student[a]['QQ'],student[a]['邮箱']))
                        print('[1]修改 [2] 删除 [0] 返回上一级菜单，请选择要执行的操作。')
                        caozuo = input('请输入你要执行操作的序号:')
                        if caozuo == '0':
                            print('正在返回上一级菜单')
                            break
                        if caozuo == '1':
                            new_name = input('请输入新的姓名')
                            new_tel = input('请输入新的电话')
                            new_qq = input('请输入新的QQ')
                            new_mail = input('请输入新的邮箱')
                            student[a]['姓名'] = new_name
                            student[a]['电话'] = new_tel
                            student[a]['QQ'] = new_qq
                            student[a]['邮箱'] = new_mail
                            print('修改成功！！')
                        if caozuo  == '2':
                            del student[a]
                            print('删除成功##')
                        elif a == len(student) - 1:
                            print('请输入的姓名不存在')
        else:
            print('看清范围在输入。。。')
    else:
        print('请输入数字！！')
