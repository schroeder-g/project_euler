def self_powers():
    return str(sum([n**n for n in range(1, 1000)]))[-10:]
