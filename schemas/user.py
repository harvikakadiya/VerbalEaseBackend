def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "firstName":str(item["firstName"]),
        "lastName":str(item["lastName"]),
        "email":str(item["email"]),
        "birthDate":str(item["birthDate"]),
        "password":str(item["password"]),
    }
    
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]