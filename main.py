from fastapi import FastAPI
from routers import main_router, about, about_product, on_startup, search_of_product
from routers.gasoline import gasoline_power_plants, gasolinegenerators , inverter_gasolinegenerators
from routers.diesel import diesel_power_plants, diesel_high_voltage_generators, diesel_portable, tss_premium, tss_prof, tss_slavyanka, tss_standart
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

#С базой данных
#from routers.with_db import read_all_product, delete_product

#http://127.0.0.1:8000


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


# С использованием базы данных
#app.include_router(read_all_product.router)
#app.include_router(delete_product.router)

#Поисковая строка
app.include_router(search_of_product.router)
#О продукте
app.include_router(about_product.router)
