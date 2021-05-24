from flask import Flask,jsonify,request
app=Flask(__name__)

#POST is used to receive the data from web server prospective 
#GET is used to send data back
stores=[
    
    {
        'name': 'My wonderful store',
            'items':[
                        {
                            'name':'My Items',
                            'price': 15.99
                        }
                    ]
    }
]



#POST    /store data: {name:}    ----- create a new store with given name{name:}

@app.route('/store',methods=['POST']) #by default POST act as a GET request
def create_store():
    request_data=request.get_json()

    for i in range(len(stores)):
        if request_data["name"] in stores[i]['name']:
            new_store={
                "name":request_data["name"],
                "items":request_data["items"]
            }
            stores[i]=new_store

        else:
            new_store={
                "name":request_data["name"],
                "items":request_data["items"]
            }
            stores.append(new_store)
    return jsonify(new_store)


#GET     /store/<string:name>    ----- Get a store for given name, its going to return some data about it.

@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
    #if the store name matches return it
    #if the none match, return the error message

#GET     /store                  ----- Return list of all the stores.

@app.route('/store/')
def get_stores():
    return jsonify({'stores':stores})

#POST    /store/<string:name>/item {name:,price}        -------- create an item inside the specific store for the given name.

@app.route('/store/<string:name>/item',methods=['POST']) #by default POST act as a GET request
def create_store_item(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item={
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(stores)
        
    return jsonify({'message':'store not found'})

#GET     /store/<string:name>/item                      -------- return all the items of specific store

@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
        
    return jsonify({'messege':'store not found'})



app.run(port=5000)