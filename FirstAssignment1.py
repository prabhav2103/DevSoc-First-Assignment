from openai import OpenAI
import os
import json
client = OpenAI(
    api_key="key",
    base_url="https://api.groq.com/openai/v1",
)

file_object = open("text.txt", "r")
listOfLines = file_object.readlines()
for line in listOfLines:
    response = client.responses.create(
        input=line,
        model="openai/gpt-oss-20b",
    )
    data = {
        "input":line,
        "output":response.output_text
    }
    with open("Responses.json", "a") as f:
        json.dump(data, f)
        f.write("\n")