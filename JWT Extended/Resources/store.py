from Models.item_Model import ItemModel
from flask_restful import Resource
from Models.store_model import StoreModel
from flask_jwt_extended import jwt_required

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_by_item_name(name)
        if store:
            return store.json(),200
        
        return {"Message":"The store message is not found"},404

    def post(self,name):
        if StoreModel.find_by_item_name(name):
            return {"Message":"The store {} is already there".format(name)},400

        store=StoreModel(name)

        try:
            store.save_to_db()

        except:
            return {"Message":"An error occured while creating the store"},500

        return store.json()

    @jwt_required()
    def delete(self,name):
        store=StoreModel.find_by_item_name(name)
        if store:
            store.delete()
            return {"Message":"The store deleted successfully"}
        
        return {"Message":"The store is not exist"}
        



class StoreList(Resource):
    def get(self):
        return {'store':[store.json() for store in StoreModel.find_all()]}
