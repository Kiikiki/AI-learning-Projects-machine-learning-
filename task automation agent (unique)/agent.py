from google import genai
from emailTool import authenticateGmail, getEmails, thisWeekEmail
from taskTool import uploadTask, viewTasks, deleteTask, finishTaskManual, finishTaskAgent
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

# connection to an LLM
client = genai.Client(api_key=apiKey)

# test LLM connection (works!)
# response = client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents = "say hello to the world!" 
# )
# print("[Assistant]: " + response.text)

# what the LLM does:

# load emails from both accounts

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

taskList = []

# task
while True:
    print("\nWelcome What would you like to do?")
    print("1. Upload Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Check Task Completion by Email")
    print("6. Exit")

    choice = input("\nEnter your choice: ") 
    if choice == '1':
        taskList = uploadTask(taskList)
    elif choice == '2':
        viewTasks(taskList)
    elif choice == '3':
        taskList = deleteTask(taskList)
    elif choice == '4':
        finishTaskManual(taskList)
    elif choice == '5':
        finishTaskAgent(taskList, recentEmails, client)
    elif choice == '6':
        print("\nExiting...")
        break
