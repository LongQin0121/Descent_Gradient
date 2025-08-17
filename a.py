# k = self.polar["clean"]["k"] 
# drag': {'cd0': 0.018, 'e': 0.799, 'gears': 0.017, 'k': 0.039}



def calculate_k(self):
    """动态计算诱导阻力因子"""
    span = self.aircraft["wing"]["span"]      # 翼展
    area = self.aircraft["wing"]["area"]      # 翼面积
    e = self.aircraft["drag"]["e"]            # 奥斯瓦尔德效率因子
    
    AR = span**2 / area                       # 展弦比
    k = 1 / (np.pi * AR * e)                 # 诱导阻力因子
    
    return k