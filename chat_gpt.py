from openai import OpenAI
import os
import openai

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


# client.files.create(
#   file=open("data.jsonl", "rb"),
#   purpose="fine-tune"
# )

client.fine_tuning.jobs.create(
  training_file="file-abc123", 
  model="gpt-3.5-turbo"
)