from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.integration import Eventbridge, SQS
from diagrams.aws.network import APIGateway
from diagrams.aws.general import User

with Diagram("AWS Microservices - Event Driven Architecture", show=False):
    user = User("User")

    api = APIGateway("API Gateway")

    # Microservices Cluster
    with Cluster("Microservices"):
        user_service = ECS("User Service")
        order_service = ECS("Order Service")
        payment_service = ECS("Payment Service")

    # Dedicated Databases
    with Cluster("Databases (Dedicated per Service)"):
        user_db = RDS("User DB")
        order_db = RDS("Order DB")
        payment_db = RDS("Payment DB")

    # Event Bus
    event_bus = Eventbridge("Event Bus")

    # Consumers
    with Cluster("Event Consumers"):
        notification = Lambda("Notification Service")
        analytics = Lambda("Analytics Service")

    queue1 = SQS("Notification Queue")
    queue2 = SQS("Analytics Queue")

    # User Flow
    user >> api
    api >> user_service
    api >> order_service
    api >> payment_service

    # Service to DB (Dedicated DB pattern)
    user_service >> user_db
    order_service >> order_db
    payment_service >> payment_db

    # Event-driven communication
    user_service >> event_bus
    order_service >> event_bus
    payment_service >> event_bus

    event_bus >> queue1 >> notification
    event_bus >> queue2 >> analytics