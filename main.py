from rsa import Rsa


def print_menu():
    menu_rsa = {
        1: "G - g : Generate Keys",
        2: "E - e : Encrypt",
        3: "D - d : Decrypt",
        4: "Q - q : Quite",
    }
    print("\t\t--------- RSA ALGORITHM ---------")
    for key in menu_rsa:
        print("\t \t \t", menu_rsa[key])
    print("\t\t---------------------------------")

def print_all_algorithm():
    menu = {
        1: "1 - RSA",
        2: "2 - EL-GAMAL",
        3: "3 - MERKLE HElLMAN -knapsack-",
        4: "4 - QUITE",
    }
    for key in menu:
        print("\t \t \t", menu[key])

if __name__ == '__main__':


    print_all_algorithm()
    option = input("Enter your choice : ")

    if int(option) == 1:

        MIN_, MAX_ = 1400, 10000
        rsa = Rsa(start=MIN_, end=MAX_, file_name="algo_rsa")

        while True:
            print_menu()
            option = input("Enter your choice : ")

            if option == "g" or option == "G":
                #Generate keys
                rsa.generate_keys()

            elif option == "e" or option == "E":
                # Encrypt
                try:
                    message = input("please type a message format integer : ")
                    cipher_text = rsa.encrypt(message)
                except:
                    print("An Error is Accrued, please make sure the message is an integer")



            elif option == "d" or option == "D":
                # Decrypt
                try:
                    cipher_text = input("please type a cipher text : ")
                    rsa.decrypt(cipher_text)
                except:
                    print("An Error is Accrued, please make sure the cipher text is an integer")

            else:
                exit()
