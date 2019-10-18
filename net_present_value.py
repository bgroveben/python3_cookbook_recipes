import matplotlib.pyplot as plt

# Update Project A Cash Flows Here
project_a = [-1000000, 0, 0, 50000, 50000, 200000, 250000, 250000, 250000, 250000, 375000, 375000, 375000, 375000, 375000, 250000, 250000, 250000, 250000, 100000]

# Update Project B Cash Flows Here
project_b = [-1000000, 50000, 50000, 50000, 50000, 250000, 500000, 500000, 500000, 500000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]

discount_rate = [0.05, 0.055, 0.06, 0.065, 0.07, 0.075, 0.08, 0.085, 0.09, 0.095, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18]

def calculate_npv(rate, cash_flow):
    npv = 0
    for t in range(len(cash_flow)):
        npv += cash_flow[t]/(1+rate)**t
    return npv

npvs_a = list()
npvs_b = list()
for rate in discount_rate:
    npv_a = calculate_npv(rate, project_a)
    npvs_a.append(npv_a)
    npv_b = calculate_npv(rate, project_b)
    npvs_b.append(npv_b)

plt.plot(discount_rate,npvs_a,linewidth=2.0,color='red',label='Project A')
plt.plot(discount_rate,npvs_b,linewidth=2.0,color='blue',label='Project B')
plt.axhline(y=0,linewidth=0.5,color='black')
plt.title('NPV Profile for Projects A and B')
plt.xlabel('Discount Rate')
plt.ylabel('Net Present Value')
plt.legend()
plt.show()
