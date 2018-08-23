'''运行状态插件'''
import re

from coolqbot.bot import bot
from coolqbot.logger import logger

from plugins.repeat import recorder

#TODO:统计复读数据
@bot.on_message('group', 'private')
async def status(context):
    match = re.match(r'^\/(status|状态)', context['message'])
    if match:
        str_data = f'十分钟内发送消息的数量为{recorder.message_number(10)}'
        return {'reply': str_data}
