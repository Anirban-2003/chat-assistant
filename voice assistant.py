import openai
import pyttsx3

openai.api_key = "###"

messages = [{"role": "system", "content": "chatbot"}]
while(1):
    user_input=input()
    if user_input=="stop":
        break
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    
    text_speech = pyttsx3.init()
    text_speech.say(ChatGPT_reply)
    print(ChatGPT_reply)
    text_speech.runAndWait()
