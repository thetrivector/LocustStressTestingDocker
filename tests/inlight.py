import sys
import time
import json
from locust import FastHttpUser, task

class MyUser(FastHttpUser):
    connection_timeout = 10.0

    @task
    def inlightStoresCall(self):
        query = """query getRestaurants {
                restaurants {
                    id
                    name
                    longitude
                    latitude
                    phone
                    status
                    openNow
                    orderingEnabled
                    tableOrderingEnabled
                    deliveryEnabled
                    pickUpEnabled
                    dineInGuestCheckoutEnabled
                    deliveryGuestCheckoutEnabled
                    pickUpGuestCheckoutEnabled
                    address {
                        address1
                        address2
                        country
                        postcode
                        state
                        suburb
                        }
                    openingHours {
                        day
                        openingTime
                        closingTime
                        }
                    catering
                    facilities
                    deliveryServices {
                        deliveroo {
                            live
                            link
                            }
                        uberEats {
                            live
                            link
                            }
                        menulog {
                            live
                            link
                            }
                        doorDash {
                            live
                            link
                            }
                        }
                    averageOrderTime
                    thresholds {
                        lowerThresholdAmount
                        orderType
                        time
                        }
                    utcOffset
                    seoTitle
                    isHoliday
                    }
            }
            """

        self.client.post("", json={"query": query, "variables":{}}, name="Inlight Stores Call")

    @task
    def inlightMenuCall(self):
        query = "query getMenu($restaurantId: String!, $loadDetails: Boolean, $orderType: OrderType) {  menu(    input: {restaurantId: $restaurantId, loadDetails: $loadDetails, orderType: $orderType}  ) {    id    name    categories {      name      handle      description      products {        ...ProductFields      }    }    nutrition    recommendedProducts    featuredProducts    menuPromotion {      enabled      name      description      plu    }    showStockShortageAlert  }}fragment ProductFields on Product {  choices {    id    type    name    maximumOptionQuantity    maximumOptionLimit    minimumOptionLimit    defaultSelectedOptions    options {      id      description      kilojoules      name      plu      points      prices {        cents        points      }      sortOrder      size      groupName      suitability      isAvailable      image    }  }  description  disclaimer  id  image  kilojoules  isDetailedProduct  byoType  modifier  longName  shortName  groupName  name  otherSizes  points  prices {    cents    points  }  size  suitability  isAvailable}"

        self.client.post("", name="Inlight Menu Call", json={"query": query, "variables":{"restaurantId":"50","loadDetails":True,"orderType":"PICK_UP"}})

    @task
    def inlightValidateOrder (self):
        query = "query ValidateOrder($input: OrderInput!) {  validateOrder(input: $input) {    message    success  }}"

        self.client.post("", name="Inlight Validate Order", debug_stream=sys.stderr, json={"query": query, "variables":{
            "input": {
                "offers": [],
                "orderItems": [
                    {
                        "options": [],
                        "price": 375,
                        "productId": "DINE_IN-205-4001",
                        "quantity": 1
                    }
                ],
                "orderNotes": "",
                "orderTotal": 375,
                "orderTotalSplitArray": [
                    {
                        "orderTotal": 375,
                        "paymentType": "CREDIT_CARD"
                    }
                ],
                "orderType": "DINE_IN",
                "pickUpTime": "ASAP",
                "receiptType": "NONE",
                "restaurantId": "12",
                "surcharges": [],
                "tableNumber": "1"
            }
    }})