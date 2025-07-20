from fastapi import APIRouter, Body
from app.utils.chain_factory import build_chain

router = APIRouter()

@router.post("/")
async def process_llm(provider: str = Body(...), input: str = Body(...), task_type: str = Body("summary")):
    chain = build_chain(provider=provider, task_type=task_type)
    result = chain.run(input)
    return {"response": result}