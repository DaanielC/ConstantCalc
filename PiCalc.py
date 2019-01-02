import random
import matplotlib.pyplot as plt

inCirc = 0
outCirc = 0
piGuess = []

numRuns = int(input('Number of runs to do: '))
for i in range(numRuns):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x ** 2 + y ** 2)  <= 1:
        inCirc += 1
    else:
        outCirc += 1
    piGuess.append((4 * inCirc) / (inCirc + outCirc))
plt.plot(piGuess)
plt.ylabel('pi guess')
plt.xlabel('num guesses')
plt.show()
pi = (4 * inCirc) / (inCirc + outCirc)
print('π =', pi)