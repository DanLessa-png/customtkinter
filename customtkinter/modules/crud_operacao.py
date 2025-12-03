import uuid, os, json
FILE_PATH = "data/operacao.txt"

def criar(dados):
    dados["id"] = str(uuid.uuid4())
    with open(FILE_PATH,"a") as f: f.write(json.dumps(dados)+"\n")

def listar():
    if not os.path.exists(FILE_PATH): return []
    with open(FILE_PATH,"r") as f: return [json.loads(l.strip()) for l in f if l.strip()]

def atualizar(id_, novos_dados):
    registros = listar()
    with open(FILE_PATH,"w") as f:
        for r in registros:
            if r["id"] == id_: r.update(novos_dados)
            f.write(json.dumps(r)+"\n")

def deletar(id_):
    registros = listar()
    with open(FILE_PATH,"w") as f:
        for r in registros:
            if r["id"] != id_: f.write(json.dumps(r)+"\n")
