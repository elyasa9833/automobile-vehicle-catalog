from abc import ABC, abstractmethod

class Spesifikasi(ABC):
    # engine (ex. 3000 cc), gas (ex. Petrol/Diesel), power (ex. 300 hp), transmission (ex. Automatic/Manual)
    def __init__(self, engine, gas, power, transmission):
        self.engine = engine
        self.gas = gas
        self.power = power
        self.transmission = transmission

    @abstractmethod
    def serialize(self):
        pass


class Fitur(ABC):
    # power outlet (ex. False), cruise control (ex. True), keyless (ex. True), airbag (ex. True), sunroof (ex. False)
    def __init__(self, power_outlet, cruise_control, keyless, airbag, sunroof):
        self.power_outlet = power_outlet
        self.cruise_control = cruise_control
        self.keyless = keyless
        self.airbag = airbag
        self.sunroof = sunroof

    @abstractmethod
    def serialize(self):
        pass


# Merk Mobil
class MerkMobil:
    def __init__(self, nama:str):
        self.merk = nama


# Model dari Merk Mobil
class Mobil(MerkMobil, Spesifikasi, Fitur):
    DESKRIPSI_MODEL = ""
    HARGA = 0

    def __init__(self, merk:str, model:str, deskripsi:str, harga:int, engine:int, gas:str, power:int, transmission:str, power_outlet:bool, cruise_control:bool, keyless:bool, airbag:bool, sunroof:bool):
        MerkMobil.__init__(self, merk)
        Spesifikasi.__init__(self, engine, gas, power, transmission)
        Fitur.__init__(self, power_outlet, cruise_control, keyless, airbag, sunroof)
        self.model = model
        Mobil.DESKRIPSI_MODEL = deskripsi
        Mobil.HARGA = harga

    def spesifikasi(self):
        return f"Spesifikasi: \n\tEngine: {self.engine}cc \n\tGas: {self.gas} \n\tPower: {self.power}hp \n\tTransmission: {self.transmission}\n"

    def fitur(self):
        return f"Fitur: \n\tPower Outlet: {self.power_outlet} \n\tCruise Control: {self.cruise_control} \n\tKeyless: {self.keyless} \n\tAirbag: {self.airbag} \n\tSunroof: {self.sunroof}\n"

    # method serialize return dictionary
    def serialize(self):
        return {
            "merk": self.merk,
            "model": self.model,
            "deskripsi": Mobil.DESKRIPSI_MODEL,
            "harga": Mobil.HARGA,
            "spesifikasi": {
                "engine": f"{self.engine} cc",
                "gas": self.gas,
                "power": f"{self.power} hp",
                "transmission": self.transmission
            },
            "fitur": {
                "power_outlet": self.power_outlet,
                "cruise_control": self.cruise_control,
                "keyless": self.keyless,
                "airbag": self.airbag,
                "sunroof": self.sunroof
            }
        }


sigra = Mobil("Daihatsu", "Sigra", "Mobil Keluarga", 200000000, 1200, "Pertalite", 100, "Manual", False, False, False, True, False)
xpander = Mobil("Mitsubishi", "Xpander", "Mobil Keluarga", 300000000, 1500, "Pertamax", 150, "Automatic", True, True, False, True, False)

# print(sigra.serialize())
# print(sigra.spesifikasi())
# print(sigra.fitur())

# print(xpander.serialize())
# print(xpander.spesifikasi())
# print(xpander.fitur())