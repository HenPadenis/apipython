import pandas as pd
from datetime import datetime
import email.message
import smtplib
from time import sleep
import pyautogui as pg
from flask import Flask, request, jsonify
from flask_cors import CORS


def process_data(dados):
    if 'status' in dados and dados['status'] == 'enviado':
        pg.hotkey('win', 'r')
        pg.write('cmd')
        pg.press('enter')
        sleep(0.5)
        pg.write('ipconfig')
        pg.press('enter')
        sleep(0.3)
        pg.write('hostname')
        pg.press('enter')
    else:
        return {'resposta': 'Status inválido'}    