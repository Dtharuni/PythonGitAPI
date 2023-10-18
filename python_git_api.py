""" Python Git API """
import requests

def getapirepofetch(varinputuserid):
    """ Definition for fetching repo """
    rp = requests.get('https://api.github.com/users/'+varinputuserid+\
         '/repos', auth=('user', 'pass'), timeout=10)
    return rp

def getrepolist(rp):
    """ Definition for listing repo """
    repo = rp.json()
    repo_list =[]
    repo_list = [repos['name'] for repos in repo]
    return repo_list

def getrepocommitcnt(varinputuserid,reponame):
    """ Definition for commit repo"""
    rc=requests.get('https://api.github.com/repos/'+varinputuserid+'/'+reponame+\
         '/commits', auth=('user', 'pass'), timeout=10)
    commitlen=len(rc.json())
    return str(commitlen)

def getapi(varinputuserid):
    """ Definition for fetching user ID """
    rp=getapirepofetch(varinputuserid)
    if rp.status_code==200:
        repo_list=getrepolist(rp)
        for rn in repo_list:
            print('Repo Name :'+rn+'\nNumber of Commits :'+getrepocommitcnt(varinputuserid,rn))
        print("Error in the API, Try Again",rp.status_code)

#getapi("Dtharuni")
