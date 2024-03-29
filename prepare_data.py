# from docx import Document
# import json

# def extract_qa_pairs(doc_path):
#     doc = Document(doc_path)
#     qa_pairs = []
#     current_q = None
#     current_a = ""
#     for para in doc.paragraphs:
#         text = para.text.strip()
#         if text.startswith("Q:"):
#             if current_q is not None:  # Save the previous Q&A pair
#                 qa_pairs.append({"question": current_q, "answer": current_a.strip()})
#                 current_a = ""  # Reset answer for next pair
#             current_q = text[2:].strip()  # Capture new question
#         elif current_q is not None:  # Collecting answer
#             if text.endswith("?"):  # Check if it's the end of a question
#                 current_a += text  # Append to answer
#                 # Optionally, check for next question number logic here
#             else:
#                 current_a += text + " "  # Continue collecting answer
#     # Add the last Q&A pair if not added
#     if current_q and current_a.strip():
#         qa_pairs.append({"question": current_q, "answer": current_a.strip()})
#     return qa_pairs

# def convert_to_jsonl(qa_pairs, output_path):
#     with open(output_path, "w", encoding="utf-8") as f:
#         for pair in qa_pairs:
#             entry = {
#                 "messages": [
#                     {"role": "system", "content": "You are discussing Lenovo GM2 earbuds during a TikTok Live session."},
#                     {"role": "user", "content": pair["question"]},
#                     {"role": "assistant", "content": pair["answer"]}
#                 ]
#             }
#             f.write(json.dumps(entry) + "\n")

# if __name__ == "__main__":
#     doc_path = "100-QA-with-AI.docx"  # Update this to your document's path
#     output_path = "output_file.jsonl"  # Desired output path
#     qa_pairs = extract_qa_pairs(doc_path)
#     convert_to_jsonl(qa_pairs, output_path)
#     print("Conversion complete. Output saved to:", output_path)



# Correcting the splitting approach as per the new instructions
import json
file_path = "smds-clear-data.jsonl"
# Resetting the read of the file to handle the new instruction
data = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        data.append(json.loads(line))

# New approach to split data: 8 for train, then 2 for val, and so on until the end of the dataset
train_data_corrected = []
val_data_corrected = []

# Splitting the data according to the new pattern
for i in range(0, len(data), 10):  # Increment by 10 since each cycle includes 8 train + 2 val
    train_data_corrected.extend(data[i:i+8])  # Next 8 for training
    val_data_corrected.extend(data[i+8:i+10])  # Following 2 for validation

# Writing the corrected split data back to new JSONL files
train_file_path_corrected = 'train_data_corrected.jsonl'
val_file_path_corrected = 'val_data_corrected.jsonl'

# Writing corrected training data
with open(train_file_path_corrected, 'w', encoding='utf-8') as file:
    for item in train_data_corrected:
        file.write(json.dumps(item, ensure_ascii=False) + '\n')

# Writing corrected validation data
with open(val_file_path_corrected, 'w', encoding='utf-8') as file:
    for item in val_data_corrected:
        file.write(json.dumps(item, ensure_ascii=False) + '\n')

train_file_path_corrected, val_file_path_corrected, len(train_data_corrected), len(val_data_corrected)
