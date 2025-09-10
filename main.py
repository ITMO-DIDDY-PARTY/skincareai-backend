from openai import OpenAI 
import base64

MODEL="gpt-4o-mini"
KEY = "GPT_KEY"
client = OpenAI(api_key=KEY)

def encode_image(image: bytes):
    return base64.b64encode(image).decode("utf-8")

def generate_recipe_from_img(image: bytes, type: str | None = None) -> str:
    base64_image = encode_image(image)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": f"You are an experienced skin care expert that only answers in Markdown format. Analyze given picture and give your diagnosis for this skin care problem, if you cant see any then just give skin care tips to keep it up. if you can diagnose any problems, give advice on how to heal that. Of course we will consult specialist anyways."},
            {"role": "user", "content": [
                {"type": "text", "text": "What can be done with this type of skin? Do you see any issues over there?"},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"}
                }
            ]}
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content
