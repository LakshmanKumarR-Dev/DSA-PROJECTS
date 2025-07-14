import re

def process(txt):
    txt = txt.lower()
    txt = re.sub(r'[^a-z0-9\s]', '', txt)
    word = txt.split()
    return word

def ngrams(text, n):
    return [' '.join(text[i:i+n]) for i in range(len(text)-n+1)]

def kmp(pat, txt):
    def lps(pat):
        pi_table = [0] * len(pat)
        length = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                pi_table[i] = length
                i += 1
            else:
                if length != 0:
                    length = pi_table[length - 1]
                else:
                    pi_table[i] = 0
                    i += 1
        return pi_table

    pi_table = lps(pat)
    i, j = 0, 0
    count = 0
    while i < len(txt):
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == len(pat):
            count += 1
            j = pi_table[j - 1]
        elif i < len(txt) and pat[j] != txt[i]:
            if j != 0:
                j = pi_table[j - 1]
            else:
                i += 1
    return count

def jaccard(exp1, exp2):
    intsec = set(exp1) & set(exp2)
    uni = set(exp1) | set(exp2)
    if not uni:
        return 0
    return len(intsec) / len(uni)

def compare(txt1, txt2):
    doc1 = process(txt1)
    doc2 = process(txt2)

    ngram1 = ngrams(doc1, 3)
    ngram2 = ngrams(doc2, 3)

    similarity = jaccard(ngram1, ngram2)

    sentence = " ".join(doc1)
    kmps = 0
    for phrase in ngram2:
        kmps += kmp(phrase, sentence)

    return similarity, kmps

def main():
    print("Enter first sentence: ")
    text1 = input(">> ")

    print("Enter second sentence: ")
    text2 = input(">> ")

    similarity, kmp_score = compare(text1, text2)
    print(f"Similarity using Jaccard: {similarity * 100:.2f}%")
    print(f"KMP Score: {kmp_score}")

    if similarity > 0.5 or kmp_score > 10:
        print("High Chance of Plagiarism")
    elif similarity > 0.3:
        print("Moderate Similarity")
    else:
        print("Documents are original") 

if __name__ == "__main__":
    main()
