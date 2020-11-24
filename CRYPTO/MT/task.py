import random
flag = "HECTF{" + ''.join(hex(random.getrandbits(32))[2:]
                          for _ in range(4)) + "}"
with open('secret.txt', 'w') as f:
    for i in range(1500):
        f.write(str(random.getrandbits(32)) + "\n")

out = [random.getrandbits(32) for _ in range(624)]
xor_out = [out[i] ^ out[i + 1] for i in range(623)] + [out[623]]

with open('output.txt', 'w') as f:
    for i in range(624):
        f.write(str(xor_out[i]) + "\n")