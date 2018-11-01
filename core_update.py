from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'daniel')

commit = atualizar.values(nome='daniel prata', idade=24)
result = con.execute(commit)
print(result.rowcount)