from locust import HttpUser, TaskSet, task, between
import random

class UserBehavior(TaskSet):
    _user_count = 0
    _auction_id_is_random = False
    _auction_id_max = 0

    def on_start(self):
        self.token = ""
        UserBehavior._user_count += 1
        self.set_default_user()

    def set_default_user(self):
        username = f"buyer{UserBehavior._user_count}"
        password = f"password1234"
        self.token = self.signin_member(username, password)

    def signin_member(self, user_id: str, password: str) -> str:
        response = self.client.post(
            "/auth/signin",
            json={
                "signInId": user_id,
                "password": password
            }
        )
        return response.cookies.get("JSESSIONID")

    @task
    def bid(self):
        if UserBehavior._auction_id_is_random:
            path = f"/auctions/{random.randint(1, UserBehavior._auction_id_max)}/purchase"
        else:
            path = "/auctions/1/purchase"

        self.client.post(
            path, 
            json={
                "price": 1000,
                "quantity": 1
            },
            cookies={"JSESSIONID": self.token})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(0.1, 0.3)