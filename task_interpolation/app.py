import interpolation.interpolation_controller as inter

def select_action(functions):
    # Выбор действия из доступных
    is_run = True
    while is_run:
        print('\nДоступные операции:')
        for i, item in enumerate(functions):
            print(i, item.__name__)
        i = int(input('\nВыберете операцию: '))
        if i < len(functions):
            function = functions[i]
            function()
        else:
            is_run = False

def select_controller(controllers):
    # Выбор контроллера из доступных
    is_run = True
    while is_run:
        print('\nДоступные контроллеры:')
        for i, item in enumerate(controllers):
            print(i, item.__name__)
        i = int(input('\nВыберете контроллер: '))
        if i < len(controllers):
            controller = controllers[i]
            actions = controller.get_actions()
            select_action(actions)
        else:
            is_run = False

def get_controllers():
    # Получение доступных контроллеров
    return [inter]

controllers = get_controllers()
select_controller(controllers)