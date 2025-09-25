This is the source code for the SSHC project by qusai elwazir

File organization:
./root/sshC.py - source code for computer computer component of the project.
./public_key.pem - public key used to verify signatures

./smartCard/src_remote.py - remote source code to run on the pi
./smartCard/sig - random message to generate signature
./smartCard/private_key.pem - private key used to create signature for vm access 

sshC.py - code searches root directory for signature until it exists then calls ssh if it is valid

private_key.pem - code handles input from used on the card and creates and sends signature 

Qusai Elwazir WED AUG 20 2025
