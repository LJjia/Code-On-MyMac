#!/usr/bin/env python
#-*- coding:utf-8 _*-
__author__ = 'LJjia'
# *******************************************************************
#     Filename @  merge.py
#       Author @  Jia Liangjun
#  Create date @  2021/05/03 13:45
#        Email @  LJjiahf@163.com
#  Description @  
# ********************************************************************



import json
import pprint



json_diagnoses_attr_list=['state',
                          'last_known_disease_status',
                          'days_to_last_follow_up',
                          'primary_diagnosis',
                          'tumor_grade',
                          'progression_or_recurrence']
json_demographic_attr_list=['gender',
                            'year_of_birth',
                            'days_to_death',
                            'cause_of_death',
                            'vital_status',
                            'race']

def getKeyWord(name):
    if '.' in name:
        key=name.split('.')[2]
    elif ('_' in name) or('-' in name):
        key=name.replace('_','-').split('-')[2]
    else:
        print("warn! input param %s  error"%name)
        key=None
    return key

# 两种 名字 TARGET-10-PANJPG-09A-01R 和 TARGET.10.PANJPG.09A.01R
def bSameName(name1,name2):
    bSame=getKeyWord(name1)==getKeyWord(name2)
    return bSame

with open("clinical.cart.2021-04-24.json",encoding='utf-8') as load_f:
    attribute_json = json.load(load_f)
with open('annotated_TCGA_matrix.txt',encoding='utf-8') as fd_matrix_txt:
    patient_txt_ori=fd_matrix_txt.readline().strip()+'\n'
    matrix_patient_name_list=patient_txt_ori.strip().split('\t')
    patient_gene=fd_matrix_txt.readlines()
with open('/Users/ljjia/PythonCode/Casual/51/OV_estimate_score.gct',encoding='utf-8') as fd_estimate_score:
    fd_estimate_score.readline()
    fd_estimate_score.readline()
    estimmate_patienr_name_txt_ori=fd_estimate_score.readline()
    estimmate_patienr_name_list=estimmate_patienr_name_txt_ori.strip().split('\t')
    estimmate_patienr_score_txt_ori=fd_estimate_score.readlines()

pprint.pprint(attribute_json[0]['diagnoses'][0]['submitter_id'])

def generOneLineAttr(srcList,srcJson,value,patient_name):
    bFindCnt=0
    for idx,attr in enumerate(srcJson):
        if bSameName(attr['diagnoses'][0]['submitter_id'],patient_name):
            srcList.append('\t')
            srcList.append(value)
            bFindCnt+=1
    if bFindCnt!=1:
        print("find cnt %s",bFindCnt)


def gener_result():
    print('read json name %s'%(len(attribute_json)))
    with open("result.txt",'w',encoding='utf-8') as result_fd:
        result_fd.writelines(patient_txt_ori)
        result_fd.writelines(patient_gene)
        for dictKey in json_diagnoses_attr_list:
            # 名称直接跳过
            if dictKey=='submitter_id':
                continue
            tumor_stage_list=list(dictKey)
            for patient_name in matrix_patient_name_list:
                bFindCnt = 0
                for idx, attr in enumerate(attribute_json):
                    if bSameName(attr['demographic'][0]['submitter_id'], patient_name):
                        tumor_stage_list.append('\t')
                        if(None==attr['diagnoses'][0].get(dictKey) or None==attr['diagnoses'][0][dictKey]):
                            tumor_stage_list.append('null')
                        else:
                            tumor_stage_list.append(str(attr['diagnoses'][0][dictKey]))
                        bFindCnt += 1
                if bFindCnt != 1:
                    print("find %s cnt %s"% (dictKey,bFindCnt))
            tumor_stage_list.append('\n')
            print("write json attr %s"%dictKey,len(tumor_stage_list),len(matrix_patient_name_list))
            # 写入结果文件 一个json 属性写一行
            result_fd.writelines(tumor_stage_list)


        for dictKey in json_demographic_attr_list:
            tumor_stage_list=list(dictKey)
            for patient_name in matrix_patient_name_list:
                bFindCnt = 0
                for idx, attr in enumerate(attribute_json):
                    if bSameName(attr['demographic'][0]['submitter_id'], patient_name):
                        tumor_stage_list.append('\t')
                        if (None==attr['demographic'].get(dictKey) or None == attr['demographic'][dictKey]):
                            tumor_stage_list.append('null')
                        else:
                            tumor_stage_list.append(str(attr['demographic'][dictKey]))
                        bFindCnt += 1
                if bFindCnt != 1:
                    print("find %s cnt %s"%(dictKey,bFindCnt))
            tumor_stage_list.append('\n')
            print("write json attr %s"%dictKey,len(tumor_stage_list),len(matrix_patient_name_list))
            # 写入结果文件 一个json 属性写一行
            result_fd.writelines(tumor_stage_list)

    # result_json_list=attribute_json[]
    return


    # with open("result.txt",'w',encoding='utf-8') as result_fd:
    #     result_fd.writelines(patient_txt_ori)
    #     result_fd.writelines(patient_gene)





if __name__ == '__main__':
    gener_result()

    #ret=bSameName('TARGET-10-PANJPG-09A-01R','TARGET.10.PANJPG.09A.01R')
    #ret = bSameName('TARGET-10-PANJPG-09A-01R', 'TARGET-10-PATHGY_diagnosis')
    #print(ret)