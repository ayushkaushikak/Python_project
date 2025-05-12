#OPPS Inheritance

class OTT_subscription:
    def __init__(self, Payment, id, plan):
        self.Payment= Payment
        self.id = id
        self.plan = plan
        
    def subscription(self):
        print(f"Subscriber with {self.id} id subscribed to {self.plan} plan")
        print(f"Payment of {self.Payment} id done")
        
        
    def unsubscription(self):
        print(f"Subscriber with {self.id} id unsubscribed to {self.plan} plan")
        
class Primium_OTT_subscription(OTT_subscription):
    
    def __init__(self, Payment, id, plan, screen):
        super().__init__(Payment, id, plan)
        self.max_screen=screen
        
    def set_max_screen(self):
        print(f"Payment of {self.Payment} id done")
        print(f"Now you subscribed to the premium plan, so your maximum screens are {self.max_screen}.")

#netflix = OTT_subscription(1200,123987,"Monthly")
#netflix.subscription()

premium_netflix = Primium_OTT_subscription(1200,123987,"Quaterly",4)
premium_netflix.subscription()
premium_netflix.set_max_screen()
    