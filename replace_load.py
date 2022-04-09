def load_txt(paralist, filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        datas = file.readlines()[0:11]
    datas_copy = [each.split() for each in datas]

    # 将datas_copy第2列前11行数据的数据依次赋值给paralist
    for i in range(11):
        paralist[i] = datas_copy[i][1]
        # 将第9个数据转换为int形
        if i == 8:
            paralist[i] = int(paralist[i])
    # 对‘user_list'关键字的值特殊处理
    paralist['user_list'] = datas_copy[3][1], datas_copy[4][1]

    # 修改字典paralist的值
    # for each in datas_copy:
    #     paralist[each[0]] = each[1]
    #     #对’start_time'转换为int形
    #     if each[0] == 'start_time':
    #         paralist[each[0]] = int(each[1])
    # return paralist

    # 关于字典如何对值快速赋值？？？？
    # i = 0
    # for key in paralist:
    #     paralist[key] = datas_copy[i][1]
    #     i += 1

    paralist['type'] = datas_copy[0][1]
    paralist['name'] = datas_copy[1][1]
    paralist['password'] = datas_copy[2][1]
    paralist['borrower_name1'] = datas_copy[3][1]
    paralist['borrower_name2'] = datas_copy[4][1]
    paralist['borrower1contact_info'] = datas_copy[5][1]
    paralist['borrower2contact_info'] = datas_copy[6][1]
    paralist['date'] = datas_copy[7][1]
    paralist['start_time'] = int(datas_copy[8][1])
    paralist['person_response'] = datas_copy[9][1]
    paralist['person_tel'] = datas_copy[10][1]
    paralist['user_list'] = datas_copy[3][1], datas_copy[4][1]