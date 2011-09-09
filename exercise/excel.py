# coding=utf-8
import xlrd
#directory = 'C:\\users\\eric xing\\desktop\\'
directory='./'
clic1 = 'workbook1.xls'
clic2 = 'organ_post_data.xls'

if __name__ == '__main__':
    old_user = xlrd.open_workbook(filename=directory + clic1)
    sheet = old_user.sheet_by_index(0)
    print 'reading sheet %s' % sheet.name
    new_user = xlrd.open_workbook(filename=directory + clic2)
    
