import matplotlib.pyplot as plt

eGuess = []
numRuns = int(input('Number of runs to do: '))
for i in range(1,numRuns):
    eGuess.append((1+i**-1)**i)
plt.plot(eGuess)
plt.ylabel('e guess')
plt.xlabel('num guesses')
plt.show()
e = (1+numRuns**-1)**numRuns
print('e =', e)