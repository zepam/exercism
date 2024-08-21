import secrets

def private_key(p):
    # pick random number between 2 and p
    # starting with 1 will sometimes fail
    return secrets.choice(range(2, p))


def public_key(p, g, private):
    return pow(g, private, p)


def secret(p, public, private):
   return pow(public, private, p)
