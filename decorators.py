from datetime import datetime


def execute_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execute_time
def random_func():
    for _ in range(1,10000):
        pass


@execute_time
def suma(a: int ,b: int) -> int:
    return a + b

@execute_time
def saludo(nombre="cesar"):
    print('Hola ' + nombre)


random_func()
suma(5, 5)
saludo("Kairi")
