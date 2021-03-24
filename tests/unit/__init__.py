import random
import string

test_first = 1
test_user_id = 99999
test_chat_id = 99999
test_message_id = 99999
test_value = 123456
test_name = 'test_name'
test_string = 'test'


class Random:
    random_string = ''.join([random.choice(string.ascii_lowercase) for i in range(20)])
