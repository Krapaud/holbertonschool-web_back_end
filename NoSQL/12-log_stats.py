#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""


def print_nginx_stats():
    """
    Provides statistics about Nginx logs in MongoDB
    
    Database: logs
    Collection: nginx
    
    Displays:
    - Total number of logs
    - Number of logs per HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of status checks (method=GET, path=/status)
    """
    pass


if __name__ == "__main__":
    print_nginx_stats()
