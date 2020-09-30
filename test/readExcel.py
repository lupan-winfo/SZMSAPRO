#coding=utf-8
import xlrd
import os
class ExcelUtil(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = os.path.join(os.path.abspath('..') + "/config/" + "mmsi.xls")
        if index == None:
            index = 0
        # 打开Excel
        self.data = xlrd.open_workbook(excel_path)
        # 获取sheet页
        self.table = self.data.sheets()[index]
        # 获取Excel数据行数
        self.rows = self.table.nrows
        # 获取Excel数据列数
        self.cols = self.table.ncols

    def get_data(self):
        result = []
        for i in range(self.rows):
            # 以list形式获取行数据
            col = self.table.row_values(i)
            result.append(col)
        return result