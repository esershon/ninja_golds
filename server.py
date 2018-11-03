from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'emilys secret key dont tell anyone!'
import random

earnings={'farm':[10,20], 'house':[2,5], 'cave':[5,10], 'casino':[-50, 50]}

@app.route('/')
def ninjagold():
    if not 'wealth' in session:
        session['count']=0
        session['wealth']=0
        session['activities']=[]
        session['activities'].insert(0,"<p class='black'>Visit locations to earn golds!</p>")
    if session['count']>=10 or session['wealth']>149:
        winstatus=('WIN' if session['wealth']>149 else 'LOSE')
        session['winstatus']="<div><h1>YOU "+ winstatus + " THE GAME</h1><form action='/reset_game' method='post'><button type='submit'>Try Again!</button></form></div>"
        session['activities']=[]
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if session['count']<10:
        session['count']=session['count']+1
        money=random.randint(earnings[request.form['location']][0],earnings[request.form['location']][1])
        color=('green' if money>0 else 'red')
        session['wealth']=session['wealth']+money
        session['activities'].insert(0,"<p class="+ color +">You earned "+ str(money) + " golds from the " + str(request.form['location'])+"</p>")
    return redirect('/')

@app.route('/reset_game', methods=['POST'])
def restart_game():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)