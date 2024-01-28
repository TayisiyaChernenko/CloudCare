import base64
from openai import OpenAI
import os
from dotenv import load_dotenv
from cv2 import  VideoCapture, imshow, imwrite, imencode
import numpy as np

# only called when flight program finishes
# wait some amt of time(for demo)
# seat value determined outside of this program.


def run_detection():
    # take photo
    cam_port = 0
    cam = VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        imshow("Chair", image)
        imwrite("Chair.jpg", image)
    else:
        print("No image detected. Please! try again")


    res = detect_items()
    print(res)

    (firstWord, rest) = res.split(maxsplit=1)
    if firstWord == "Yes":
        # websocket the item back (result)
        pass
    else:
        # websocket back no
        pass
        


def detect_items():
    load_dotenv()
    key = os.environ['OPENAI_API_KEY']
    client = OpenAI(api_key=key)
    with open("Chair.jpg", "rb") as image_file:
        im_b64 = base64.b64encode(image_file.read()).decode('utf-8')
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
                            "url": f"data:image/jpg;base64,{im_b64}",
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

