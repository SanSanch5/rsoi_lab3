from datetime import timedelta

config = {
    'debug': True,

    'website': {
        'port': 5000,
        'session_expires_after': timedelta(weeks=2),
    },       

    'sessions': {
        'port': 5001,
        'db_uri': 'sqlite:///:memory:',
    },       
    'users': {
        'port': 5002,
        'db_uri': 'sqlite:///db/users',
    },       
    'clothes': {
        'port': 5003,
        'db_uri': 'sqlite:///db/clothes',
    },       
    'orders': {
        'port': 5004,
        'db_uri': 'sqlite:///db/orders',
    },       
}
