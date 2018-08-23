from faker import Faker
import os
import random
import shutil

# empty test folders and input files
shutil.rmtree("test/")
open("test_input_file.txt", "w").close()

# initilize faker instance
fake = Faker()

# write random files
for i in range(50):
    prefix = fake.company()

    # seed 20% of data to test_input_file
    if random.randint(0, 100) < 20:
        f = open("test_input_file.txt", "a")
        f.write("%s\n" % prefix)

    # seed fake parent folders
    os.makedirs(os.path.dirname("test/%s/" % prefix))

    # seed fake child folders
    for i in range(random.randint(10,30)):
        date = fake.date_between("-2yr", "now")
        open("test/%s/%s_%s.gpg" % (prefix, prefix, date), "w")

f.close()
