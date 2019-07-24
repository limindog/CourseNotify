#%%
import requests
import json
import re
import time
url="https://querycourse.ntust.edu.tw/QueryCourse/api/courses"
data={"CourseName": "",
"CourseNo": "",
"CourseNotes": "",
"CourseTeacher": "",
"Dimension": "",
"ForeignLanguage": 0,
"Language": "zh",
"OnleyNTUST": 0,
"OnlyGeneral": 1,
"OnlyMaster": 0,
"Semester": "1081"}
engdata={"CourseName": "",
"CourseNo": "",
"CourseNotes": "",
"CourseTeacher": "",
"Dimension": "",
"ForeignLanguage": 1,
"Language": "zh",
"OnleyNTUST": 0,
"OnlyGeneral": 0,
"OnlyMaster": 0,
"Semester": "1081"}
headers = {'Content-Type': 'application/json'}
first=[]
engfirst=[]
print("通識空缺:")
r=requests.post(url,data=json.dumps(data),headers=headers)
result=json.loads(r.text)
for i in result:
        com=re.compile("[0-9]+")
        num=com.findall(i["Contents"])
        if int(num[0])>int(i["AllStudent"]):
           print("課程代碼:{} 課程名稱:{} 課程教師:{} 課程節數:{} 目前選課人數:{} 選課上限{}".format(i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0]))
           first.append(i["CourseName"])
r.close()
requests.post('https://maker.ifttt.com/trigger/value1/with/key/c77uZwZ_UcVdPZ3wSq2jF2', data = {'value1':"this is a test"})

print("-----------------------------------------")
time.sleep(3)
print("英文空缺:")
r=requests.post(url,data=json.dumps(engdata),headers=headers)
result=json.loads(r.text)
for i in result:
        com=re.compile("[0-9]+")
        num=com.findall(i["Contents"])
        if int(num[0])>int(i["AllStudent"]):
           print("課程代碼:{} 課程名稱:{} 課程教師:{} 課程節數:{} 目前選課人數:{} 選課上限{}".format(i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0]))
           engfirst.append(i["CourseName"])
r.close()
print("-----------------------------------------")
time.sleep(3)

while True:
        r=requests.post(url,data=json.dumps(data),headers=headers)
        result=json.loads(r.text)
        second=[]
        r.close()
        for i in result:
                com=re.compile("[0-9]+")
                num=com.findall(i["Contents"])
                if int(num[0])>int(i["AllStudent"]):
                    second.append(i["CourseName"])
                    if i["CourseName"] not in first:
                        print("課程代碼:{} 課程名稱:{} 課程教師:{} 課程節數:{} 目前選課人數:{} 選課上限{}".format(i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0]))
                        r = requests.post('https://maker.ifttt.com/trigger/value1/with/key/c77uZwZ_UcVdPZ3wSq2jF2', data = {'value1':"課程代碼:{} 課程名稱:{} 課程教師:{} 課程節數:{} 目前選課人數:{} 選課上限{}".format(i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0])})
                        r.close()
                

        if second != first:
            first=second
        else:
            print("通識沒有新的空缺")
            
        print("--------------------------------------------")
        r.close()
        time.sleep(2)
        r=requests.post(url,data=json.dumps(engdata),headers=headers)
        result=json.loads(r.text)
        engsecond=[]
        r.close()
        for i in result:
                com=re.compile("[0-9]+")
                num=com.findall(i["Contents"])
                if int(num[0])>int(i["AllStudent"]):
                    engsecond.append(i["CourseName"])
                    if i["CourseName"] not in engfirst:
                        print("課程代碼:{} 課程名稱:{} 課程教師:{} 課程節數:{} 目前選課人數:{} 選課上限{}".format(i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0]))
                        r = requests.post('https://maker.ifttt.com/trigger/value1/with/key/c77uZwZ_UcVdPZ3wSq2jF2', data = {'value1':"課程代碼:{} 課程名稱:{} 課程教師:{} 課程節數:{} 目前選課人數:{} 選課上限{}".format(i["CourseNo"],i["CourseName"],i["CourseTeacher"],i["Node"],i["AllStudent"],num[0])})
                        r.close()
                

        if engsecond != engfirst:
            engfirst=engsecond
        else:
            print("英文沒有新的空缺")
            
        print("--------------------------------------------")
        time.sleep(2)
        








