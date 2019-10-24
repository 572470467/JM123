from flask import Flask, jsonify
import time
import random
app = Flask(__name__)
list=[{'pos':0,'sensors':[0,1,1,1,1]},{'pos':1,'sensors':[1,0,1,1,1]},{'pos':2,'sensors':[1,1,0,1,1]},{'pos':3,'sensors':[1,1,1,0,1]},{'pos':4,'sensors':[1,1,1,1,0]}]
list0=['motor0','motor1','motor2','motor3','sensor0','sensor1','sensor2','sensor3']
list1=['motor4','motor5','motor6','sensor4','sensor5','sensor6','sensor7']
releasestart = {'a':0, 'b':0}
releaseend = {'a':0, 'b':0}
releaseactive = {'a': False, 'b': False}

def random_status(cnt):
    dic = {}
    for i in range(cnt):
        dic[str(i)] = str(random.randrange(2)) + str(random.randrange(2))
    return dic

def random_carrier():
    dic = {}
    for i in range(2):
        dic[str(i)] = str(random.randrange(5))
    return dic[str(i)]

def random_s():
    dic = {}
    for i in range(8):
        dic[str(list0[i])] = str(random.randrange(2))
    return dic

def random_n():
    dic = {}
    for i in range(7):
        dic[str(list1[i])] = str(random.randrange(2))
    return dic

@app.route('/s/status/')
def status_s():
    d=random_s()
    return jsonify(d)

@app.route('/n/status/')
def status_n():
    d=random_n()
    return jsonify(d)

@app.route('/carrier/status')
def carrier():
    d=list[int(random_carrier())]
    return jsonify(d)

@app.route('/carrier/moveto/<groupid>')
def moveto(groupid):
    d=groupid
    return jsonify(d)

@app.route('/bucketgroup/a')
def group_a():
    d = random_status(5)
    return jsonify(d)

@app.route('/bucketgroup/b')
def group_b():
    d = random_status(4)
    return jsonify(d)

@app.route('/feederon/<groupid>')
def feeder(groupid):
    if groupid in releasestart.keys():
        releasestart[groupid] = releaseend[groupid] = time.time()
        releaseactive[groupid] = True
        d = {'status': 'OK'}
    else:
       d = {'status': 'Error'}
    return jsonify(d)

@app.route('/feederoff/<groupid>')
def feeder_stop(groupid):
    if groupid in releasestart.keys():
        releaseend[groupid] = time.time()
        releaseactive[groupid] = False
        d = {'status': 'OK'}
    else:
        d = {'status': 'Error'}
    return jsonify(d)

@app.route('/scale/<groupid>')
def scale_read(groupid):
    if groupid in releasestart.keys():
        if releaseactive[groupid]:
            amt = time.time() - releasestart[groupid]
            print(time.time()-releasestart[groupid])
        else:
            amt = releaseend[groupid] - releasestart[groupid]
            print(releasestart[groupid])
        d = {'status': 'OK', 'reading': amt, 'started':releasestart[groupid]}
    else:
        d = {'status': 'Error', 'reading': -1, 'started': -1}
    return jsonify(d)

if __name__ == '__main__':
    app.run(port=5000)

