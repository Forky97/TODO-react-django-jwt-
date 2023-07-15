class BaseValidator:

    def __init__(self,data):
        
        self.data = data
        self._errors = {}
        self.is_validate = True

    
    def is_valid(self):
        if self._errors:
            self.is_validate= False
        print(self._errors)

    


class RegisterValidator(BaseValidator):


    def __init__(self,data):
        super().__init__(data)




    def validate_password(self):
        self._errors['password'] = []

        password = self.data.get("password")
        repeat_password = self.data.get("repeat_password")

        if password != repeat_password : 
            self._errors['password'].append('password_not_match')

        if not self._errors['password']:
            del self._errors['password']




    def run_validate(self):

        self.validate_password()
        return self.is_valid()
