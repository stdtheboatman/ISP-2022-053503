import http
import json
import logging
from multiprocessing import Process
import os
import time
from typing import Dict, List, Tuple
import requests
import hmac
import hashlib
import threading

class ApiCurrencyHandler:
    def __init__(self):
        pass
        
    def getCurrentServerTime(self):
        response = requests.get("https://api-adapter.backend.currency.com/api/v2/time")
        
        if response.status_code != http.HTTPStatus.OK:
            raise Exception(response.text)
        
        return response.json()["serverTime"]

    def getQueryString(self, sigKey, data: Dict[str,str]):
        queryString = "&".join([key + "=" + item for key, item in data.items()])
        
        signature = hmac.new(sigKey.encode(), queryString.encode(), hashlib.sha256).hexdigest()
        return queryString + "&signature=" + signature 


    def getTrades(self, apiKey, sigKey, symbol, timeBeginMs=None, timeEndMs=None):
        timestamp = str(self.getCurrentServerTime())
        data = {
            "recvWindow": "5000",
            "timestamp": timestamp,
            "symbol": symbol
        }
        
        if timeBeginMs != None:
            data["startTime"] = timeBeginMs
        
        if timeEndMs != None:
            data["endTime"] = timeEndMs
        
        queryString = self.getQueryString(sigKey, data)
        headers = {
            "X-MBX-APIKEY": apiKey
        }
        
        response = requests.get("https://api-adapter.backend.currency.com/api/v2/myTrades", params=queryString, headers=headers)
        
        if response.status_code != http.HTTPStatus.OK:
            raise Exception(response.text)
        
        return response.json()
    
    def getCurrencies(self, apiKey, sigKey):
        timestamp = str(self.getCurrentServerTime())
        data = {
            "recvWindow": "5000",
            "timestamp": timestamp,
        }
        
        queryString = self.getQueryString(sigKey, data)
        headers = {
            "X-MBX-APIKEY": apiKey
        }
        
        
        response = requests.get("https://api-adapter.backend.currency.com/api/v2/currencies", params=queryString, headers=headers)
        
        if response.status_code != http.HTTPStatus.OK:
            raise Exception(response.text)
        
        return response.json()
    
    def getCurrencyInfo(self, apiKey, sigKey, symbol):
        timestamp = str(self.getCurrentServerTime())
        data = {
            "recvWindow": "5000",
            "timestamp": timestamp,
            "symbol": symbol,
        }
        
        queryString = self.getQueryString(sigKey, data)
        headers = {
            "X-MBX-APIKEY": apiKey
        }
        
        
        response = requests.get("https://api-adapter.backend.currency.com/api/v2/depth", params=queryString, headers=headers)
        
        if response.status_code != http.HTTPStatus.OK:
            raise Exception(response.text)
        
        return response.json()
        
    def getCurrencyCost(self, apiKey, sigKey, symbol):
        timestamp = str(self.getCurrentServerTime())
        data = {
            "recvWindow": "5000",
            "timestamp": timestamp,
            "symbol": symbol + "%2FUSD",
        }
        
        queryString = self.getQueryString(sigKey, data)
        headers = {
            "X-MBX-APIKEY": apiKey
        }
        
        
        response = requests.get("https://api-adapter.backend.currency.com/api/v2/depth", params=queryString, headers=headers)
        
        if response.status_code != http.HTTPStatus.OK:
            raise Exception(response.text)
        
        asks = response.json()["asks"]
        
        if len(asks) < 3:
            raise Exception("Not enough information")
        
        costs = [x[0] for x in asks[:3]]
        return sum(costs) / len(costs)
    
    def getAccountInfo(self, apiKey, sigKey):
        timestamp = str(self.getCurrentServerTime())
        data = {
            "recvWindow": "5000",
            "timestamp": timestamp,
        }
        
        queryString = self.getQueryString(sigKey, data)
        headers = {
            "X-MBX-APIKEY": apiKey
        }
        
        
        response = requests.get("https://api-adapter.backend.currency.com/api/v2/account", params=queryString, headers=headers)
        
        if response.status_code != http.HTTPStatus.OK:
            raise Exception(response.text)
        
        return response.json()
          
class ApiNationalBankHandler:
    def __init__(self):
        pass

    def getExchangeRate(self):        
        response = requests.get("https://belarusbank.by/api/kursExchange?city=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA")
        
        if response.status_code != http.HTTPStatus.OK:
            raise Exception(response.text)
        
        return response.json()

class DataHandler(ApiCurrencyHandler, ApiNationalBankHandler):
    def __init__(self,  updateNationalBankApiDataTimerSeconds: int, exchangeRateFilename: str) -> None:
        ApiCurrencyHandler.__init__(self)        
        ApiNationalBankHandler.__init__(self)
        
        self._updateNationalBankApiDataTimerSeconds = updateNationalBankApiDataTimerSeconds
        self._exchangeRateFilename = exchangeRateFilename
        
        self.fiat_exchange_rate: List[Dict[str : str]] = []
        
        if os.path.exists(self._exchangeRateFilename):
            with open(self._exchangeRateFilename, "r") as f:
                self.fiat_exchange_rate = json.load(f)
        else:
            self._update_fiat_exchange_rate()
        
        
        self._set_interval(self._update_fiat_exchange_rate, self._updateNationalBankApiDataTimerSeconds)
        
        self.fiats: List[str] = ["USD", "BYN"]
        
    def _update_fiat_exchange_rate(self): 
        new_data = []
        try:
            new_data = self.getExchangeRate()
        except Exception as error:
            logging.error(error)
    
        if new_data != []:
            with open(self._exchangeRateFilename, "w+") as f:
                json.dump(new_data, f)
            
        self.fiat_exchange_rate = new_data
        
    def _set_interval(self, func, sec):
        def func_wrapper():
            self._set_interval(func, sec) 
            func()  
        
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t
    
    def isFiat(self, symbol) -> bool:
        if symbol in self.fiats:
            return True
        
        return False
    
    def convertFiatToUsd(self, symbol: str, count: float) -> float:
        if symbol == "USD":
            return count
        
        if symbol == "BYN":
            rate = self.getUsdRate()
            return rate[0] * count
        
        raise Exception("Unsuported fiat")
        
    
    def getAccountBalanceUsd(self, apiKey, sigKey) -> float:
        account = self.getAccountInfo(apiKey, sigKey)
        
        sellerCommission = account["sellerCommission"]
        balances = account["balances"]
        
        balance: float = 0
        for currency in balances:
            count: float = currency["free"]
            symbol: str = currency["asset"]
            
            if symbol.find("/") != -1:
                symbol = symbol[0:symbol .find("/")]
            
            
            if self.isFiat(symbol):
                balance += self.convertFiatToUsd(symbol, count)
            else:
                balance += count * self.getCurrencyCost(apiKey, sigKey, symbol) * (1 - sellerCommission / 100)
        
        return balance
    
    def getCurrencyDistribution(self, apiKey, sigKey) -> List[Tuple[str, float]]:
        account = self.getAccountInfo(apiKey, sigKey)
        
        sellerCommission = account["sellerCommission"]
        balances = account["balances"]
        
        distributation = []
        balance: float = self.getAccountBalanceUsd(apiKey, sigKey) 
        for currency in balances:
            count: float = currency["free"]
            symbol: str = currency["asset"]
            
            if symbol.find("/") != -1:
                symbol = symbol[0:symbol .find("/")]
            
            
            rate: float = 0
            if self.isFiat(symbol):
                rate = self.convertFiatToUsd(symbol, count)
            else:
                rate  = count * self.getCurrencyCost(apiKey, sigKey, symbol) * (1 - sellerCommission / 100)
                
            
            data = {'symbol': symbol, 'rate': rate, 'percent': rate / balance}
            distributation.append(data)
        
        return distributation
        
    
    def getUsdRate(self) -> List[float]:
        data: List[Dict[str : str]] = self.fiat_exchange_rate
        
        for currency in data:
            if currency.get("USD_in") is None:
                continue
            
            return [float(currency["USD_in"]), float(currency["USD_out"])]
            
        raise Exception("Couldn't get usd rate")
    

class DataHandlerSingleton:
    instance: DataHandler|None = None
    
    @classmethod
    def getInstance(self) -> DataHandler:
        if self.instance is None:
            self.instance = DataHandler(15 * 60, "exchangeRate.json")
        
        return self.instance
    
def some_task():
    print("hello: ", time.time())
    
def add_interval_task(intervalSeconds, task):
    def task_wrap():
        while(True):
            task()
            time.sleep(intervalSeconds)
            
    p = Process(target=task_wrap)
    p.start()