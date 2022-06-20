from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        #Get products by category
        self.client.get("/item/get_products/b8b02eb8-f9ed-4e63-8b80-7cbc575ec9fb")
        #Failing to get not existent product
        self.client.get("/get/ewfufu4fq9ih984oe")
        #Serach existing product
        self.client.get("/item/get/ad32aa06-c86a-45b8-a4e5-e603f861a047")
        #Search by filter in body
        self.client.post("/item/filter/", json={"name": "Pollo"})
        #Search by filter in body
        self.client.post("/item/filter/", json={"name": "Pollo", "price": "22.5"})
        #Search by filter in body
        self.client.post("/item/filter/", json={"name": "Pollo", "price": "22.5", "category": "b8b02eb8-f9ed-4e63-8b80-7cbc575ec9fb"})

#     @task
#     def login(self):
#         self.client.post("/api/v4/account/login_by_password", data={"username": "1140605175", "password": "JuanPerez00"})
#         self.client.get("/user/account/profile")

# b8b02eb8-f9ed-4e63-8b80-7cbc575ec9fb