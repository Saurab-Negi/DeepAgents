from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

while True:
    query = input("User: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting the Q&A bot. Goodbye!")
        break

    res = llm.invoke(query)
    print("AI: ", res.content, "\n")