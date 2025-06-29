import sys
import pandas as pd
import numpy as np
sys.stdout.reconfigure(encoding='utf-8')

features = {
    "ซึม": 0.8,
    "เบื่ออาหาร": 0.8,
    "ไข้": 0.9,
    "ผอมลง": 0.5,
    "ตัวสั่น": 0.3,
    "ตายเฉียบพลัน": 0.3,
    "ขนร่วง": 0.05,
    "คอตก": 0.4,
    "เดินวน/เดินมึน": 0.05,
    "ยืนลำบาก/เดินไม่ได้": 0.3,
    "ไอ": 0.9,
    "หายใจลำบาก": 0.9,
    "มีน้ำมูก": 0.8,
    "ถ่ายเหลวผิดปกติ": 0.5,
    "ถ่ายเป็นเลือด": 0.01,
    "ขี้สีดำ/เขียวผิดปกติ": 0.01,
    "กลิ่นปากแรง": 0.2,
    "ตุ่มใส/ตุ่มหนองผิวหนัง": 0.01,
    "แผลบริเวณผิวหนัง": 0.05,
    "ผิวหนังตกสะเก็ด": 0.01,
    "แผลบริเวณปาก/ลิ้น": 0.1,
    "น้ำลายไหลผิดปกติ": 0.1,
    "ตาแดง": 0.1,
    "น้ำตาไหลผิดปกติ": 0.1,
    "ขี้ตาเยอะ/ตาแฉะ": 0.1,
    "เดินกะเผลก": 0.05,
    "เต้านมอักเสบ": 0.05,
    "ต่อมน้ำเหลืองโต": 0.4,
    "บวมใต้คาง": 0.1,
    "ข้อบวม": 0.05,
    "แผลบริเวณขา/กีบ": 0.05,
}


def generate_data(disease_name, feature_prob, n_sample=100):
    data=[]
    for _ in range(n_sample):
        sample={}
        for features,prob in feature_prob.items():
            sample[features]=1 if np.random.rand()< prob else 0
        sample['disease']= disease_name
        data.append(sample)
    return pd.DataFrame(data)

data=generate_data("bp", features, n_sample=100)

print(data.head())

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/bp.csv", index=False, encoding='utf-8-sig')
            