def is_palinddromes(string):
    return string[::-1]==string

def palindromes_sentences(sentences):
    string=""
    for char in sentences:
        if char.isalnum():
            string+=char
    print(string)
    return is_palinddromes(string)

ans=palindromes_sentences("the quick brown fox jumps over the lazy dog")
print(ans)