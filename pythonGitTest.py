import unittest
import requests
from PythonGitAPI import GetApi 


class GitApi_Tests(unittest.TestCase):
    
    def test_api(self):
        varInputUserID="Dtharuni"
        rp = requests.get('https://api.github.com/users/'+varInputUserID)
        self.assertEqual(rp.status_code,200)
        print("Test 1 Response Code: ",rp.status_code)
    
        repo = rp.json()
        #print(rp.json())
        self.assertEqual(repo["login"],varInputUserID)
        print("test 2 Username: ",repo["login"])
    def test_repo(self):
        varInputUserID="Dtharuni"
        rp = requests.get('https://api.github.com/users/Dtharuni')

    def test_invalid_user(self):
        varInputUserID = "NonExistentUser123"
        rp = requests.get('https://api.github.com/users/' + varInputUserID)
        self.assertEqual(rp.status_code, 404)
        print("Test 2 Response Code (Invalid User): ", rp.status_code)

    def test_rate_limit(self):
        rp = requests.get('https://api.github.com/rate_limit')
        self.assertEqual(rp.status_code, 200)
        limit_data = rp.json()["resources"]["core"]
        remaining_limit = limit_data["remaining"]
        self.assertTrue(remaining_limit > 0, "API rate limit is not exhausted")

  
if __name__ == '__main__':
    #varInputUserID = "Dtharuni"
    unittest.main()