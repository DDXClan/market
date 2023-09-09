import bcrypt


async def hashed_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


async def verify_password(password, hash_password):
    return bcrypt.checkpw(password.encode('utf-8'), hash_password.encode('utf-8'))

