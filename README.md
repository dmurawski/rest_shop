﻿# Storefront 🛍️
---
**Storefront** to aplikacja e-commerce stworzona w Django, która pozwala na zarządzanie produktami, zamówieniami i użytkownikami. Aplikacja korzysta z Dockera do uproszczenia konfiguracji środowiska.

## Funkcje projektu 🌟
- Autoryzacja i autentykacja z użyciem Djoser
- Zarządzanie produktami, zamówieniami i kategoriami
- Testy za pomocą **pytest**
- Zastosowanie Redis i Celery do przetwarzania w tle
- Monitoring zadań Celery za pomocą Flower
- Testowy SMTP z użyciem smtp4dev
## Technologie 🛠️
- Python 3.9
- Django 4.2.16
- Docker & Docker Compose
- MySQL
- Redis
- Celery
- Pytest
- Locuts
- Silky
## Wymagania ✅
- Docker
- Docker Compose
## Instalacja i uruchomienie 🚀
1. Sklonuj repozytorium:
```bash
git clone https://github.com/dmurawski/storefront.git
```
2. Uruchom aplikację w Dockerze
```bash
docker-compose up -d --build
```
## Uruchamianie logów danego kontenera 🧪
Aby uruchomić testy jednostkowe:
np. dla tests
```bash
docker-compose logs -f tests
```
## Przykładowe konta 👤
Administrator:
- Login: admin
- Hasło: admin
## Endpointy
### Główne endpointy
**/admin/**

**/app/home/**

**/store/**

**/store/products/**

**/store/carts/** - tworzy koszyk

**/store/collections/** - lista zbiorów

**/store/customers/** - wyswietla userów (tylko admin)

**/store/orders/** - tworzenie zamówienia za pomoca uuid koszyka

**/auth/users/** - tworzenie Customera

**/auth/jwt/create/** - tworzenie tokena JWT

**/auth/jwt/refresh/** - odswieżenie tokena JWT

#### Podendpointy:
- /store/products/*{product_id}*/reviews/ - tworzenie review dla danego produktu
- /store/products/*{product_id}*/ - detail view for product
- /store/products/*{product_id}*/images/ - dodawanie image do product
- /store/carts/*{uuid_cart}*/items/ - dodawanie produktu do koszyka
- /store/customers/me/ - Edycja swojego profilu (admin może edytować wszystkie profile)
- /store/orders/*{order_id}*/ - aktualizacja statusu zamówienia




