def is_pangram(sentence):
    input = sorted(set(sentence.lower())) #sorted is optional
    count = 0

    for ch in input:
        if ord(ch) in range(ord('a'),ord('z')+1):
            count+=1

    if count == 26:
        return True
    else:
        return False
