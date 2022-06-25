import random
def random_passwd(n):
        '''this function creates random password  from 33 to 126 ASCII'''
        passwd = ' '
        i = 0 
        while i < n:
              passwd =  passwd + chr(random.randint(33, 126))
              i += 1 
        return passwd

print(random_passwd(8))
