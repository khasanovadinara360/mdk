import pandas as pd
import time
from typing import Dict, List
from datetime import datetime
import os
import sys

class LanguageDetector:
    
    def __init__(self):
        self.setup_detector()
    
    def setup_detector(self):
        try:
            from langdetect import detect, detect_langs, DetectorFactory
            
            DetectorFactory.seed = 0
            
            self.detect = detect
            self.detect_langs = detect_langs
            self.detector_available = True
            
            print("langdetect загружена")
            
        except ImportError as e:
            print(f"Ошибка импорта: {e}")
            print("Установите библиотеку командой:")
            print("pip install langdetect")
            self.detector_available = False
            self.detect = None
            self.detect_langs = None
    
    def detect_language(self, text: str) -> Dict:
        try:
            from utils.config import LANGUAGE_NAMES
        except ImportError:
             LANGUAGE_NAMES = {
                'en': 'English',
                'ru': 'Russian',
                'fr': 'French',
                'es': 'Spanish',
                'de': 'German',
                'it': 'Italian',
                'pt': 'Portuguese',
                'zh-cn': 'Chinese',
                'ja': 'Japanese',
                'ko': 'Korean',
                'ar': 'Arabic',
                'hi': 'Hindi',
                'tr': 'Turkish',
                'el': 'Greek',
                'pl': 'Polish',
                'uk': 'Ukrainian',
                'kk': 'Kazakh',
                'nl': 'Dutch',
                'sv': 'Swedish',
                'fi': 'Finnish',
                'hu': 'Hungarian',
                'cs': 'Czech',
                'ro': 'Romanian',
                'bg': 'Bulgarian',
                'sr': 'Serbian',
                'he': 'Hebrew',
                'fa': 'Persian',
                'vi': 'Vietnamese',
                'th': 'Thai',
                'id': 'Indonesian',
                'ms': 'Malay',
                'sw': 'Swahili',
                'eo': 'Esperanto',
                'unknown': 'Unknown'
            }
        if not self.detector_available:
            return {
                'text': text[:60] + '...' if len(text) > 60 else text,
                'text_length': len(text),
                'language_code': 'error',
                'language_name': 'Детектор не доступен',
                'confidence': 0,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        
        try:
            lang_code = self.detect(text)
            
            try:
                languages = self.detect_langs(text)
                confidence = languages[0].prob if languages else 0.5
            except:
                confidence = 0.5
            
            language_name = LANGUAGE_NAMES.get(lang_code, lang_code)
            
            return {
                'text': text[:60] + '...' if len(text) > 60 else text,
                'text_length': len(text),
                'language_code': lang_code,
                'language_name': language_name,
                'confidence': round(confidence, 3),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except Exception as e:
            return {
                'text': text[:60] + '...' if len(text) > 60 else text,
                'text_length': len(text),
                'language_code': 'error',
                'language_name': f'ERROR: {str(e)[:50]}',
                'confidence': 0,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
    
    def analyze_texts(self, texts: List[str]) -> List[Dict]:
        results = []
        
        print(f"Начинаю анализ {len(texts)} текстов...")
        
        for i, text in enumerate(texts, 1):
            print(f"[{i}/{len(texts)}] Анализ текста...")
            print(f"   Текст: '{text[:40]}...'")
            
            result = self.detect_language(text)
            results.append(result)
            
            if result['language_code'] != 'error':
                print(f"   Язык: {result['language_name']} уверенность: {result['confidence']:.1%}")
            else:
                print(f"   ОШИБКА: {result['language_name']}")
        
        return results
    
    def save_results(self, data: List[Dict], filename: str = None):
        if not data:
            print("Нет данных для сохранения")
            return
        
        try:
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"language_results_{timestamp}.csv"
        
            file_dir = os.path.dirname(filename)
            if file_dir:
                os.makedirs(file_dir, exist_ok=True)
            else:
                filename = os.path.join(os.getcwd(), filename)
            
            df = pd.DataFrame(data)
            
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            
            print(f"Результаты сохранены: {filename}")
            print(f"Записей сохранено: {len(df)}")
            
            if 'detected_language' in df.columns:
                lang_counts = df['detected_language'].value_counts()
                print("Распределение языков:")
                for lang, count in lang_counts.items():
                    print(f"   {lang}: {count}")
            
            return filename
            
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            print(f"   Тип filename: {type(filename)}")
            print(f"   Значение filename: '{filename}'")
            return None