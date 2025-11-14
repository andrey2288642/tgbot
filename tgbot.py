import pyzipper
import os
import sys
import tempfile
import subprocess
import time
import signal
import psutil  # pip install psutil

# КОНФИГУРАЦИЯ
ZIP_PASSWORD = "9423123"  # Ваш пароль от ZIP

def main():
    # Ищем ZIP файлы
    zips = [f for f in os.listdir('.') if f.endswith('.zip')]
    if not zips:
        print("ZIP файл не найден в текущей директории")
        return
    
    zip_file = zips[0]
    print(f"Найден ZIP файл: {zip_file}")
    
    # Создаем временную директорию для распаковки
    temp_dir = tempfile.mkdtemp()
    print(f"Создана временная директория: {temp_dir}")
    
    try:
        # Распаковываем архив
        extract_success = extract_zip(zip_file, temp_dir)
        
        if not extract_success:
            print("Не удалось распаковать архив")
            return
        
        # Ищем Python файлы в распакованной директории
        py_files = find_python_files(temp_dir)
        
        if not py_files:
            print("Python файлы не найдены в распакованном архиве")
            return
        
        print(f"Найдены Python файлы: {py_files}")
        
        # Запускаем основной файл в отдельном процессе
        run_bot_in_subprocess(py_files, temp_dir)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        import traceback
        traceback.print_exc()

def extract_zip(zip_file, extract_to):
    """Распаковывает запароленный ZIP архив"""
    try:
        with pyzipper.AESZipFile(zip_file, 'r') as z:
            # Устанавливаем пароль
            z.setpassword(ZIP_PASSWORD.encode('utf-8'))
            
            # Проверяем архив
            z.testzip()
            print("ZIP архив валиден")
            
            # Распаковываем все файлы
            z.extractall(extract_to)
            print(f"Архив успешно распакован в: {extract_to}")
            
            return True
            
    except pyzipper.BadZipFile:
        print("Ошибка: Файл не является ZIP архивом или поврежден")
        return False
    except pyzipper.ZipDecryptionError:
        print("Ошибка: Неверный пароль")
        return False
    except Exception as e:
        print(f"Ошибка при распаковке: {e}")
        return False

def find_python_files(directory):
    """Находит все Python файлы в директории и поддиректориях"""
    python_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                python_files.append(full_path)
    
    return python_files

def select_main_file(py_files):
    """Выбирает основной файл для запуска по приоритету"""
    # Приоритет 1: main.py
    for file in py_files:
        if os.path.basename(file) == 'main.py':
            return file
    
    # Приоритет 2: __main__.py
    for file in py_files:
        if os.path.basename(file) == '__main__.py':
            return file
    
    # Приоритет 3: run.py, start.py, app.py
    priority_names = ['run.py', 'start.py', 'app.py', 'script.py', 'bot.py', 'tgbot.py']
    for priority_name in priority_names:
        for file in py_files:
            if os.path.basename(file) == priority_name:
                return file
    
    # Приоритет 4: первый файл в корневой директории
    root_files = [f for f in py_files if os.path.dirname(f) == os.path.dirname(py_files[0])]
    if root_files:
        return root_files[0]
    
    # Приоритет 5: любой первый файл
    return py_files[0] if py_files else None

def run_bot_in_subprocess(py_files, temp_dir):
    """Запускает бота в отдельном subprocess и следит за ним"""
    main_file = select_main_file(py_files)
    if not main_file:
        print("Не удалось выбрать основной файл для запуска")
        return
    
    print(f"Запускаем бота: {main_file}")
    print("Бот запущен в отдельном процессе...")
    print("Для остановки нажмите Ctrl+C\n")
    
    process = None
    restart_count = 0
    max_restarts = 10
    
    def signal_handler(sig, frame):
        """Обработчик Ctrl+C"""
        nonlocal process
        print("\n🛑 Останавливаем бота...")
        if process and process.poll() is None:
            # Останавливаем процесс и все его дочерние процессы
            try:
                parent = psutil.Process(process.pid)
                children = parent.children(recursive=True)
                for child in children:
                    child.terminate()
                parent.terminate()
            except:
                pass
        sys.exit(0)
    
    # Регистрируем обработчик сигнала
    signal.signal(signal.SIGINT, signal_handler)
    
    while restart_count < max_restarts:
        try:
            print(f"🚀 Запуск бота (попытка {restart_count + 1}/{max_restarts})...")
            
            # Запускаем бота в отдельном процессе
            process = subprocess.Popen(
                [sys.executable, main_file],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Читаем вывод в реальном времени
            def read_output(pipe, pipe_name):
                for line in pipe:
                    print(f"[BOT] {line}", end='')
            
            import threading
            stdout_thread = threading.Thread(target=read_output, args=(process.stdout, "stdout"))
            stderr_thread = threading.Thread(target=read_output, args=(process.stderr, "stderr"))
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            stdout_thread.start()
            stderr_thread.start()
            
            # Ждем завершения процесса
            return_code = process.wait()
            
            if return_code == 0:
                print("✅ Бот завершил работу нормально")
                break
            else:
                restart_count += 1
                print(f"⚠️ Бот завершился с кодом {return_code}. Перезапуск через 5 секунд...")
                time.sleep(5)
                
        except KeyboardInterrupt:
            signal_handler(signal.SIGINT, None)
            break
        except Exception as e:
            restart_count += 1
            print(f"❌ Ошибка запуска бота: {e}. Перезапуск через 5 секунд...")
            time.sleep(5)
    
    if restart_count >= max_restarts:
        print(f"❌ Достигнуто максимальное количество перезапусков ({max_restarts})")

if __name__ == "__main__":
    print("=== 🤖 Telegram Bot Launcher ===")
    print("Бот будет запущен в отдельном процессе")
    print("Для остановки нажмите Ctrl+C\n")
    main()