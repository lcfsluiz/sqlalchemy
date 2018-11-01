from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

# new = ins.values(idade=24, nome='daniel', senha='teste123')
# con.execute(new)


con.execute(ins, [
    {'nome': 'marcio', 'idade': 21, 'senha': 'semsenha'},
    {'nome': 'gustavo', 'idade': 18, 'senha': 'abacaxi123'},
    {'nome': 'guilherme', 'idade': 22, 'senha': 'goiaba123'}


])
