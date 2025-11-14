import directions
import logging
import xml.etree.ElementTree as ET

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_incoming_in_xml(filepath):
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except FileNotFoundError:
        logging.error(f'Помилка: XML-файл не знайдено за шляхом: {filepath}')
        return
    except ET.ParseError as e:
        logging.error(f'Помилка парсингу XML-файлу {filepath}. Перевірте синтаксис XML. Деталі: {e}')
        return

    for group in root.findall('group'):
        timing_exbytes = group.find('timingExBytes')
        if timing_exbytes is not None:
            incoming = group.find('incoming')
            if incoming is not None:
                logging.info(f"Group: {group.find('name').text}, incoming: {incoming.text}")
            else:
                logging.info("Group: {group.find('name').text}, incoming: Не знайдено")

xml_file_path = directions.FILES_DIR / 'xml' / 'groups.xml'
find_incoming_in_xml(xml_file_path)