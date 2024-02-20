import g4f
from g4f.Provider import (
    Acytoo,
    Aichat,
    Ails,
    AiService,
    AItianhu,
    Bard,
    ChatgptAi,
    ChatgptLogin,
    GetGpt
)

content = input()
response = g4f.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "content"}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')