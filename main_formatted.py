import os.path
from flask import Flask, request, render_template, redirect
import pandas as pd
df = pd.read_excel('output.xlsx')
print(df)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        df.loc[len(df.index)] = [name, age]
        with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, index=False)
    return render_template('home.html')

def sum(x, y):
    return x + y
print(sum(5, 6))

def subtract(x, y):
    return x - y
print(subtract(5, 7))

def multiply(x, y):
    return x * y
print(multiply(5, 6))
if __name__ == '__main__':
    app.run()