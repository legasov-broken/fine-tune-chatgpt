import json

# Path to the input text file
input_file_path = '100 Q&A with Kylie Jenner on TikTok.txt'
# Path to the output JSONL file
output_file_path = 'path_to_your_output_file.jsonl'

individual_qa_pairs = []

with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize a variable to temporarily hold the question
question = ""

for line in lines:
    # Check if the line contains a question
    if "Q: " in line:
        # Extract everything after "Q: "
        question = line.strip().split("Q: ", 1)[1]
    # Check if the line contains an answer and if there's an existing question to pair with
    elif "A " in line:
        # Extract everything after "A: "
        answer = line.strip().split("A ", 1)[1]
        # Construct the QA pair in the desired JSON structure
        qa_interaction = {
            "messages": [
                {"role": "system", "content": "You are a Kylie-bot that understand the product and talk like Kylie"},
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer}
            ]
        }
        individual_qa_pairs.append(qa_interaction)
        question = ""  # Reset the question for the next pair

# Writing the transformed data to a JSONL file
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    for qa_pair in individual_qa_pairs:
        json_line = json.dumps(qa_pair) + '\n'
        outfile.write(json_line)

print(f'Transformed Q&A pairs have been saved to {output_file_path}')