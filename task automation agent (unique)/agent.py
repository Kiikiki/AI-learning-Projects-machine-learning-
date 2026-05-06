
from openai import OpenAI
from emailTool import authenticateGmail, getEmails, thisWeekEmail

# connection to an LLM
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4.1",
    messages=[
        { "role": "user", "content": "Remind me of of my schedule, tasks and organize my emails" }
    ]
)

print(response.choices[0].message.content)

scopes = ['https://www.googleapis.com/auth/gmail.readonly']

servicePersonal = authenticateGmail('credentialsPersonal.json', 8080)
serviceWork = authenticateGmail('credentialsWork.json', 0)

print("\nAuthentication successful for both accounts!")

personalMails = getEmails(servicePersonal)
print("\nFetched personal emails...")

workMails = getEmails(serviceWork)
print("\nFetched work emails.")

emails = personalMails + workMails
print("\nCompiled all emails from both accounts.")

recentEmails = thisWeekEmail(emails)
print("\nFiltered emails from the last week.")
print(f"\nYou have {len(recentEmails)} emails from the last week.")




