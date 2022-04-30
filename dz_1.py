"есть article.txt файл найти cамое длинное слово в файле"

def longest_word(file):
    try: 
        with open("article.txt", 'r',encoding="utf_8") as file:
            words = file.read().split()
            max_len = len(max(words, key=len))
            print(f"В самом длинном слове {max_len} букв")
            return (f"Самое длинное слово в файле {[word for word in words if len(word) == max_len]}")
    except Exception:
        print ("Произошла ошибка, проверьте код")
print(longest_word(""))
