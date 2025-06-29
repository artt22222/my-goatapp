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
    "ซึม": 0.3,
    "เบื่ออาหาร": 0.3,
    "ไข้": 0.2,
    "ผอมลง": 0.4,
    "ตัวสั่น": 0.05,
    "ตายเฉียบพลัน": 0.01,
    "ขนร่วง": 0.95,
    "คอตก": 0.2,
    "เดินวน/เดินมึน": 0.01,
    "ยืนลำบาก/เดินไม่ได้": 0.1,
    "ไอ": 0.01,
    "หายใจลำบาก": 0.01,
    "มีน้ำมูก": 0.01,
    "ถ่ายเหลวผิดปกติ": 0.05,
    "ถ่ายเป็นเลือด": 0.01,
    "ขี้สีดำ/เขียวผิดปกติ": 0.01,
    "กลิ่นปากแรง": 0.05,
    "ตุ่มใส/ตุ่มหนองบริเวณผิวหนัง": 0.7,
    "แผลบริเวณลำตัว/ผิวหนัง": 0.9,
    "ผิวหนังตกสะเก็ดบริเวณลำตัว": 0.8,
    "แผลบริเวณปาก": 0.2,
    "น้ำลายไหลผิดปกติ": 0.2,
    "ตาแดง": 0.1,
    "น้ำตาไหลผิดปกติ": 0.1,
    "ขี้ตาเยอะ/ตาแฉะ": 0.1,
    "เดินกะเผลก": 0.3,
    "เต้านมอักเสบ": 0.2,
    "ต่อมน้ำเหลืองโต": 0.4,
    "บวมใต้คาง": 0.2,
    "ข้อบวม": 0.1,
    "แผลบริเวณขา/กีบ": 0.6,
}


data= generate_data("skin", features, n_sample=100)

print(data.drop(columns='disease').mean()*100)

data.to_csv("case/skin.csv", index=False, encoding='utf-8-sig')