import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from state import UserDate
from config import *
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage



storage = MemoryStorage()
bot =Bot(token=API_TOKEN)
dp=Dispatcher(bot, storage=storage)


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=lang)




@dp.message_handler(text = "Uzbek")
async def exo(message: types.Message):

    await message.answer("Raqamingzni yuboring", reply_markup=contact)
    await UserDate.telfon_raqam.set()
    
    
@dp.message_handler(content_types=  "contact", state= UserDate.telfon_raqam)
async def exo(message: types.Message, state = FSMContext):
    tel = message.contact['phone_number']
    
    await state.update_data(telfon_raqam =tel)
    await message.answer("Sizni qaysi kasallik bezovta qilyapti", reply_markup=kasal)   
    await UserDate.kasal_turi.set()


@dp.message_handler(text = "Semizlik", state=UserDate.kasal_turi)
async def exo(message: types.Message, state: FSMContext):
    
    await state.update_data(kasal_turi= message.text)
    await message.answer("Yoshingiz nechi")
    await UserDate.yosh3.set()
    
    
@dp.message_handler(state=UserDate.yosh3)
async def exo(message: types.Message, state: FSMContext):
    
    await state.update_data(yosh3= message.text)
    await message.answer("Boyingiz")
    await UserDate.boy3.set()
    
    
    
@dp.message_handler(state=UserDate.boy3)
async def exo(message: types.Message, state: FSMContext):
    
    await state.update_data(boy3= message.text)
    await message.answer("Vazningiz")
    await UserDate.vazn3.set()
    

@dp.message_handler(state=UserDate.vazn3)
async def exo(message: types.Message, state: FSMContext):
    
    await state.update_data(vazn3= message.text)
    await message.answer("Qayerdansiz")
    await UserDate.qayer2.set()    


@dp.message_handler(state=UserDate.qayer2)
async def exo(message: types.Message, state: FSMContext):
    
    await state.update_data(qayer2= message.text)
    data = await state.get_data()
    tel_ = data.get("telfon_raqam")
    kasallik_ = data.get("kasal_turi")
    nech_ = data.get("yosh3")
    yosh_ = data.get("boy3")
    insulin_ = data.get("vazn3")
    qat = data.get("qayer2")
    
    info_ = f"""Telfon raqam: +{tel_}
Kasallik turi: {kasallik_}
Yosh: {nech_}
Boy: {yosh_}
Vazn: {insulin_}
Qayerdanligi: {qat}

User id: @{message.from_user.username}"""
    
    await bot.send_message(admin, info_)
    await message.answer("Tez orada siz bilan boglanamiz") 
    await state.finish()
    await state.reset_data()

    
    
    
    
    
    




@dp.message_handler(text = "Qandli diabet", state=UserDate.kasal_turi)
async def exo(message: types.Message, state: FSMContext):
    
    await state.update_data(kasal_turi= message.text)
    await message.answer("Sizda qandli diabetning nechanchi turi", reply_markup=diabet)
    await UserDate.nechanci.set()
    
    
@dp.message_handler(text = "1 tip")
async def exo(message: types.Message):
    
    await message.answer("Mumkinmas")
    
    
    
    
@dp.message_handler(text = "2 tip", state=UserDate.nechanci)
async def exo(message: types.Message, state: FSMContext):
    p = message.text
    
    await state.update_data(nechanci = p)
    await message.answer("Yoshingiz nechida")
    await UserDate.yosh.set()
 
    
@dp.message_handler(state=UserDate.yosh)
async def exo(message: types.Message, state = FSMContext):

    await state.update_data(yosh=message.text)

    await message.answer("Kasallik necha yil boldi")
    await UserDate.yil.set()

    
@dp.message_handler(state=UserDate.yil)
async def exo(message: types.Message, state = FSMContext):

    await state.update_data(yil=message.text)

    await message.answer("Insulin ukol olganmisiz", reply_markup=insulin)
    await UserDate.insulin.set()
    
    
@dp.message_handler(text = "Ha", state=UserDate.insulin)
async def exo(message: types.Message, state: FSMContext):

    await state.update_data(insulin = message.text)
    await message.answer("Vazn qancha") 
    await UserDate.vazn.set()
    


@dp.message_handler(text = "Yoq", state=UserDate.insulin)
async def exo(message: types.Message, state: FSMContext):

    await state.update_data(insulin = message.text)
    data = await state.get_data()
    tel_ = data.get("telfon_raqam")
    kasallik_ = data.get("kasal_turi")
    nech_ = data.get("nechanci")
    yosh_ = data.get("yosh")
    insulin_ = data.get("insulin")

    info_ = f"""Telfon raqam: +{tel_}
Kasallik turi: {kasallik_}
Tur: {nech_}
Yosh: {yosh_}
Insulin: {insulin_}

User id: @{message.from_user.username}"""
    
    await bot.send_message(admin, info_)
    await message.answer("Tez orada siz bilan boglanamiz") 
    await state.finish()
    await state.reset_data()
    

    
    
    
    
@dp.message_handler(state=UserDate.vazn)
async def exo(message: types.Message, state: FSMContext):


    await state.update_data(vazn = message.text)
    await message.answer("Boyingiz nechi")
    await UserDate.boy.set()
    
@dp.message_handler(state=UserDate.boy)
async def exo(message: types.Message, state: FSMContext):


    await state.update_data(boy = message.text)
    data = await state.get_data()
    tel_ = data.get("telfon_raqam")
    kasallik_ = data.get("kasal_turi")
    nech_ = data.get("nechanci")
    yosh_ = data.get("yosh")
    yil_ = data.get("yil")
    insulin_ = data.get("insulin")
    vazn_ = data.get("vazn")
    buy_ = data.get("boy")
    qayer_ = data.get("qayerdansiz")
    info_ = f"""Telfon raqam: +{tel_}
Kasallik turi: {kasallik_}
Tur: {nech_}
Yosh: {yosh_}
Insulin: {insulin_}
Vazn: {vazn_}
Buy: {buy_}
Qayerdanligi: {qayer_}
Username: @{message.from_user.username}"""
    
    
    await bot.send_message(admin, info_)
    await message.answer("Tez orada siz bilan boglanamiz") 
    await state.finish()
    await state.reset_data()
    
    
    
    
    
    
@dp.message_handler(text = "Bilmayman",state=UserDate.nechanci)
async def exo(message: types.Message, state : FSMContext):

    await state.update_data(nechanci=message.text)

    await message.answer("Yoshingiz nechida", reply_markup=tip3)
    await UserDate.yosh1.set()
    
@dp.message_handler(text = "25 va yuqori",state=UserDate.yosh1)
async def exo(message: types.Message, state : FSMContext):

    await state.update_data(yosh1=message.text)

    await message.answer("Insulin olganmisiz", reply_markup=insulin_2)
    await UserDate.insulin2.set()    
    


@dp.message_handler(text = "YOQ", state=UserDate.insulin2)
async def exo(message: types.Message, state: FSMContext):


    await state.update_data(insulin2 = message.text)
    await message.answer("Vazningiz") 
    await UserDate.vazn2.set()
    

@dp.message_handler(state = UserDate.vazn2)
async def exo(message: types.Message, state:FSMContext):


    await state.update_data(vazn2 = message.text)
    await message.answer("Boyingiz" ) 
    await UserDate.boy2.set()
    
@dp.message_handler(state = UserDate.boy2)
async def exo(message: types.Message, state:FSMContext):


    await state.update_data(boy2 = message.text)
    await message.answer("Qayerdansiz")
    await UserDate.qayer.set()

@dp.message_handler(state= UserDate.qayer)
async def exo(message: types.Message, state:FSMContext):
    await state.update_data(qayer = message.text)
    data = await state.get_data()
    tel_ = data.get("telfon_raqam")
    kasallik_ = data.get("kasal_turi")
    nech_ = data.get("nechanci")
    yosh_ = data.get("yosh1")
    
    insulin_ = data.get("insulin2")
    vazn_ = data.get("vazn2")
    buy_ = data.get("boy2")
    qayer_ = data.get("qayer")
    info_ = f"""Telfon raqam: +{tel_}
Kasallik turi: {kasallik_}
Tur: {nech_}
Yosh: {yosh_}
Insulin: {insulin_}
Vazn: {vazn_}
Buy: {buy_}
Qayerdanligi: {qayer_}
Username: @{message.from_user.username}"""
    
    
    await bot.send_message(admin, info_)
    
    
    await message.answer("Tez orada mutaxasis siz bilan boglanadi") 
    await state.finish()
    await state.reset_data()
    
    
   












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)