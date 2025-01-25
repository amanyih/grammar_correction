import os
import csv
from datasets import load_dataset

REPLACEMENTS = [
    (" .", "."), 
    (" ,", ","), 
    (" '", "'"), 
    (" ?", "?"), 
    (" !", "!"), 
    (" :", ":"), 
    (" ;", ";"), 
    (" n't", "n't"), 
    ("2 0 0 6", "2006"), 
    ("5 5", "55"), 
    ("4 0 0", "400"), 
    ("1 7-5 0", "1750"), 
    ("2 0 %", "20%"), 
    ("5 0", "50"), 
    ("1 2", "12"), 
    ("1 0", "10"), 
    ('" ballast water', '"ballast water')
]

def remove_excess_spaces(text):
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text

def generate_csv(csv_path, dataset):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["input", "target"])
        for case in dataset:
            input_text = "grammar: " + case["sentence"]
            input_text = remove_excess_spaces(input_text)
            for correction in case["corrections"]:
                correction = remove_excess_spaces(correction)
                if input_text and correction:
                    writer.writerow([input_text, correction])

train_dataset = load_dataset("jfleg", split="validation[:]") 
eval_dataset = load_dataset("jfleg", split="test[:]")

generate_csv("Dataset/JFLEG/train.csv", train_dataset)
generate_csv("Dataset/JFLEG/eval.csv", eval_dataset)

c4_dataset = load_dataset("liweili/c4_200m", split="train", streaming=True)

def c4_generate_csv(csv_path, iterator, num_examples):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["input", "target"])
        for _ in range(num_examples):
            try:
                data = next(iterator)
                input_text = "grammar: " + data["input"]
                input_text = remove_excess_spaces(input_text)
                correction = remove_excess_spaces(data["output"])
                if input_text and correction:
                    writer.writerow([input_text, correction])
            except StopIteration:
                break

c4_iterator = iter(c4_dataset)
c4_generate_csv("Dataset/C4_200M/c4data.csv", c4_iterator, num_examples=3500)
