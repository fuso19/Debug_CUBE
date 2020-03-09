import sys
from time import sleep
import paramiko


cube_a = '172.16.75.254'
cube_b = '172.16.75.253'

# Cria conexao ssh
conn_a = paramiko.SSHClient()
conn_a.set_missing_host_key_policy(paramiko.AutoAddPolicy)

conn_b = paramiko.SSHClient()
conn_b.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# conexoes
conn_a.connect(cube_a, username='atelecom', password='brzPWD@15')
conn_b.connect(cube_b, username='atelecom', password='brzPWD@15')

cube_a_conn = conn_a.invoke_shell()
cube_b_conn = conn_b.invoke_shell()

cube_a_conn.send('terminal length 0\n')
cube_b_conn.send('terminal length 0\n')
sleep(1)

cube_a_conn.send('clear log\n')
cube_b_conn.send('clear log\n')
sleep(1)

cube_a_conn.send('confirm\n')
cube_b_conn.send('confirm\n')
sleep(1)

cube_a_conn.send('debug ccsip messages\n')
cube_b_conn.send('debug ccsip messages\n')

print('Debug Ativado. Faça sua ligação!\n')
stop_program = input('Digite qualquer tecla para parar o debug: ')

cube_a_conn.send('undebug all\n')
cube_b_conn.send('undebug all\n')
sleep(1)


cube_a_conn.send('show log\n')
cube_b_conn.send('show log\n')
sleep(1)

log_a = cube_a_conn.recv(10000).decode('utf-8')
log_b = cube_b_conn.recv(10000).decode('utf-8')

fa = open('Log_A.txt', 'w')
fa.write(log_a)
fa.close()

fb = open('Log_B.txt', 'w')
fb.write(log_b)
fb.close()
