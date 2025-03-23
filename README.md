# AutoSkip

AutoSkip is a tool that automates clicking the "Skip Intro" button or performing similar actions in applications and video players, saving you time and simplifying interaction with interfaces.

## Installation

To install and set up the project, follow these steps:

1. Clone the repository to your computer:
   ```bash
   git clone https://github.com/dishai/autoskip.git
   ```

2. Navigate to the project directory:
   ```bash
   cd autoskip
   ```

3. (Optional, but recommended) Create a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

4. Install the dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

5. Install the font:
   The project uses a font, the license for which is included in the `OFL.txt` file. To install the font:
   - Locate the font file in the project directory (`serati.ttf`).
   - On Windows: Double-click the font file and select "Install".
   - On macOS: Double-click the font file and choose "Install Font" in the Font Book application.
   - On Linux: Copy the font file to the `~/.fonts/` directory and update the font cache with the command `fc-cache -fv`.

**Note:** Ensure you have Python 3 and the `pip` package manager installed.

## Running the Project

Depending on your operating system, you can run the project as follows:

- **For Windows:**
  If you want to use the pre-built executable, simply run:
  ```
  AutoSkip.exe
  ```

- **For macOS/Linux or if running from source code:**
  Launch the main script using Python:
  ```bash
  python main.py
  ```
  or, if using Python 3:
  ```bash
  python3 main.py
  ```

**Note:** Before running, ensure all dependencies are installed and the virtual environment is activated (if used).

## Usage Examples

Below are examples of how you can use AutoSkip:

- **Automatically skipping intros in a video player:**
  If you want to skip intros in a specific video player, simply launch the program, and it will automatically click the "Skip" button as soon as it appears.

- **Setting a delay before clicking:**
  If you need to set a delay before the automatic click (e.g., 5 seconds), use the `interval` parameter:
  ```bash
  python main.py
  ```

**Note:** Ensure the target application or window is active while the program is running.

## License

This project is distributed under the license specified in the `LICENSE` file. Please review it for detailed information about rights and restrictions.

## Contact

If you have questions, suggestions, or want to report a bug, you can reach me via Telegram:

- Telegram: @dishacker
#
# Русский README
## AutoSkip

AutoSkip — это инструмент, который автоматизирует нажатие на кнопку "Пропустить заставку" или выполняет аналогичные действия в приложениях и видеоплеерах, экономя ваше время и упрощая взаимодействие с интерфейсами.

## Установка

Чтобы установить и настроить проект, выполните следующие шаги:

1. Клонируйте репозиторий на ваш компьютер:
   ```bash
   git clone https://github.com/dishai/autoskip.git

    Перейдите в папку проекта:

	cd autoskip

(Опционально, но рекомендуется) Создайте виртуальную среду для изоляции зависимостей:

python -m venv venv
source venv/bin/activate  # На macOS/Linux
venv\Scripts\activate     # На Windows

Установите зависимости, перечисленные в файле requirements.txt:

    pip install -r requirements.txt

Установите шрифт:
Проект использует шрифт, лицензия на который находится в файле OFL.txt. Чтобы установить шрифт:

    Найдите файл шрифта в папке проекта  (serati.ttf).
    На Windows: дважды щёлкните по файлу шрифта и нажмите "Установить".
    На macOS: дважды щёлкните по файлу шрифта и выберите "Установить шрифт" в программе "Шрифты".
    На Linux: скопируйте файл шрифта в папку ~/.fonts/ и обновите кэш шрифтов командой fc-cache -fv.



Примечание: Убедитесь, что у вас установлен Python версии 3, а также менеджер пакетов pip.
Запуск проекта

## Запуск

В зависимости от вашей операционной системы, вы можете запустить проект следующим образом:

Для Windows:
 Если вы хотите использовать готовый исполняемый файл, просто запустите:
* AutoSkip.exe


Для macOS/Linux или если вы запускаете из исходного кода:
Запустите основной скрипт с помощью Python:

      python main.py

или, если используется Python 3:

    python3 main.py

Примечание: Перед запуском убедитесь, что все зависимости установлены, и вы активировали виртуальную среду (если используете).
Примеры использования

## Ниже приведены примеры, как можно использовать AutoSkip:

   Автоматический пропуск заставок в видеоплеере:
   Если вы хотите пропускать заставки в определённом видеоплеере, просто запустите программу, и она автоматически будет нажимать кнопку "Пропустить", как только она появится:


Настройка задержки перед нажатием:
Если вам нужно задать задержку перед автоматическим нажатием (например, 5 секунд), используйте параметр interval:

Примечание: Убедитесь, что целевое приложение или окно активно во время работы программы.

## Лицензия

Этот проект распространяется под лицензией, указанной в файле LICENSE. Пожалуйста, ознакомьтесь с ним для получения подробной информации о правах и ограничениях.
## Контакты:

Если у вас есть вопросы, предложения или вы хотите сообщить об ошибке, вы можете связаться со мной через Telegram:

 - Telegram: @dishacker
