from abc import ABC, abstractmethod

class Sports(ABC):
    @abstractmethod
    def practice_session(self):
        pass

    @abstractmethod
    def host_match(self):
        pass

    @abstractmethod
    def award_ceremony(self):
        pass



class CollegeBasketball(Sports):
    def practice_session(self):
        print("Basketball practice session held in College A gym.")

    def host_match(self):
        print("College A hosting inter-college basketball match.")

    def award_ceremony(self):
        print("College A awards ceremony for basketball players.")

class CollegeFootball(Sports):
    def practice_session(self):
        print("Football practice session held in College B field.")

    def host_match(self):
        print("College B hosting inter-college football match.")

    def award_ceremony(self):
        print("College B awards ceremony for football players.")

class CollegeSwimming(Sports):
    def practice_session(self):
        print("Swimming practice session held at College C pool.")

    def host_match(self):
        print("College C hosting inter-college swimming competition.")

    def award_ceremony(self):
        print("College C awards ceremony for swimmers.")


def organize_sport_event(sport: Sports):
    sport.practice_session()
    sport.host_match()
    sport.award_ceremony()


organize_sport_event(CollegeBasketball())
organize_sport_event(CollegeFootball())
organize_sport_event(CollegeSwimming())
