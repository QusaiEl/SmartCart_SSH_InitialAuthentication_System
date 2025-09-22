import argparse
import subprocess
import os
import time

sshPath = "ssh -p 8022 -i PATHs/id_rsa server1@127.0.0.1"
pubKey = "./public_key.pem"



def permission_check_hold():
    searchCounter = 0 
    while True:
        try:
            permission = subprocess.run(["openssl", "dgst", "-sha256", "-verify", "public_key.pem", "-signature", "sig.bin", "sig"], capture_output=True, text=True, check=True)
            if permission.stdout == "Verified OK\n":
                os.remove("sig")
                os.remove("sig.bin")
                return True 
            elif permission.stdout == "Verification Failure\n":
                return False 

        except subprocess.CalledProcessError as e:
            print(e.returncode)
            if not os.path.exists("sig.bin") or not os.path.exists("sig"):
                print(f"Attempt: {searchCounter}: Key not found please enter passcode on your smart card or enter ^Z to end the process.")
                searchCounter += 1
                time.sleep(2)
                continue
            else:
                return False
               
        
def main():
    
    parser = argparse.ArgumentParser(description="SSHC is for secure authentication when wanting to ssh into a machine with sensitive permissions or data")
    parser.add_argument("userID", help="User ID of party attempting secure shell login.")
    parser.add_argument("-secure", "-s", action="store_true", help="Secure mode.")
    args = parser.parse_args()

    if not permission_check_hold(): ## permission holding check
        print("Invalid Signature: Access Denied")
        return

    try:
        subprocess.run(["sshpass", "-p", "1234", "ssh", "-p", "8022", f"{args.userID}@127.0.0.1"]) ## login to ssh
    except subprocess.CalledProcessError as E:
        print({E.stdeerr})

if __name__ == "__main__":
    main()