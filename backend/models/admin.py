from backend.models.user import User
from backend.models.challenge import Challenge


class Admin(User):
    """Admin model that inherits from User model"""

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

    def __init__(self, *args, **kwargs):
        """Admin class constructor
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.role = 'admin'

    def add_challenge(self, ch):
        """ Add challenge to database """
        if isinstance(ch, Challenge):
            try:
                challenge = Challenge.query.filter_by(title=ch.title).first()
                if challenge:
                    print(f"Challenge {ch.title} already exists.")
                    return
                else:
                    self.challenges.append(ch)
                    self.save()
                    return True
            except Exception as e:
                print(f"Error adding challenge: {e.__cause__}")
        else:
            return False

    def edit_challenge(self, id, **kwargs):
        """ Edit challenge in database (placeholder) """
        if isinstance(id, int):
            challenge = Challenge.query.get(id)
            if kwargs:
                for k, v in kwargs.items():
                    if hasattr(challenge, k):
                        setattr(challenge, k, v)
                challenge.save()
                return True
        return False         
            
    def remove_challenge(self, challenge):
        """ Remove challenge from database (placeholder) """
        if isinstance(challenge, Challenge):
            self.challenges.remove(challenge)
            self.save()
            return True
        return False
    
    def suspend_account(self, userid):
        """ Suspend user account """
        User.query.get(userid).active = False
        User.save()
