from .cache_peer import CachePeer
from .get_max_voice_chat import GetMaxVoiceChat
from .mtproto_handler import MtProtoHandler
from .ping import Ping
from .run import Run
from .start import Start


class Utilities(
    CachePeer,
    GetMaxVoiceChat,
    Ping,
    MtProtoHandler,
    Run,
    Start,
):
    pass
