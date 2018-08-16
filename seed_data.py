from faker import Faker
import random

# initilize faker instance
fake = Faker()

# write random files
for i in range(50):

    prefix = fake.company()
    
    for i in range(random.randint(5,20)):
        date = fake.date_between('-2yr', 'now')
        open("test/%s_%s.gpg" % (prefix, date), 'w')