from hashlib import sha256
from mpi4py import MPI
from time import time
from sys import argv
import numpy as np
import string
english_all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
char_array = np.array(list(english_all))
char_array_len = len(char_array)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

msg = [0,0,0]
if rank == 0:
    start_time = time()
    hashed_string = sha256(argv[1].encode()).hexdigest()
    msg[2] = hashed_string
    print("SHA256    -> "+ hashed_string)
    #print("Raw input -> "+ argv[1])
    for i in range(1,size):
        chunk_size = char_array_len / size
        temp = 0
        if chunk_size % 2 != 0:
            temp = 1
        chunk_size = int(chunk_size + temp)
        msg[1] = char_array[ (i-1)*chunk_size : (i-1)*chunk_size + chunk_size ]
        comm.send(msg,dest=i,tag=i)
    for i in range(1, size):
        recvd = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG)
        if recvd[2] == True:
            print("FOUND!")
            print(str(recvd[1]))
            end_time = time()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            break
        print("NOT FOUND")

else:
    my_msg = comm.recv(source=0, tag=rank)
    result = ""
    for i in my_msg[1]:
        for j in char_array:
            for k in char_array:
                for l in char_array:
                    result = i+j+k+l
                    hashed_string = sha256(result.encode()).hexdigest()
                    if hashed_string == my_msg[2]:
                        print(result)
                        msg[0], msg[1], msg[2] = rank, result, True
                        comm.send(msg,dest=0,tag=0)
                        exit(0)
    msg[0], msg[1], msg[2] = rank, " ", True
    comm.send(msg,dest=0,tag=0)