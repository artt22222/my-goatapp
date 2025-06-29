import pandas as pd 
import numpy as np 
import sys 
sys.stdout.reconfigure(encoding='utf-8')

def generate_data(disease_name, feature_prob, n_sample=100):
    data=[]
    for _ in range(n_sample):
        sample = {}
        for features, prob in feature_prob.items():
            sample[features]= 1 if np.random.rand() < prob else 0 
        sample['disease']= disease_name
        data.append(sample)
    return pd.DataFrame(data)

features = {
    "ซึม": 0.7,
    "เบื่ออาหาร": 0.6,
    "ไข้": 0.3,
    "ผอมลง": 0.9,
    "ตัวสั่น": 0.3,
    "ตายเฉียบพลัน": 0.05,
    "ขนร่วง": 0.1,
    "คอตก": 0.4,
    "เดินวน/เดินมึน": 0.7,
    "ยืนลำบาก/เดินไม่ได้": 0.9,
    "ไอ": 0.1,
    "หายใจลำบาก": 0.1,
    "มีน้ำมูก": 0.1,
    "ถ่ายเหลวผิดปกติ": 0.05,
    "ถ่ายเป็นเลือด": 0.01,
    "ขี้สีดำ/เขียวผิดปกติ": 0.01,
    "กลิ่นปากแรง": 0.05,
    "ตุ่มใส/ตุ่มหนองผิวหนัง": 0.01,
    "แผลบริเวณผิวหนัง": 0.05,
    "ผิวหนังตกสะเก็ด": 0.05,
    "แผลบริเวณปาก/ลิ้น": 0.05,
    "น้ำลายไหลผิดปกติ": 0.05,
    "ตาแดง": 0.05,
    "น้ำตาไหลผิดปกติ": 0.05,
    "ขี้ตาเยอะ/ตาแฉะ": 0.05,
    "เดินกะเผลก": 0.95,
    "เต้านมอักเสบ": 0.3,
    "ต่อมน้ำเหลืองโต": 0.3,
    "บวมใต้คาง": 0.1,
    "ข้อบวม": 0.95,
    "แผลบริเวณขา/กีบ": 0.3,
}


data= generate_data("cae", features,n_sample=100)

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/cae.csv", index=False, encoding='utf-8-sig')
