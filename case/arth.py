import pandas as pd
import numpy as np
import sys 
sys.stdout.reconfigure(encoding='utf-8')

features = {
    "ซึม": 0.6,
    "เบื่ออาหาร": 0.4,
    "ไข้": 0.4,
    "ผอมลง": 0.5,
    "ตัวสั่น": 0.1,
    "ตายเฉียบพลัน": 0.01,
    "ขนร่วง": 0.05,
    "คอตก": 0.2,
    "เดินวน/เดินมึน": 0.01,
    "ยืนลำบาก/เดินไม่ได้": 0.6,
    "ไอ": 0.01,
    "หายใจลำบาก": 0.02,
    "มีน้ำมูก": 0.05,
    "ถ่ายเหลวผิดปกติ": 0.05,
    "ถ่ายเป็นเลือด": 0.01,
    "ขี้สีดำ/เขียวผิดปกติ": 0.01,
    "กลิ่นปากแรง": 0.05,
    "ตุ่มใส/ตุ่มหนองผิวหนัง": 0.05,
    "แผลบริเวณผิวหนัง": 0.05,
    "ผิวหนังตกสะเก็ด": 0.05,
    "แผลบริเวณปาก/ลิ้น": 0.01,
    "น้ำลายไหลผิดปกติ": 0.01,
    "ตาแดง": 0.01,
    "น้ำตาไหลผิดปกติ": 0.01,
    "ขี้ตาเยอะ/ตาแฉะ": 0.01,
    "เดินกะเผลก": 0.95,
    "เต้านมอักเสบ": 0.05,
    "ต่อมน้ำเหลืองโต": 0.2,
    "บวมใต้คาง": 0.5,
    "ข้อบวม": 0.95,
    "แผลบริเวณขา/กีบ": 0.4,
}

def generate_data(disease_name, feature_prob, n_sample=100):
    data=[]
    for _ in range(n_sample):
        sample = {}
        for features, prob in feature_prob.items():
            sample[features]=1 if np.random.rand()< prob else 0 
        sample['disease']= disease_name
        data.append(sample)
    return pd.DataFrame(data)

data= generate_data("arth", features, n_sample=100)

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/arth.csv", index=False, encoding='utf-8-sig')