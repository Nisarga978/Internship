class Speaker:
    def speak(self, message):
        pass
        self.message=message
        return f"Speaking: {self.message}"
class Scheduler:
    def schedule(self, task, time):
        pass
        self.task=task
        self.time=time
        return f"Scheduled {self.task} at {self.time}"
class SmartAssistant(Speaker, Scheduler):
        pass

s1 = SmartAssistant()
print( s1.speak("Hi"))