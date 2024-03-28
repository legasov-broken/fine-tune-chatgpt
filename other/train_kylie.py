# import json

# # Path to the input text file
# input_file_path = '100 Q&A with Kylie Jenner on TikTok.txt'
# # Path to the output JSONL file
# output_file_path = 'path_to_your_output_file.jsonl'

# individual_qa_pairs = []

# with open(input_file_path, 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# # Initialize a variable to temporarily hold the question
# question = ""

# for line in lines:
#     # Check if the line contains a question
#     if "Q: " in line:
#         # Extract everything after "Q: "
#         question = line.strip().split("Q: ", 1)[1]
#     # Check if the line contains an answer and if there's an existing question to pair with
#     elif "A " in line:
#         # Extract everything after "A: "
#         answer = line.strip().split("A ", 1)[1]
#         # Construct the QA pair in the desired JSON structure
#         qa_interaction = {
#             "messages": [
#                 {"role": "system", "content": "You are a Kylie-bot that understand the product and talk like Kylie"},
#                 {"role": "user", "content": question},
#                 {"role": "assistant", "content": answer}
#             ]
#         }
#         individual_qa_pairs.append(qa_interaction)
#         question = ""  # Reset the question for the next pair

# # Writing the transformed data to a JSONL file
# with open(output_file_path, 'w', encoding='utf-8') as outfile:
#     for qa_pair in individual_qa_pairs:
#         json_line = json.dumps(qa_pair) + '\n'
#         outfile.write(json_line)

# print(f'Transformed Q&A pairs have been saved to {output_file_path}')



# # Khởi tạo hai file đầu ra cho train và val
# file_path = 'other/kylie-data.jsonl'
# train_file_path = 'other/train.jsonl'
# val_file_path = 'other/val.jsonl'

# # Đọc file .jsonl, chia, và ghi vào hai file mới
# with open(file_path, 'r', encoding='utf-8') as input_file, \
#      open(train_file_path, 'w', encoding='utf-8') as train_file, \
#      open(val_file_path, 'w', encoding='utf-8') as val_file:
    
#     # Đếm số dòng để xác định khi nào ghi vào train và khi nào ghi vào val
#     line_counter = 0
    
#     for line in input_file:
#         if line_counter < 8:  # 8 dòng đầu tiên cho train
#             train_file.write(line)
#         else:  # 2 dòng sau cho val
#             val_file.write(line)
        
#         line_counter += 1
#         if line_counter == 10:  # Đặt lại bộ đếm sau mỗi 10 dòng
#             line_counter = 0

# # Trả về đường dẫn của hai file mới
# train_file_path, val_file_path



import os
from openai import OpenAI
from flask import Flask, request, jsonify

# Set the API key
os.environ["OPENAI_API_KEY"] = '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'
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Define the model name
model = "ft:gpt-3.5-turbo-0125:personal::97FF0Gjf"

def chat_gpt(user_content): 
    system_message = "You are a Kylie-bot that understand the product and talk like Kylie"
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_content},
    ]

    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return completion.choices[0].message.content.strip()

if __name__ == '__main__':
    while True:
        user_input = input("You:")
        response = chat_gpt(user_input)
        print("Chatbot: ",response)

