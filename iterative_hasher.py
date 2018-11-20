#written by Yohann Abittan
#this program uses hashlib to either produce hashes which have been hashed iteratively a given number of times
#or to test wether a given hash matches a password after a number of iterations of hashing

import hashlib

def encryptMd5(initial):
    encrypted = hashlib.md5()
    encrypted.update(initial)
    return encrypted.hexdigest()

def encryptSha1(initial):
    encrypted = hashlib.sha1()
    encrypted.update(initial)
    return encrypted.hexdigest()

def encryptSha224(initial):
    encrypted = hashlib.sha224()
    encrypted.update(initial)
    return encrypted.hexdigest()

def encryptSha256(initial):
    encrypted = hashlib.sha256()
    encrypted.update(initial)
    return encrypted.hexdigest()

def encryptSha384(initial):
    encrypted = hashlib.sha384()
    encrypted.update(initial)
    return encrypted.hexdigest()

def encryptSha512(initial):
    encrypted = hashlib.sha224()
    encrypted.update(initial)
    return encrypted.hexdigest()


def main():
    counter = 0
    passwordFound = 0

    print("\n \nWelcome to iterative hasher \n")
    print("Would you like to generate a hash? (1) \n")
    mode = raw_input("Or would you like to iteratively hash an input and test if it matches a target? (2) \n")
    print("Which algorithm would you like to use? \n")
    algo = raw_input("1 = md5, 2 = sha1, 3 = sha224, 4 = sha384, 5 = sha512 \n")

    password = raw_input("What is your password\n")

    if mode == "2":
        target = raw_input("What is your target hash?\n")
    
    iterations = int(raw_input("How many times would you like to hash the input? \n"))
    
    while counter!=iterations:
        if algo == "1" or algo == "md5":
            password = encryptMd5(password)
        elif algo == "2" or algo == "sha1":
            password = encryptSha1(password)
        elif algo == "3" or algo == "sha224":
            password = encryptSha224(password)
        elif algo == "4" or algo == "sha384":
            password = encryptSha384(password)
        elif algo == "5" or algo == "sha512":
            password = encryptSha512(password)

        if mode == 2:
            if password == target:
                print("Got it ! number of iterations =%s"%counter)
                passwordFound = 1
                break

        step = int(iterations/10)
        
        if counter%step==0:
            print("hashing no:%s"%counter)
            print password
            
        counter+=1
    if mode == "2":
        if passwordFound !=1:    
            print ("target not found :(")
    elif mode == "1":
        print("\n \nAfter %s iterations your final hash is = "%iterations + password)
        
if __name__ == "__main__":
    main()
