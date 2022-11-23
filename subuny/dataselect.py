import db
import pandas as pd

result=db.select_db()
sensor=[]

for i in result:
    sensor.append(i)
    
sensordata=pd.DataFrame(sensor)
print(sensordata)
sensordata.to_csv("센서데이터.csv", encoding="euc-kr")    