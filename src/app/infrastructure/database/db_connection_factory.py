from psycopg2 import pool


class DatabaseConnectionFactory:   
    _connection_pool = None
    
    @classmethod
    def initialize(cls, minconn: int = 1, maxconn: int = 5):
        if cls._connection_pool is None:
            cls._connection_pool = pool.SimpleConnectionPool(
                minconn,
                maxconn,
                user='postgres',
                password='abc123',
                host='localhost',
                port='5432',
                database='postgres'
            )
            
    @classmethod
    def get_connection(cls):
        if cls._connection_pool is None:
            raise Exception("Connection pool is not initialized. Call initialize() first.")
        return cls._connection_pool.getconn()
    
    @classmethod
    def realease_connection(cls, connection):
        if cls._connection_pool is None:
            raise Exception("Connection pool is not initialized. Call initialize() first.")
        cls._connection_pool.putconn(connection)
        
        
    @classmethod
    def close_all_connections(cls):
        if cls._connection_pool is not None:
            cls._connection_pool.closeall()
            cls._connection_pool = None
        else:
            raise Exception("Connection pool is not initialized. Call initialize() first.")
