from django import template




register = template.Library()




def percent(num):

    num  = num * 100

    return int(round(num,1))



def roundNum(num, step):

    return round(num,step)




register.filter('percent', percent)

register.filter('round', roundNum)