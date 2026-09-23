from fastapi import FastAPI
from routers import login_page, login, logout, main_router, about, about_product, on_startup, search_of_product, serve_verification_file
from routers.gasoline import gasoline_power_plants, gasolinegenerators , inverter_gasolinegenerators
from routers.diesel import diesel_power_plants, diesel_high_voltage_generators, diesel_portable, tss_premium, tss_prof, tss_slavyanka, tss_standart
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from models.offer import Offer
from models.offerimage import OfferImage

# Администрирование
from routers.website_administration import create_product, read_all_product, delete_product, update_product
# Администрирование пользователей
from routers.user import create_user, read_user, delete_user, update_user, about_user

#http://127.0.0.1:8000

#для локальной работы
#postgrSQL
#Порт: 5432
#Суперпользователь: postgres
#Пароль: 11111

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins="",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

#app.include_router(on_startup.router)

app.include_router(main_router.router)
app.include_router(about.router)

# Бензиногенераторы
app.include_router(gasoline_power_plants.router)
app.include_router(gasolinegenerators.router)
app.include_router(inverter_gasolinegenerators.router)

# Дизельные генераторы
app.include_router(diesel_power_plants.router)

app.include_router(diesel_high_voltage_generators.router)
app.include_router(diesel_portable.router)
app.include_router(tss_premium.router)
app.include_router(tss_prof.router)
app.include_router(tss_slavyanka.router)
app.include_router(tss_standart.router)


# Администрирование сайта
app.include_router(create_product.router)
app.include_router(read_all_product.router)
app.include_router(update_product.router)
app.include_router(delete_product.router)

#авторизация
app.include_router(login.router)
app.include_router(login_page.router)

#Пользователь
app.include_router(create_user.router)
app.include_router(read_user.router)
app.include_router(update_user.router)
app.include_router(delete_user.router)
app.include_router(login.router)
app.include_router(about_user.router)
app.include_router(logout.router)

#Поисковая строка
app.include_router(search_of_product.router)
#О продукте
app.include_router(about_product.router)

app.include_router(serve_verification_file.router)