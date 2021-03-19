# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-

def solution(cards):
  def draw(num):
    if num >= len(cards): return -1
    if cards[num] > 10: return 10
    return cards[num]

  def is_black_jack(arr):
    if len(arr) == 2 and 1 in arr and 10 in arr: return True
    return False
  
  def is_win(p, d):
    if p>d: return True
    elif p<d: return False
    else: return 0

  money = 0
  
  card_count = 0
  game_over = False
  while not game_over:
    player =[]
    dealer = []
    player.append(draw(card_count)); card_count +=1
    dealer.append(draw(card_count)); card_count +=1 # 딜러의 첫번째 카드가 뒤집힌 카드
    player.append(draw(card_count)); card_count +=1
    dealer.append(draw(card_count)); card_count +=1
    if -1 in player or -1 in dealer: break
    if is_black_jack(player):
      if sum(dealer) == 21: continue
      elif is_win(21, sum(dealer)): money += 3
      else: money -= 2
    if dealer[1] == 1 or dealer[1] >= 7:
      while sum(player) < 17:
        card = draw(card_count); card_count += 1
        if card == 1 and 17<= sum(player)+11 <= 21: card = 11
        player.append(card)
        if card == -1: game_over = True; break
      if sum(player) > 21: money -= 2
    elif dealer[1] == (2 or 3):
      while sum(player) < 12:
        card = draw(card_count); card_count += 1
        if card == 1 and 12<= sum(player)+11 <= 21: card = 11
        player.append(card)
        if card == -1: game_over = True; break
    elif dealer[1] == (4 or 5 or 6):
      if is_black_jack(dealer):
        if sum(player) == 21: continue
        else: money -= 2
      while sum(dealer) < 17:
        card = draw(card_count); card_count += 1
        if card == 1 and 17<= sum(dealer)+11 <= 21: card = 11
        dealer.append(card)
        if card == -1: game_over = True; break
      if sum(dealer) > 21: money += 2
    if is_black_jack(dealer):
      if sum(player) == 21: continue
      else: money -= 2
    while sum(dealer) < 17:
      card = draw(card_count); card_count += 1
      if card == 1 and 17<= sum(dealer)+11 <= 21: card = 11
      dealer.append(card)
      if card == -1: game_over = True; break
    if sum(dealer) > 21: money += 2
    if sum(player) == sum(dealer): continue
    elif is_win(sum(player), sum(dealer)): money += 2
    else: money -= 2

  return money

cards = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print(solution(cards))

# 20:20분 시작
# 21:14분 완료
# 55분 소요