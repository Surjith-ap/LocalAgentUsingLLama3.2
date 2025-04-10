from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")
template = """
You are an expert in answering questions about the lullu mall
Here are some reviews:
{reviews}

Here is the question:
{question}

"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    question = input("Enter a question(Enter q to quit): ")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)
