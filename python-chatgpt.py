import openai
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("message",help="To print python script by sending request to Open API")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = os.environ.get('OPENAI_API_KEY')
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

response = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages = [
        {"role": "user" ,"content": f"write a python script to {args.message}.Provide only code not text"}
    ],
    max_tokens= 500,
    temperature =  0.5  
)

response = OpenAI.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()['choices'][0]['message']['content']
    with open(args.file_name, "w") as file:
        file.write(response_text)

else:
    print(f"Request failed with status code: {str(response.status_code)}")
