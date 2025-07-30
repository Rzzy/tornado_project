from tornado.ioloop import IOLoop
from forum import creat_app, manager
from forum.models import UserModel

def start_app():
    creat_app()
    IOLoop.current().start()

def create_table():
    UserModel.create_table()

async def create_data():
    await manager.create(UserModel, id='123', email = 'yz@foxmail.com', password = '123')

if __name__ == '__main__':
    start_app()
    # create_table()
    # 异步函数必须放进事件循环中执行
    # IOLoop.current().run_sync(create_data)