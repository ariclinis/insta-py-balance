from instapy import InstaPy

print("what's your user name ?")
name = str(input())
print("Say me you fuck password :)")
pwd = str(input())
session = InstaPy(username=name, password=pwd)
session.login()

""" Activity unfollow who dont follow me back"""

ariclinis_followers = session.grab_followers(username=name, amount="full", live_match=True, store_locally=True)
ariclinis_following = session.grab_following(username=name, amount="full", live_match=True, store_locally=True)

print("IMBECIS")
imbecis = list(set(ariclinis_following)-set(ariclinis_followers))
nImbecis = len(imbecis)
print("Do you have "+str(nImbecis)+" that dont follow You back")
print("How many of them do you want unfollow ? :)")
n = 5
session.unfollow_users(amount=n, custom_list_enabled=True, custom_list=imbecis, custom_list_param="nonfollowers", style="RANDOM", unfollow_after=0, sleep_delay=1)
