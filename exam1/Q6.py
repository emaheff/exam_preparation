def secret(s1, s2, key):
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1) == 0 or len(s2) == 0:
        return False
    if ord(s1[0]) + key == ord(s2[0]):
        return secret(s1[1:], s2[1:], key+1)
    return False


