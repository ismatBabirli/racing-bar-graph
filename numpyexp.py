import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation

df = pd.read_csv('https://git.io/fjpo3', usecols=['name', 'group', 'year', 'value'])

colors = dict(zip(
    ['India','Europe','Asia','Latin America','Middle East','North America','Africa'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50']
))

group_lk = df.set_index('name')['group'].to_dict()

fig, ax = plt.subplots(figsize=(15, 8))

def racing_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200

    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        #print(value-dx,value+dx,i)
        ax.text(value-dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i, f'{value:,.0f}', size=14, ha='left',  va='center')
    
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Population (X thousand)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.10, 'The most populous cities in the world from 1500 to 2019',
            transform=ax.transAxes, size=20, weight=600, ha='left')
    ax.text(1, 0, 'by Developers Hub', transform=ax.transAxes, ha='right',
            color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)

animator = animation.FuncAnimation(fig, racing_barchart, frames=range(1500, 2019))
animator.save("Most populated cities.mp4")