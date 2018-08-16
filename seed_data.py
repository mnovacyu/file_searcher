from faker import Faker
import os
import random


# initilize faker instance
fake = Faker()

# write random files
for i in range(50):
    prefix = fake.company()
    folder = fake.iban()

    os.makedirs(os.path.dirname("test/%s/" % folder))
        
    for i in range(random.randint(10,30)):
        date = fake.date_between("-2yr", "now")
        open("test/%s/%s_%s.gpg" % (folder, prefix, date), "w")