import sys
import time
from locust import FastHttpUser, task

# Inherits the FastHttpUser class
class MyUser(FastHttpUser):
    connection_timeout = 5.0

    @task
    def redcatStoresCall(self):
        # client = FastHttpSession class
        self.client.get("/", name="Root Call")

