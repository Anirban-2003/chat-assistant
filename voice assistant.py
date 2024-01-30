import pyttsx3
import openai

openai.api_key = "###"
user_input=input()

messages = [{"role": "system", "content": "chatbot"}]
messages.append({"role": "user", "content": user_input})

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

ChatGPT_reply = response["choices"][0]["message"]["content"]
text_speech = pyttsx3.init()
text_speech.say(ChatGPT_reply)
print(ChatGPT_reply)
text_speech.runAndWait()
