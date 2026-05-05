# connection to an LLM
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4.1",
    messages=[
        { "role": "user", "content": "Remind me of of my schedule, tasks and organize my emails" }
    ]
)

print(response.choices[0].message.content)

# tools
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# let it call Gmail API to read email
scopes = ['https://www.googleapis.com/auth/gmail.readonly']
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)

# will open a browser to ask for perms
credentials = flow.run_local_server(port=0) 
service = build('gmail', 'v1', credentials=credentials)

def get_schedule():

def get_tasks():

def organize_emails():
    emails = service.users().messages().list(userId='me').execute
    messages = emails.get('messages', [])

    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        emails.append(txt)