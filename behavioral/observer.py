'''
In this module, we show a simple example of the Observer Design Pattern.

The Observer Design Pattern lets one object (the Subject) notify many other objects
(Observers) when something changes. This example uses a Channel as the Subject
and User as the Observer.

Notes:
- Channel keeps a list of followers (observers).
- When Channel.send_message is called, every follower receives the update
  through their channel_updated method.
- This is a local and simple implementation. For production code you may want
  thread-safety, weak references, error isolation, logging, and unsubscribe support.

You can read more about this Design Pattern here:
https://www.geeksforgeeks.org/system-design/observer-pattern-set-1-introduction/
'''


# This class is the Subject in the Observer pattern.
# It keeps a list of followers and notifies them when a message is sent.
class Channel:
    def __init__(self, channel_name: str, followers: list=None) -> None:
        # channel_name: the name of this channel
        # followers: an optional initial list of observer objects
        # Use a new list when no followers are provided to avoid shared mutable default.
        self.channel_name = channel_name
        self.followers = [] if followers is None else followers

    def add_follower(self, follower: object) -> None:
        # Add a follower (observer) to this channel's list.
        # The follower is expected to implement channel_updated(channel_name, message).
        self.followers.append(follower)

    def send_message(self, message: str) -> None:
        # Notify every follower about a new message.
        # For each follower call its channel_updated method with channel name and message.
        for follower in self.followers:
            follower.channel_updated(self.channel_name, message)
    

# This class defines the Observer interface.
# In Python this is a simple base class with the expected method signature.
class Observer:
    def channel_updated(self, channel_name: str, message: str) -> None:
        # The base method is a placeholder.
        # Concrete observer classes should override this method.
        pass


# This class is a concrete Observer.
# Each User receives notifications from channels it follows.
class User(Observer):
    def __init__(self, username: str) -> None:
        # username: the display name for this user
        self.username = username

    def channel_updated(self, channel_name: str, message: str) -> None:
        # Called by Channel when a new message is sent.
        # Print a readable notification for this user.
        print(f"\n For `{self.username}`, there's a new message from channel `{channel_name}`: {message}\n")
    

# Example usage: create channels and users, subscribe users, then send messages.
if __name__ == '__main__':
    print('\n\n\n\n\n')

    technology_channel = Channel('TeChNoLoGiA')
    sports_channel = Channel('SPORTS')

    # Create user observers
    user1 = User('Ali')
    user2 = User('Reza')
    user3 = User('Alexander')
    user4 = User('Zeinab')
    user5 = User('Fatemeh')
    user6 = User('Rosy')

    # Subscribe users to channels (add followers)
    technology_channel.add_follower(user1)
    technology_channel.add_follower(user4)
    technology_channel.add_follower(user5)
    sports_channel.add_follower(user2)
    sports_channel.add_follower(user3)
    sports_channel.add_follower(user6)

    # Send messages: each channel notifies its own followers only
    technology_channel.send_message('Hi! There is just a new Samsung phone that is going to be published very soon! Its name is S26 Ultra.')
    sports_channel.send_message('Hello sport fans! In the previous F1 grand prix in Monza italy, the winner of the race was Max Verstappen!!!')

    print('\n\n\n\n\n')
