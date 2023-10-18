""" Test for Python Git API """
import unittest
import requests

class GitApiTests(unittest.testcase):
    """ Class for Git API Tests """
    def test_api(self):
        """ Definition for API test """
        varinputuserid="Dtharuni"
        rp = requests.get('https://api.github.com/users/'+varinputuserid, timeout=10)
        self.assertequal(rp.status_code,200)
        print("Test 1 Response Code: ",rp.status_code)
        repo = rp.json()
        #print(rp.json())
        self.assertequal(repo["login"],varinputuserid)
        print("test 2 Username: ",repo["login"])

    def test_repo(self):
        """ Definition for Repo test """
        varinputuserid = "Dtharuni"
        rp = requests.get('https://api.github.com/users/Dtharuni', timeout=10)
        print("UserID:",varinputuserid)
        print("Github Link:", rp)

    def test_invalid_user(self):
        """ Definiition for invilad user """
        varinputuserid = "NonExistentUser123"
        rp = requests.get('https://api.github.com/users/' + varinputuserid, timeout=10)
        self.assertequal(rp.status_code, 404)
        print("Test 2 Response Code (Invalid User): ", rp.status_code)

    def test_rate_limit(self):
        """ Definition for rate limit """
        rp = requests.get('https://api.github.com/rate_limit', timeout=10)
        self.assertequal(rp.status_code, 200)
        limit_data = rp.json()["resources"]["core"]
        remaining_limit = limit_data["remaining"]
        self.asserttrue(remaining_limit > 0, "API rate limit is not exhausted")

if __name__ == '__main__':
    #varinputuserid = "Dtharuni"
    unittest.main()
