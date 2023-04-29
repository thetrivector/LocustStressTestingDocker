import sys
import time
from locust import FastHttpUser, task

# Inherits the FastHttpUser class
class MyUser(FastHttpUser):
    connection_timeout = 10.0

    @task
    def redcatStoresCall(self):
        # client = FastHttpSession class
        self.client.get("stores", name="Redcat Stores Call")

    @task
    def redcatMenuCall(self):
        self.client.get("stores/50/menu", name="Redcat Menu Call")

