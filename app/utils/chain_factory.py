# from langchain.llms import OpenAI, Cohere, HuggingFaceHub
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# import os

# def get_llm(provider: str):
#     if provider == "openai":
#         return OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
#     elif provider == "cohere":
#         return Cohere(cohere_api_key=os.getenv("COHERE_API_KEY"))
#     elif provider == "huggingface":
#         return HuggingFaceHub(repo_id="gpt2", huggingfacehub_api_token=os.getenv("HF_API_KEY"))
#     else:
#         raise ValueError("Unsupported LLM provider")

# def build_chain(provider: str, task_type: str = "summary"):
#     llm = get_llm(provider)

#     if task_type == "summary":
#         prompt = PromptTemplate(
#             input_variables=["input"],
#             template="Summarize the following search results:\n\n{input}\n\nSummary:"
#         )
#     elif task_type == "qa":
#         prompt = PromptTemplate(
#             input_variables=["input"],
#             template="Answer the following question based on available info:\n\n{input}\n\nAnswer:"
#         )
#     else:
#         raise ValueError("Unsupported task type")

#     chain = LLMChain(llm=llm, prompt=prompt)
#     return chain