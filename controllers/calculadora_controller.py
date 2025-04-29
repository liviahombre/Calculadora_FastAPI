from fastapi import APIRouter, HTTPException
from models.operacao import Operacao

router = APIRouter()

@router.post("/soma")
async def soma(op: Operacao):
    return {"operacao": "soma", "resultado": op.soma()}

@router.post("/subtracao")
async def subtracao(op: Operacao):
    return {"operacao": "subtracao", "resultado": op.subt()}

@router.post("/multiplicacao")
async def multiplicacao(op: Operacao):
    return {"operacao": "multiplicacao", "resultado": op.mult()}

@router.post("/divisao")
async def divisao(op: Operacao):
    try:
        resultado = op.div()
        return {"operacao": "divisao", "resultado": resultado}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
