def commands(binary_str):
    command_list = ["Reverse the order of the operations in the secret handshake.", "jump", "close your eyes", "double blink", "wink"]
    actions = list()

    for n in range(len(binary_str) - 1, 0, -1):
        if binary_str[n] == "1":
            actions.append(command_list[n])
    if binary_str[0] == "1":
        actions.reverse()
    return actions
