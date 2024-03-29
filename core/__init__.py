"""
MIT License

Copyright (c) 2024 Aurel Hoxha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import my_secrets.key
import config
import platform
from colorama import Fore, Style
import os
import io
import random
import asyncio
import time
import aiohttp
from PIL import Image, ImageFont, ImageDraw
import discord
import logging
import json
import traceback
from datetime import datetime, timedelta
from discord.ext import commands, tasks
from discord import Modal, TextInput, Button, ButtonStyle, SelectMenu, SelectOption, SlashCommandOption as Option, Localizations,\
    SlashCommandOptionChoice as Choice
from discord.utils import get
from pathlib import Path