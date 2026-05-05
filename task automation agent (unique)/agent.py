from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4.1",
    messages=[
        { "role": "user", "content": "Remind me of of my schedule, tasks and organize my emails" }
    ]
)

print(response.choices[0].message.content)