def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        j=i+1
        while j<len(phone_book):
            if phone_book[j].startswith(phone_book[i]):
                return False
            j += 1
            
            
    return answer