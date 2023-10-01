class User:
    def __init__(user_instance, new_username):
        user_instance._username = new_username
    
    def get_username(user_instance):
        return user_instance._username
    
    def set_username(user_instance, new_username):
        user_instance._username = new_username
        
    
user = User.__new___(User)
User.__init__(user,"myusername")
