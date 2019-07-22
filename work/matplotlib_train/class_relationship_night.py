import json
import matplotlib.pyplot as plt
# 读取解析文件
input = open(r"C:\Users\root\Desktop\class_relationship.txt","r")
param = input.read()
input.close()



plt.figure()

# 以名称为key值  重新创建数据
points = {}

#解析json数据
json_param = json.loads(param)
for data in json_param:
    points["{}".format(data["shortName"])] = data

xmlbean = {"xaxis": 0, "yaxis": 0}
points["XmlBeanFactory"] = xmlbean
print(points)
for data in json_param:
    currentClassName = data["shortName"]
    nextClassName = data["nextShortName"]
    nextClassObject = points[nextClassName]
    xaxis = data["xaxis"]
    yaxis = data["yaxis"]

    plt.plot((xaxis,nextClassObject["xaxis"]), (data["yaxis"],nextClassObject["yaxis"]),\
            # color='r', markerfacecolor='blue', marker='o',drawstyle="steps-pre")
            color='r', markerfacecolor='blue', marker='o')
    if(xaxis % 2 == 0):
        plt.text(xaxis,yaxis + 0.1,data["shortName"], ha='center', va='bottom', fontsize=10)
    else:
        plt.text(xaxis, yaxis - 0.1, data["shortName"], ha='center', va='bottom', fontsize=10)
plt.axis("off")
plt.show()
