# SHA256_Crack
-Simple program to find a string that has been hashed with sha256 algorithm using MPI4PY
-To run this program you need mpiexec https://www.microsoft.com/en-us/download/details.aspx?id=57467
-Open a terminal and enter "mpiexec -n [ NUMBER_OF_PROCESSES ] python Password_Cracking.py [ 4_LETTER_STRING ]"
-This program can only crack 4 letter strings that include 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' with no spaces
