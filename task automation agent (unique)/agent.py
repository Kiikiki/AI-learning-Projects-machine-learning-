from google import genai
from emailTool import authenticateGmail, getEmails, thisWeekEmail
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

# connection to an LLM
client = genai.Client(api_key="apiKey")

# test LLM connection (works!)
# response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents = "say hello to the world!" 
# )

# print(response.text)

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = ""
)

# what the LLM does:

# email tool
# scopes = ['https://www.googleapis.com/auth/gmail.readonly']

# servicePersonal = authenticateGmail('credentialsPersonal.json', 8080)
# serviceWork = authenticateGmail('credentialsWork.json', 0)

# print("\nAuthentication successful for both accounts!")

# personalMails = getEmails(servicePersonal)
# print("\nFetched personal emails...")

# workMails = getEmails(serviceWork)
# print("\nFetched work emails.")

# emails = personalMails + workMails
# print("\nCompiled all emails from both accounts.")

# recentEmails = thisWeekEmail(emails)
# print("\nFiltered emails from the last week.")
# print(f"\nYou have {len(recentEmails)} emails from the last week.")




