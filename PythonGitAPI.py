import requests

def GetApiRepofetch(varInputUserID):
    rp = requests.get('https://api.github.com/users/'+varInputUserID+'/repos', auth=('user', 'pass'))
    return rp

def GetRepoList(rp):
    repo = rp.json()
    repo_list =[]
    repo_list = [repos['name'] for repos in repo]
    return repo_list

def GetRepoCommitCnt(varInputUserID,RepoName):
    rc=requests.get('https://api.github.com/repos/'+varInputUserID+'/'+RepoName+'/commits', auth=('user', 'pass'))
    Commitlen=len(rc.json())
    return str(Commitlen)

def GetApi(varInputUserID):
    rp=GetApiRepofetch(varInputUserID)
    if(rp.status_code==200):
        repo_list=GetRepoList(rp)
        for Rn in repo_list:
            print('Repo Name :'+Rn+'\nNumber of Commits :'+GetRepoCommitCnt(varInputUserID,Rn))
    else:
        print("Error in the API, Try Again",rp.status_code)

#GetApi("Dtharuni")