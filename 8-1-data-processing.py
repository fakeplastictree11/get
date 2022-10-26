import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

settings = np.loadtxt('settings.txt', dtype=float)
frequency = settings[0]
voltage_step = settings[1]
data_array = np.loadtxt('data.txt', dtype=int) * voltage_step
time_array = np.arange(0, len(data_array) / frequency, 1 / frequency)

charge_time = data_array.argmax() / frequency
uncharge_time = (len(data_array) - data_array.argmax()) / frequency

fig, ax = plt.subplots(figsize=(15, 10), dpi=400)
ax.plot(time_array, data_array, color='midnightblue', marker='.', mec='b', mfc='b', linestyle='solid', linewidth=2, markersize=12, markevery=25, label='V(t)')
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепи', ha='center', fontsize=20, wrap=True)
ax.set_ylabel('V, В', fontsize=12)
ax.set_xlabel('t, с', fontsize=12)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.tick_params(which='major', width=1.0)
ax.tick_params(which='major', length=10)
ax.tick_params(which='minor', width=1.0)
ax.tick_params(which='minor', length=5)

ax.set_xlim(0, 90)
ax.set_ylim(0, 3.5)
ax.grid(which='major', color='0.75', linestyle='-', linewidth=1)
ax.grid(which='minor', color='0.5', linestyle='--', linewidth=0.5)
ax.text(60, 2, 'Время зарядки: {:.3f}'.format(charge_time), fontsize=15)
ax.text(60, 2.5, 'Время разрядки: {:.3f}'.format(uncharge_time), fontsize=15)
ax.legend(fontsize=15)

fig.savefig('test1.png')
fig.savefig('test2.svg')
plt.show()