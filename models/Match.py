class Match():
    def __init__(self, competitors, start_date, end_date="", tournament_id="", game_type=""):
        self.competitors = competitors
        self.start_date = start_date
        self.end_date = end_date
        if not tournament_id == "":
            self.tournament_id = tournament_id