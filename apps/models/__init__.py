from gino_starlette import Gino
from project_env.settings import *

db = Gino(
    dsn=DB_DSN,
    pool_min_size=DB_POOL_MIN_SIZE,
    pool_max_size=DB_POOL_MAX_SIZE,
    echo=DB_ECHO,
    ssl=DB_SSL,
    use_connection_for_request=DB_USE_CONNECTION_FOR_REQUEST,
    retry_limit=DB_RETRY_LIMIT,
    retry_interval=DB_RETRY_INTERVAL,
)
from models.user import *
