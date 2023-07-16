import jwt


class Utils:



    @staticmethod
    def get_user_from_token(data):

        auth_header = data.headers.get('Authorization')

        auth_token = auth_header.split(' ')[1]

        payload = jwt.decode(auth_token, algorithms=['RS256'], options={"verify_signature": False})
        user_username = payload['user']


        return user_username