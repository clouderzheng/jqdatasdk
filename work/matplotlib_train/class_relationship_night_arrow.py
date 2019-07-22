import json
import matplotlib.pyplot as plt

def read_txt(path):
    """
    读取文件信息
    :param path:
    :return:
    """
    input = open(path, "r")
    param = input.read()
    input.close()
    return param

def draw_class_ration(data_shortName_map,param ):
    plt.figure()

    ax = plt.axes()
    # 遍历层级关系
    for data in param:
        nextObject = data_shortName_map[data["nextShortName"]]
        ax.arrow(nextObject["xaxis"], nextObject["yaxis"], data["xaxis"], data["yaxis"], head_width=0.05, head_length=0.1, fc='k', ec='k')
    plt.axis("off")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.show()

path = r"C:\Users\root\Desktop\class_relationship.txt"
param = read_txt(path)

data_shortName_map = {}
# 手动构造第一个节点
xmlbean = {"xaxis": 0, "yaxis": 0}
data_shortName_map["XmlBeanFactory"] = xmlbean
json_param = json.loads(param)
for data in json_param:
    data_shortName_map["{}".format(data["shortName"])] = data

draw_class_ration(data_shortName_map,json_param)
