from kafka import KafkaProducer
import random
import time

# Создание экземпляра производителя Kafka
#producer = KafkaProducer(bootstrap_servers=['localhost:29092','localhost:19092'])
producer = KafkaProducer(bootstrap_servers=['localhost:19094','localhost:19093','localhost:19092'])

# Бесконечный цикл для отправки сообщений каждые 5 секунд
while True:
    # Генерация случайного числа
    random_number = random.randint(1, 100)

    # Отправка сообщения в топик
    producer.send('my-topic', str(random_number).encode('utf-8'))
    
    producer.flush()
    print(f"Отправлено число: {random_number}")

    # Пауза на 5 секунд
    time.sleep(1)