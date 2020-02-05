class BaseEntity():
    def __init__(self) -> None:
        print('#### BASE ENTITY CREATED ###')

    def __del__(self):
        print('#### DESTROYING THE OBJECT ###')
