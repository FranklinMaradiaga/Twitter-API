import unittest
from twitter import get_following_users, get_dict, create_database


class TestTwitter(unittest.TestCase):

    def test_get_following_users(self):
        ids = ['34719119', '1605', '18989355', '300878435', '541882699']

        names = ['Walter Isaacson', 'Sam Altman', 'Mike Solana',
                 'Dilbert', 'Andrea Stroppa']

        usernames = ['WalterIsaacson', 'sama', 'micsolana',
                     'Dilbert_Daily', 'Andst7']

        dict = {
            'ids': ids,
            'names': names,
            'usernames': usernames
        }

        self.assertEqual(get_following_users("44196397", 5), dict)


if __name__ == '__main__':
    unittest.main()
