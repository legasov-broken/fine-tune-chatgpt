import os
from openai import OpenAI
from flask import Flask, request, jsonify

# Set the API key
os.environ["OPENAI_API_KEY"] = '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'
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Define the model name
model = "ft:gpt-3.5-turbo-0125:personal::95TFx11J"

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chat():
    user_content = request.json.get('content')
    if not user_content:
        return jsonify({"error": "No content provided"}), 400

    system_message = "Bạn là chatbot của Smartmind (SMDS) - một công ty môi giới chứng khoán, nhiệm vụ của bạn là hỗ trợ khách hàng trả lời những câu hỏi của họ về nền tảng này"
    messages = [
        # {"role": "system", "content": system_message},
        {"role": "user", "content": user_content},
    ]

    completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    try:
        # Assuming the API response has the 'content' directly accessible and modifiable
        response_content = completion.choices[0].message.dict()

        # Replace '\\n' with '\n' if present
        formatted_content = response_content.replace('\\n', '\n')
    except AttributeError:
        # If the expected path or operations fail, return the original content
        formatted_content = completion.choices[0].message.dict()

    # Return the formatted content in the response
    return jsonify({"response": formatted_content})

if __name__ == '__main__':
    app.run(debug=True)
