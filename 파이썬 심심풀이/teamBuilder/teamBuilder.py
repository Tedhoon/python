import random
import pandas as pd

path = r'C:\Users\82106\Desktop\멋쟁이사자처럼 8기\멋쟁이 사자처럼 8기 전수조사_부산대(장전캠퍼스).xlsx'
df = pd.ExcelFile(path).parse('부산대(장전캠퍼스)')
likelion = df['이름'].values[3:19]
shuffle = sorted(likelion, key=lambda x: random.random())
[print(f"team{i+1} : {shuffle[i*4:i*4+4]}") for i in range(4)]
