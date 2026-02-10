
class InstagramAccount:
 
    def __init__(self, account_name, password):
        self.account_name = account_name              
        self._private_reels = []                      
        self.__archived_reels = []                    
        self.__password = password                    
   
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"{reel_name} added to private reels.")


    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"{reel_name} added to archived reels.")


    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")


    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"


    
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password!")



account = InstagramAccount("iamnisarga_official", 43211234)

account.add_private_reel("Trip_reel")
account.add_private_reel("Dance_Reel")

account.display_private_reels(True)
account.display_private_reels(False)

account.add_archived_reel("Old_Memories")

account.display_archived_reels(43211234)
print(account.get_archived_reels(43211234))

