"""AuthFlood Engine"""
import json,random,time

class AuthFloodDetector:
    def __init__(self,threshold=50,window=10):
        self.threshold=threshold
        self.window=window
        self.auth_log=[]
    
    def log_auth(self,mac,timestamp=None):
        if timestamp is None: timestamp=time.time()
        self.auth_log.append({"mac":mac,"time":timestamp})
        self.auth_log=[e for e in self.auth_log if timestamp-e["time"]<self.window]
    
    def detect_flood(self):
        if len(self.auth_log)>self.threshold:
            macs={}
            for e in self.auth_log: macs[e["mac"]]=macs.get(e["mac"],0)+1
            top_mac=max(macs,key=macs.get) if macs else None
            return {"flooding":True,"count":len(self.auth_log),"top_mac":top_mac,"top_count":macs.get(top_mac,0)}
        return {"flooding":False,"count":len(self.auth_log)}
    
    def get_stats(self):
        macs=set(e["mac"] for e in self.auth_log)
        return {"total_auths":len(self.auth_log),"unique_macs":len(macs),"window":self.window}
