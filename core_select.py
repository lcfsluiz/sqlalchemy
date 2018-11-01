from sqlalchemy import select
from core import user_table
from pprint import pprint

result = select([user_table])
result2 = select([user_table]).where(user_table.c.nome == 'daniel')

# for x in result.execute():
#     print(x[4].strftime('%d-%m-%Y %H:%M:%S'))

# print([x for x in result2.execute()])
# # print([x for x in result.execute()])

pprint([x for x in select([user_table]).execute()])