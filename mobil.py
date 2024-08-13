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
        return {
            "engine": f"{self.engine} cc",
            "gas": self.gas,
            "power": f"{self.power} hp",
            "transmission": self.transmission
        }


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
        return {
            "power_outlet": self.power_outlet,
            "cruise_control": self.cruise_control,
            "keyless": self.keyless,
            "airbag": self.airbag,
            "sunroof": self.sunroof
        }


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
        return Spesifikasi.serialize(self)

    def fitur(self):
        return Fitur.serialize(self)

    # method serialize return dictionary
    def serialize(self):
        return {
            "brand": self.merk,
            "model": self.model,
            "deskripsi": Mobil.DESKRIPSI_MODEL,
            "harga": Mobil.HARGA,
            "spesifikasi": self.spesifikasi(),
            "fitur": self.fitur()   
        }


cars = [
    Mobil("Daihatsu", "Sigra", "Mobil Keluarga", 200000000, 1200, "Pertalite", 100, "Manual", False, False, False, True, False),
    Mobil("Mitsubishi", "Xpander", "Mobil Keluarga", 300000000, 1500, "Pertamax", 150, "Automatic", True, True, False, True, False),
    Mobil("Daihatsu", "Terios", "Mobil SUV", 250000000, 1500, "Pertamax", 150, "Automatic", True, True, False, True, False)
]
