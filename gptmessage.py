# coding=windows-1251
import g4f
import time
from g4f.Provider import (
    Chatgpt4Online,
    PerplexityLabs,
    ChatgptDemoAi,
    GeminiProChat,
    ChatgptNext,
    HuggingChat,
    ChatgptDemo,
    FreeChatgpt,
    GptForLove,
    ChatgptAi,
    DeepInfra,
    ChatBase,
    Liaobots,
    FreeGpt,
    Llama2,
    Vercel,
    Gemini,
    GptGo,
    Gpt6,
    You,
    Pi,
)
def get_responce(content):
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        provider=GeminiProChat,
        messages=[{"role": "user", "content": content}],
        stream=True,
    )

    message = ''
    
    for word in response:
        message += word
    return message
