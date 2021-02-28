def solution(answers):
	a_count = b_count = c_count=0
	for i in range(0,len(answers)):
		if (i%5)+1 == answers[i]:
				a_count+=1
				print("a 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(a_count, i%5+1, answers[i]))
		if (i%2)==0:
			if (answers[i]==2):
				b_count += 1
				print("b 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(b_count, i%2, answers[i]))
		else:
			if (i%8)==1 and answers[i] == 1:
				b_count += 1
				print("b 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(b_count, i%8, answers[i]))
			elif (i % 8) == 3 and answers[i] == 3:
				b_count += 1
				print("b 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(b_count, i%8, answers[i]))
			elif (i % 8) == 5 and answers[i] == 4:
				b_count += 1
				print("b 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(b_count, i%8, answers[i]))
			elif (i % 8) == 7 and answers[i] == 5:
				b_count += 1
				print("b 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(b_count, i%8, answers[i]))
		if (i%10)==0 or (i%10)==1:
			if answers[i] == 3:
				c_count += 1
				print("c 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(c_count, i%10, answers[i]))
		elif (i%10)==2 or (i%10)==3:
			if answers[i] == 1:
				c_count += 1
				print("c 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(c_count, i%10, answers[i]))
		elif (i%10)==4 or (i%10)==5:
			if answers[i] == 2:
				c_count += 1
				print("c 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(c_count, i%10, answers[i]))
		elif (i%10)==6 or (i%10)==7:
			if answers[i] == 4:
				c_count += 1
				print("c 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(c_count, i%10, answers[i]))
		elif (i%10)==8 or (i%10)==9:
			if answers[i] == 5:
				c_count += 1
				print("c 값: {} // 현재 i값 : {} 현재 answer값 : {}".format(c_count, i%10, answers[i]))
                
	print(a_count, b_count, c_count)

	num = max(a_count, b_count, c_count)

	answer = []
	if a_count == num:
		answer.append(1)
	if b_count == num:
		answer.append(2)
	if c_count == num:
		answer.append(3)
	return answer
	
answers = [2,4,3,5,1
		,1,2,4,3,5,
		5,1,1,2,5,
		4,3,2,1]
a = solution(answers)
print(a)
