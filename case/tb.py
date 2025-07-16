import pandas as pd 
import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')

features = {
    "ซึม": 0.7,
    "เบื่ออาหาร": 0.7,
    "ไข้": 0.6,
    "ผอมลง": 0.9,
    "ตัวสั่น": 0.1,
    "ตายเฉียบพลัน": 0.0,
    "ขนร่วง": 0.2,
    "คอตก": 0.1,
    "เดินวน/เดินมึน": 0.0,
    "ยืนลำบาก/เดินไม่ได้": 0.1,
    "ไอ": 0.9,
    "หายใจลำบาก": 0.8,
    "มีน้ำมูก": 0.7,
    "ถ่ายเหลวผิดปกติ": 0.1,
    "ถ่ายเป็นเลือด": 0.0,
    "ขี้สีดำ/เขียวผิดปกติ": 0.0,
    "กลิ่นปากแรง": 0.1,
    "ตุ่มใส/ตุ่มหนองผิวหนัง": 0.0,
    "แผลบริเวณผิวหนัง": 0.1,
    "ผิวหนังตกสะเก็ด": 0.0,
    "แผลบริเวณปาก/ลิ้น": 0.0,
    "น้ำลายไหลผิดปกติ": 0.1,
    "ตาแดง": 0.1,
    "น้ำตาไหลผิดปกติ": 0.1,
    "ขี้ตาเยอะ/ตาแฉะ": 0.1,
    "เดินกะเผลก": 0.2,
    "เต้านมอักเสบ": 0.0,
    "ต่อมน้ำเหลืองโต": 0.8,
    "บวมใต้คาง": 0.0,
    "ข้อบวม": 0.1,
    "แผลบริเวณขา/กีบ": 0.0,
}

def generate_data(disease_name, feature_prob, n_sample=100):
    data=[]
    for _ in range(n_sample):
        sample= {}
        for features, prob in feature_prob.items():
            sample[features]=1 if np.random.rand()< prob else 0
        sample['disease']= disease_name
        data.append(sample)
    return pd.DataFrame(data)

data = generate_data("tb", features, n_sample=100)

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/tb.csv", index=False, encoding='utf-8-sig')