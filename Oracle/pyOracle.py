import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_21_9")

dsn_tns = cx_Oracle.makedsn('192.170.10.6', '1521', service_name='ORCL')
conn = cx_Oracle.connect(user='GESTAO', password='sah', dsn=dsn_tns)

cursor = conn.cursor()
cursor.execute("SELECT APELIDO FROM EMPRESA")
results = cursor.fetchall()

for row in results:
    print("{0:10}".format(row[0]))

cursor.close()
conn.close()
