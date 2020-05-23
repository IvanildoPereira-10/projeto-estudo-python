from datetime import date, time, datetime

def workDateTime():
    dataAtual = datetime.now()
    print(dataAtual)
    print(dataAtual.strftime('%c'))
    print(dataAtual.strftime('%d/%m/%Y %H:%M:%S'))
    print(dataAtual.year) ######## .day tras o dia .weekday dia da semana
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado','Domingo')
    print(tupla[dataAtual.weekday()])

def workDte():
    dataAtual = date.today()
    dataAtual_str = dataAtual.strftime('%A %B %Y')
    #print(dataAtual.strftime('%d-%m-%Y'))
    print(type(dataAtual))
    print(dataAtual_str)
    #print(dataAtual.strftime('%A %B %Y'))
    print(type(dataAtual_str))

def workTime():
    horario = time(hour= 12, minute=30,second=33)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S:')
    print(horario_str)

if __name__ == '__main__':
    #workDte()
    #workTime()
    workDateTime()