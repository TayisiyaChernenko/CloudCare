import base64
from openai import OpenAI
import os
from dotenv import load_dotenv

# only called when flight program finishes
# wait some amt of time(for demo)
# seat value determined outside of this program.


def run_detection():
    # take photo

    res = detect_items()
    print(res)

    (firstWord, rest) = res.split(maxsplit=1)
    if firstWord == "Yes":
        # websocket the item back (result)
        pass
    else:
        # websocket back no
        pass
        



# delete when pi connected properly 
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def detect_items():
    load_dotenv()
    key = os.environ['OPENAI_API_KEY']
    client = OpenAI(api_key=key)
    image_path = "empty_chair.jpg"
    
    # Getting the base64 string, delete when convcert to pi
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(

        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": "Assume you are checking if someone left an item on an airplane seat. Yes or No, is there any physical object in the chair in the center of the photo? Exclude shadows. If yes, what object is in the chair?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "low"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    run_detection()

