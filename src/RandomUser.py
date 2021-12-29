import requests

class RandomUser:
    def __init__(self, seed=None):
        try:
            if seed is None:
                url= 'https://randomuser.me/api/'
            elif not seed and type(seed) is not str:
                raise Exception
            else:
                url= 'https://randomuser.me/api/?seed=' + seed
            self.randomUser = requests.get(url).json()
            if self is None:
                raise Exception
        except:
            raise ValueError("Something went wrong")

    def get_info(self):
        return self.randomUser["info"]

    def get_user(self):
        return self.randomUser["results"][0]

    def get_gender(self):
        return self.randomUser["results"][0]["gender"]

    def get_name(self):
        return self.randomUser["results"][0]["name"]

    def get_title(self):
        return self.randomUser["results"][0]["name"]["title"]

    def get_first_name(self):
        return self.randomUser["results"][0]["name"]["first"]

    def get_last_name(self):
        return self.randomUser["results"][0]["name"]["last"]    

    def get_location(self):
        return self.randomUser["results"][0]["location"]

    def get_street(self):
        return self.randomUser["results"][0]["location"]["street"]

    def get_city(self):
        return self.randomUser["results"][0]["location"]["city"]

    def get_state(self):
        return self.randomUser["results"][0]["location"]["state"]

    def get_country(self):
        return self.randomUser["results"][0]["location"]["country"]

    def get_postcode(self):
        return self.randomUser["results"][0]["location"]["postcode"]

    def get_coordinates(self):
        return self.randomUser["results"][0]["location"]["coordinates"]

    def get_timezone(self):
        return self.randomUser["results"][0]["location"]["timezone"]

    def get_email(self):
        return self.randomUser["results"][0]["email"]

    def get_login(self):
        return self.randomUser["results"][0]["login"]

    def get_uuid(self):
        return self.randomUser["results"][0]["login"]["uuid"]

    def get_username(self):
        return self.randomUser["results"][0]["login"]["username"]

    def get_password(self):
        return self.randomUser["results"][0]["login"]["password"]

    def get_dob(self):
        return self.randomUser["results"][0]["dob"]

    def get_registered(self):
        return self.randomUser["results"][0]["registered"]

    def get_phone(self):
        return self.randomUser["results"][0]["phone"]

    def get_cell(self):
        return self.randomUser["results"][0]["cell"]

    def get_id(self):
        return self.randomUser["results"][0]["id"]

    def get_picture(self):
        return self.randomUser["results"][0]["picture"]

    def get_nat(self):
        return self.randomUser["results"][0]["nat"]

