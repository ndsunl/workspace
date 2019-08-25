def print_msg():
    msg = "I'm closure"

    def printer():
        print(msg)

    return printer

closure = print_msg()
closure()