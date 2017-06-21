"""
Author: Brian McGinnis

"""

import json
from watson_developer_cloud import ConversationV1

class conversation:

    def __init__(self, usr, pas, workspace):
        self.convo = ConversationV1(
            username = usr,
            password = pas,
            version= '2017-04-21')
        self.workspace_id = workspace

    def sendMessage(self, message):
        response = self.convo.message(workspace_id = self.workspace_id, message_input = {'text': message})
        jsn = json.loads(json.dumps(response))
        return jsn['output']['text'][0]

#con = conversation('154b5b29-d1ca-4ff2-be09-c33c5e1d9e20' , 'pmNftYlpvMS8','9ef80568-2a3b-4790-a8e0-363c0bc7d237')
#respon = con.sendMessage("LOVE ME JERRY")        
#print(respon)
