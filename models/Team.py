class Team():
    def __init__(self, members, team_name=""):
        self.members = members
        if  team_name == "":
            self._key = ("".join(members)).replace(" ","")
        else:
            self.team_name = team_name 
            self._key = team_name.replace(" ","")  

