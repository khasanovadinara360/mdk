#!/usr/bin/env python3
"""
Главный скрипт для запуска проекта
Определение языка текста
"""

import sys
import os

# Добавляем папку utils в путь импорта
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Пробуем импортировать
try:
    from collecting_from_api.api_collector import LanguageDetector
    from utils.config import TEXTS_FOR_ANALYSIS, TEST_DATASET
    print("✓ Все модули успешно импортированы")
    
except ImportError as e:
    print(f"✗ Ошибка импорта: {e}")
    print("\nПроверьте структуру проекта:")
    print("  D:\\mdk\\")
    print("  ├── collecting_from_api\\")
    print("  │   ├── __init__.py")
    print("  │   └── api_collector.py")
    print("  ├── utils\\")
    print("  │   ├── __init__.py")
    print("  │   └── config.py")
    print("  └── run_api_part.py")
    sys.exit(1)

def main():
    """Основная функция"""
    
    print("="*70)
    print("ПРОЕКТ: ОПРЕДЕЛЕНИЕ ЯЗЫКА ТЕКСТА")
    print("Используется библиотека: langdetect")
    print("="*70)
    
    # Создаем детектор
    print("\n1. ИНИЦИАЛИЗАЦИЯ ДЕТЕКТОРА...")
    detector = LanguageDetector()
    
    if not detector.detector_available:
        print("\n❌ Невозможно продолжить. Установите библиотеку:")
        print("   pip install langdetect")
        return
    
    # Часть 1: Анализ тестовых текстов
    print("\n2. АНАЛИЗ ТЕКСТОВ...")
    print("-"*40)
    
    # Берем первые 5 текстов для анализа
    texts_to_analyze = TEXTS_FOR_ANALYSIS[:5]
    results = detector.analyze_texts(texts_to_analyze)
    
    # Сохраняем результаты
    detector.save_results(results, 'language_detection_results.csv')
    
    # Часть 2: Дополнительный анализ
    print("\n3. ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ...")
    print("-"*40)
    
    # Проверяем пользовательские тексты
    user_texts = [
    "Data Science is an interdisciplinary field that uses scientific methods to extract knowledge from data.",
    "Машинное обучение - это интересно! Оно позволяет компьютерам учиться на примерах.",
    "L'intelligence artificielle est l'avenir de la technologie moderne.",
    "La ciencia de datos es muy importante para la toma de decisiones empresariales.",
    "Künstliche Intelligenz revolutioniert viele Industriezweige weltweit.",
    "L'apprendimento automatico è una branca dell'intelligenza artificiale.",
    "A análise de dados é fundamental para o crescimento das empresas.",
    "数据科学是现代技术的重要组成部分。",
    "機械学習は人工知能の一分野です。",
    "데이터 과학은 현대 비즈니스에 필수적입니다.",
    "الذكاء الاصطناعي هو مستقبل التكنولوجيا.",
    "डेटा साइंस आधुनिक व्यवसाय के लिए आवश्यक है।",
    "Yapay zeka, birçok endüstride devrim yaratıyor.",
    "Η τεχνητή νοημοσύνη είναι το μέλλον της τεχνολογίας.",
    "Nauka o danych jest kluczowa dla współczesnego biznesu.",
    "Машинне навчання дозволяє комп'ютерам вчитися на прикладах.",
    "Деректер ғылымы заманауи бизнес үшін өте маңызды.",
    "Datawetenschap is essentieel voor moderne bedrijven.",
    "Artificiell intelligens revolutionerar många industrier.",
    "Tekoäly on tulevaisuuden teknologiaa.",
    "Az adattudomány alapvető fontosságú a modern üzleti életben.",
    "Umělá inteligence mění mnoho průmyslových odvětví.",
    "Inteligența artificială este viitorul tehnologiei.",
    "Изкуственият интелект е бъдещето на технологийте.",
    "Вештачка интелигенција је будућност технологије.",
    "בינה מלאכותית היא העתיד של הטכנולוגיה.",
    "هوش مصنوعی آینده فناوری است.",
    "Trí tuệ nhân tạo là tương lai của công nghệ.",
    "ปัญญาประดิษฐ์คืออนาคตของเทคโนโลยี",
    "Kecerdasan buatan adalah masa depan teknologi.",
    "Akili bandia ndio wakati ujao wa teknolojia.",
    "Data Science estas grava por moderna negoco.",
    "Hello! Привет! Bonjour! 你好! 안녕하세요!",
    "Yes",
    "Да",
    "Oui",
    "Sí",
    "はい",
    "نعم"
    ]
    
    print("\nАнализ дополнительных текстов:")
    user_results = detector.analyze_texts(user_texts)
    
    # Сохраняем пользовательские результаты
    detector.save_results(user_results, 'user_texts_analysis.csv')
    
    # Часть 3: Итоги
    print("\n4. ИТОГИ ПРОЕКТА")
    print("-"*40)
    
    total_texts = len(results) + len(user_results)
    
    print(f"\n✓ Всего проанализировано текстов: {total_texts}")
    print(f"✓ Созданы файлы с результатами:")
    print(f"   1. language_detection_results.csv")
    print(f"   2. user_texts_analysis.csv")
    
    # Простой тест точности
    print(f"\n✓ Тест определения языка:")
    test_text = "This is a simple test in English"
    test_result = detector.detect_language(test_text)
    print(f"   Текст: '{test_text}'")
    print(f"   Результат: {test_result['language_name']}")
    
    print("\n" + "="*70)
    print("ПРОЕКТ УСПЕШНО ЗАВЕРШЕН!")
    print("="*70)

if __name__ == "__main__":
    main()