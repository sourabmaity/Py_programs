profit = [2,4,3,1,10]
dedline_ = [3,3,3,4,4]
total = [0 for i in range(max(dedline_))]
while total.count(0):
    m = profit.index(max(profit))
    d=dedline_[m]
    while d>0:
        if total[d-1]==0:
            total[d-1]=max(profit)
            break
        else:
            d-=1
    profit[m]=0
print(sum(total),total)
