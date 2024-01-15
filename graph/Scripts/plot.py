import matplotlib.pyplot as plt

fig, ax = plt.subplots()

path = '/home/rumin/Documents/Code/Web/graph/War/numbers.txt'
file = open(path,'r')
num = file.read().splitlines()
a = num[0]
b = num[1]
c = num[2]
file.close()


fruits = ['apple', 'blueberry', 'cherry']
counts = [a, b, c]
bar_labels = ['red', 'blue', '_red']
bar_colors = ['tab:red', 'tab:blue', 'tab:red']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

# Сохранение графика с указанием пути
plt.savefig('/home/rumin/Documents/Code/Web/graph/static/main/img/plot.png')

