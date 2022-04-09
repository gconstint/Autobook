def load_txt(paralist, filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        datas = file.readlines()[0:11]
    datas_copy = [each.split() for each in datas]

    # 关于字典如何对值快速赋值
    # <本次代码于2022-04-09 修改 参考了enumerate的用法
    temp_list = ['type', 'name', 'password', 'borrower_name1', 'borrower_name2', 'borrower1contact_info',
                 'borrower2contact_info', 'date', 'start_time', 'person_response', 'person_tel', 'user_list']
    for i, value in enumerate(temp_list):
        # 当value值为user_list时，需要对其进行特殊处理
        if value == 'user_list':
            paralist[value] = datas_copy[3][1], datas_copy[4][1]
        elif value == "start_time":
            paralist[value] = int(datas_copy[8][1])
        else:
            paralist[value] = datas_copy[i][1]

    # paralist['type'] = datas_copy[0][1]
    # paralist['name'] = datas_copy[1][1]
    # paralist['password'] = datas_copy[2][1]
    # paralist['borrower_name1'] = datas_copy[3][1]
    # paralist['borrower_name2'] = datas_copy[4][1]
    # paralist['borrower1contact_info'] = datas_copy[5][1]
    # paralist['borrower2contact_info'] = datas_copy[6][1]
    # paralist['date'] = datas_copy[7][1]
    # paralist['start_time'] = int(datas_copy[8][1])
    # paralist['person_response'] = datas_copy[9][1]
    # paralist['person_tel'] = datas_copy[10][1]
    # paralist['user_list'] = datas_copy[3][1], datas_copy[4][1]
