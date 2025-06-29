import pandas as pd 
import numpy as np 
import sys 
sys.stdout.reconfigure(encoding='utf-8')

def generate_data(disease_name, feature_prob, n_sample=100):
    data=[]
    for _ in range(n_sample):
        sample= {}
        for features, prob in feature_prob.items():
            sample[features]=1 if np.random.rand() < prob else 0
        sample['disease']= disease_name
        data.append(sample)
    return pd.DataFrame(data)

features = {
    "ซึม": 0.7,
    "เบื่ออาหาร": 0.7,
    "ไข้": 0.2,
    "ผอมลง": 0.95,
    "ตัวสั่น": 0.1,
    "ตายเฉียบพลัน": 0.1,
    "ขนร่วง": 0.3,
    "คอตก": 0.4,
    "เดินวน/เดินมึน": 0.05,
    "ยืนลำบาก/เดินไม่ได้": 0.6,
    "ไอ": 0.2,
    "หายใจลำบาก": 0.2,
    "มีน้ำมูก": 0.1,
    "ถ่ายเหลวผิดปกติ": 0.9,
    "ถ่ายเป็นเลือด": 0.6,
    "ขี้สีดำ/เขียวผิดปกติ": 0.7,
    "กลิ่นปากแรง": 0.2,
    "ตุ่มใส/ตุ่มหนองบริเวณผิวหนัง": 0.05,
    "แผลบริเวณลำตัว/ผิวหนัง": 0.05,
    "ผิวหนังตกสะเก็ดบริเวณลำตัว": 0.1,
    "แผลบริเวณปาก": 0.05,
    "น้ำลายไหลผิดปกติ": 0.05,
    "ตาแดง": 0.1,
    "น้ำตาไหลผิดปกติ": 0.1,
    "ขี้ตาเยอะ/ตาแฉะ": 0.1,
    "เดินกะเผลก": 0.2,
    "เต้านมอักเสบ": 0.05,
    "ต่อมน้ำเหลืองโต": 0.3,
    "บวมใต้คาง": 0.85,
    "ข้อบวม": 0.05,
    "แผลบริเวณขา/กีบ": 0.1,
}


data= generate_data("para", features, n_sample=100)

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/para.csv", index=False, encoding='utf-8-sig')