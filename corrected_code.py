

@app.route('/', methods=['GET', 'POST'])
def form():
    if (request.method == 'POST'):
        name = request.form['name']
        age = int(request.form['age'])
        if (age<0 or age>110):
            return redirect('/')
        else:
            df.loc[len(df.index)] = [name, age]
            with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, index=False)
    return render_template('home.html')
