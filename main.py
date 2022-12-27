from flask import Flask, request, render_template, redirect
app = Flask(__name__)


def fib(n):
    if n<=0:
        pass
    elif n == 1:
        yield 0
    else:
        prev,cur = 0,1
        yield prev
        for i in range(n-1):
            yield cur
            prev,cur=cur,prev+cur

@app.route('/first')
def fib_1():
    # http://127.0.0.1:5000/first
    n = 9
    return f'<h1>{n} первых чисел Фибоначчи: {str(list(fib(n)))[1:-1]}<h1>'

@app.route('/second')
def fib_2():
    # http://127.0.0.1:5000/second?count=14
    n = int(request.args.get('count'))
    return f'<h1>{n} первых чисел Фибоначчи: {str(list(fib(n)))[1:-1]}<h1>'

if __name__ == '__main__':
    app.run()

