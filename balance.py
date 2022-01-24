from instapy import InstaPy
from instapy import smart_run

print("what's your name ?")
name = str(input())
print("Say me you fuck password :)")
pwd = str(input())
session = InstaPy(username=name, password=pwd)
session.login()

with smart_run(session):
    """ Activity unfollow who dont follow me back"""
    
    ariclinis_followers = session.grab_followers(username=name, amount="full", live_match=True, store_locally=True)
    ariclinis_following = session.grab_following(username=name, amount="full", live_match=True, store_locally=True)

    print("IMBECIS")
    imbecis = list(set(ariclinis_following)-set(ariclinis_followers))
    
    session.unfollow_users(amount=len(imbecis), custom_list_enabled=True, custom_list=imbecis, custom_list_param="nonfollowers", style="RANDOM", unfollow_after=0, sleep_delay=1)
