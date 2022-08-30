#!/usr/bin/python3
""" Package initilization file
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
