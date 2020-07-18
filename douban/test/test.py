import xlwt

workbook = xlwt.Workbook(encoding="utf-8")    #创建workbook对象
worksheet = workbook.add_sheet('sheet1')      #创建工作表
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            worksheet.write(i-1,j-1,"%d * %d = %d"%(j,i,i*j))                  #行 列 内容
        else:
            break
workbook.save('student.xls')                  #保存数据表
