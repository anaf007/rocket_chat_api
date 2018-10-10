from environs import Env
env = Env()

#版本号
dev_1 = env.str('API_VERSION') or 'v1'