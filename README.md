# LOUNGE-RESTAURANT-COMMENTS

Bu proje, bir restoran yorum sistemi simülasyonudur. Kafka, gRPC, PostgreSQL ve Flask kullanılarak geliştirilmiştir.

## Gereksinimler

- Docker
- Docker Compose

## Kurulum

1. Projeyi klonlayın:

   ```bash
   git clone https://github.com/kaaniince/lounge-restaurant-comments.git
   cd LOUNGE-RESTAURANT-COMMENTS
   ```

2. Docker Compose ile çalıştırın:

   ```bash
   docker-compose up --build
   ```

3. gRPC server için protokol dosyasını oluşturun:

   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. sentiment_analyzer.proto
   ```

4. Producer'ı çalıştırın:

   ```bash
   python producer/producer.py
   ```

5. Consumer'ı çalıştırın:

   ```bash
   python consumer/consumer.py
   ```

6. Rest API'yi çalıştırın:

   ```bash
   python -m consumer.consumer
   ```

7. Rest API'yi test edin:

   ```bash
   curl http://localhost:5000/comments
   ```

   ```bash
   curl http://localhost:5000/comments?category=positive
   ```
