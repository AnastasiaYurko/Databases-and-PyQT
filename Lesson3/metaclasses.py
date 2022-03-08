import dis

"""
Реализовать метакласс ClientVerifier, выполняющий базовую проверку класса «Клиент» 
(для некоторых проверок уместно использовать модуль dis):
отсутствие вызовов accept и listen для сокетов;
использование сокетов для работы по TCP
"""


class ClientVerifier(type):
    def __init__(cls, class_name, bases, class_dict):
        methods = []
        for func in class_dict:
            try:
                calls = dis.get_instructions(class_dict[func])
            except TypeError:
                pass
            else:
                for call in calls:
                    if call.opname == 'LOAD_GLOBAL':
                        if call.argval not in methods:
                            methods.append(call.argval)

        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError('Присутствует вызов accept или listen для сокетов')

        if 'get_message' in methods or 'send_message' in methods:
            pass
        else:
            raise TypeError('Отстуствуют вызовы get_message или send_message для сокетов')
        super().__init__(class_name, bases, class_dict)


"""
Реализовать метакласс ServerVerifier, выполняющий базовую проверку класса «Сервер»:
отсутствие вызовов connect для сокетов;
использование сокетов для работы по TCP.
"""


class ServerVerifier(type):
    def __init__(cls, class_name, bases, class_dict):
        methods = []
        attrs = []
        for func in class_dict:
            try:
                calls = dis.get_instructions(class_dict[func])
            except TypeError:
                pass
            else:
                for call in calls:
                    print(call)
                    if call.opname == 'LOAD_GLOBAL':
                        if call.argval not in methods:
                            methods.append(call.argval)
                    elif call.opname == 'LOAD_ATTR':
                        if call.argval not in attrs:
                            attrs.append(call.argval)
        print(methods)
        if 'connect' in methods:
            raise TypeError('Присутствуют вызовы connect для сокетов')
        if not ('SOCK_STREAM' in attrs and 'AF_INET' in attrs):
            raise TypeError('Некорректная инициализация сокета.')

        super().__init__(class_name, bases, class_dict)
