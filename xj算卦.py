import json
import os
import random
import time


json_file = 'xj_64gua.json'


def get_yao():
    yao_list = ['老阴', '少阳', '少阴', '老阳']
    yao_result_list = []
    for i in range(6):
        input('按回车摇第' + str(i + 1) + '个爻')
        a1 = random.randint(1, 2)
        a2 = random.randint(1, 2)
        a3 = random.randint(1, 2)
        yao_num = a1 + a2 + a3 - 3
        yao = yao_list[yao_num]
        print('第' + str(i + 1) + '个爻：', yao, '\n')
        yao_result_list.append(yao_num)
    return yao_result_list


def draw_gua(yao_result_list):
    print('已经得到你的卦象：\n')
    print('本卦：')
    ben_gua = []
    for i in range(6):
        reverse_i = 5 - i    # 考虑到卦象是从下到上，所以需要反序
        yao_num = yao_result_list[reverse_i]
        if yao_num == 0:     # 老阴
            print('—— —— X')
            ben_gua.append('2')
        elif yao_num == 1:   # 少阳
            print('—————')
            ben_gua.append('1')
        elif yao_num == 2:   # 少阴
            print('—— ——')
            ben_gua.append('2')
        elif yao_num == 3:   # 老阳
            print('————— O')
            ben_gua.append('1')
        else:
            assert False, '爻数出错'
    print('\n')
    print('变卦：')
    bian_gua = []
    for i in range(6):
        reverse_i = 5 - i  # 考虑到卦象是从下到上，所以需要反序
        yao_num = yao_result_list[reverse_i]
        if yao_num == 0:     # 老阴
            print('—————')
            bian_gua.append('1')
        elif yao_num == 1:   # 少阳
            print('—————')
            bian_gua.append('1')
        elif yao_num == 2:   # 少阴
            print('—— ——')
            bian_gua.append('2')
        elif yao_num == 3:   # 老阳
            print('—— ——')
            bian_gua.append('2')
        else:
            assert False, '爻数出错'
    return ben_gua, bian_gua


def gua2num(gua):
    if gua == ['1', '1', '1']:
        gua_name = '乾'
    elif gua == ['2', '1', '1']:
        gua_name = '兑'
    elif gua == ['1', '2', '1']:
        gua_name = '离'
    elif gua == ['2', '2', '1']:
        gua_name = '震'
    elif gua == ['1', '1', '2']:
        gua_name = '巽'
    elif gua == ['2', '1', '2']:
        gua_name = '坎'
    elif gua == ['1', '2', '2']:
        gua_name = '艮'
    elif gua == ['2', '2', '2']:
        gua_name = '坤'
    else:
        assert False, '卦象出错'
    return gua_name


def jie_gua(gua):
    shang_gua = gua[0:3]
    xia_gua = gua[3:6]
    shang_gua_name = gua2num(shang_gua)
    xia_gua_name = gua2num(xia_gua)
    gua_64_name = shang_gua_name + xia_gua_name
    assert isinstance(json_file, str) and json_file, "json_file 必须是字符串且不能为空"
    assert os.path.isfile(json_file), f"文件 {json_file} 不存在"
    with open(json_file, 'r', encoding='utf8') as fp:
        gua_data_map = json.load(fp)
    gua_data = gua_data_map[gua_64_name]
    print("你摇的卦为:", gua_data['name'])
    print("解读:", gua_data['explain'])


print('\n')
print('*******************************')
print('       赛博算卦     通识天下        ')
print('*******************************')
print('\n')
print('欢迎使用xj算卦，该程序可以根据六爻计算出相应的卦象，并给出粗略的解读。')
print('本方法将铜钱正反面随机赋值1或2，1为阴，2为阳，最后出爻。')
input('请闭上眼，仔细想想你要测算的事情信息，当你想好后，按回车键开始：\n')
yao_result = get_yao()      # 六爻结果，从下到上
ben_gua_result, bian_gua_result = draw_gua(yao_result)       # 绘制卦象

print('\n')
print('解卦须知：卦象中，上上卦、中中卦等仅代表发展趋势，不代表目前的实际状况。例如“泰”卦为大吉之兆，但是它只是中中卦。')
time.sleep(1)
if ben_gua_result == bian_gua_result:
    print('本卦与变卦相同，只需查看本卦即可。\n')
    input('按回车键查看卦象：')
    jie_gua(ben_gua_result)
else:
    print('\n')
    input('按回车键查看本卦：')
    jie_gua(ben_gua_result)
    print('\n')
    input('按回车键查看变卦：')
    jie_gua(bian_gua_result)

print('\n感谢使用，祝你好运！')
