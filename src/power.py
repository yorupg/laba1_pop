def power_function(target: int, power: int ) -> float:
    """
    Пример функции, которая выполняет операцию возведения в степень
    :param target:  Число, которое будут возводить в степень
    :param input_two: Степень в которую будут возводить число
    :return: Возвращает число возведенное в степень
    """
    return pow(target, power)
def kategor(dano):
    if dano in ('kg', 'g'): return 'massa'
    if dano in ('mm', 'cm', 'm', 'km'): return 'dlina'
    if dano in ('c', 'f', 'k'): return 'temperatura'
def perevod(iz,v):
    if kategor(iz[1])=='massa':
        if iz[1]=='kg' and v=='g': return [iz[0]*1000, 'g']
        if iz[1]=='g' and v=='kg': return [iz[0]/1000,'kg']
        if iz[1]==v: return iz[0]
    if kategor(iz[1])=='dlina':
        vrem=iz[0]
        if iz[1]=='mm': vrem/=1000
        if iz[1]=='cm': vrem/=100
        if iz[1]=='km': vrem *=1000
        if v=='m': return [vrem, 'm']
        if v=='mm': return [vrem*1000, 'mm']
        if v=='cm': return [vrem*100, 'cm']
        if v=='km': return [vrem/1000, 'km']
    if kategor(iz[1])=='temperatura':
        vrem=0
        if iz[1]=='c': vrem=iz[0]
        if iz[1]=='k': vrem=iz[0]- 273.15
        if iz[1]=='f': vrem=(iz[0]-32)/1.8
        if vrem>(-273.15):
            if v=='c': return [vrem, 'c']
            if v=='k': return [vrem+273.15, 'k']
            if v=='f': return [vrem*1.8+32, 'f']
        else: return 'ниже абсолютного нуля'
def converter(zap) -> float:

    iz=[zap[0],zap[1]]
    v=zap[2]
    if kategor(iz[1])==kategor(v):
        return perevod(iz,v)
    else: return 'данный тип не поддерживается'