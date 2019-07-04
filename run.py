#/bin/env python
# encoding: utf-8

from os import path,getenv,system
from datetime import datetime
from xml.etree.ElementTree import ElementTree,Element
from datetime import datetime

# plist 路径, 从环境变量中获取
plist_file = getenv("PRODUCT_SETTINGS_PATH")

# plist 文件存在时才开始替换
if (plist_file != None) and (path.exists(plist_file)):
    
    # 替换前先备份, 防止出错导致损坏文件
    system('cp "%s" "%s"' % (plist_file, plist_file+'.bak') )
    
    tree = ElementTree()
    root = tree.parse(plist_file)
    
    # 读取所有节点
    all_data = root.findall('dict/*')
    
    # 找到版本标记位
    next_to_stop = False
    
    for row in all_data:
        if next_to_stop:
            # 替换成当前日期,格式为 yyyy-mm-dd
            text = datetime.strftime(datetime.now(), "%y-%m-%d %H:%M")
            row.text = text
            break
            
        # 找到 CFBundleVersion 位置
        if row.text == 'CFBundleVersion':
            next_to_stop = True

# 将修改写入 plist 文件
tree.write(plist_file, encoding="utf-8",xml_declaration=True)
