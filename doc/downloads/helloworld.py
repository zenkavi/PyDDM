import matplotlib.pyplot as plt
import pyddm
m = pyddm.auto_model()
s = m.solve()
plt.plot(s.t_domain, s.pdf("correct"))
plt.savefig("helloworld.png")
plt.show()
