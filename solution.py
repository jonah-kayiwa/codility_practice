def solution(A, D):
    monthly_fee = 5
    balance = 0
    cards = {}

#lets use the ZIP to loop through 
    for i, date in zip(A, D):
        month = int(date.split('-') [1])
        if i >= 0:
            balance += i

#change the negative balance            
        else:
            balance += i
        if month in cards:
            cards[month].append(i)
        else:
            cards[month] = [i]

#create a loop through the months
for month in range(1, 13):
    if month in cards  and len(cards[month]) >= 3 and sum (cards[nonth]) >= -100: 
        balance += monthly_fees *(len(cards[month]) - 3)
    else:
        balance -= monthly_fees                         

#run some tests to see if code runs
