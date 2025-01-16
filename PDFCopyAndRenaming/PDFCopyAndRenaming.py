
import os
import shutil
from datetime import datetime, timedelta
import PyPDF2
from PyPDF2.generic import TextStringObject

# Pfade definieren
source_folder = r"Source/Directory"  # Verzeichnis mit den Original-PDFs
destination_folder = r"Destination/Directory"  # Verzeichnis für kopierte und umbenannte PDFs

# Funktion zur Berechnung der Kalenderwoche und des Datumsbereichs
def calculate_week_dates(start_date: datetime, week_offset):
    start_of_week = start_date + timedelta(days=(8-start_date.isoweekday()) % 7)
    end_of_week = start_of_week + timedelta(days=4)
    return start_of_week, end_of_week

# Funktion zum Kopieren und Umbenennen von PDFs
def copy_and_rename_pdfs(start_month, end_month):
    start_of_week = datetime.strptime(f'01.{start_month}.2024', '%d.%m.%Y')
    end_date = datetime.strptime(f'31.{end_month}.2024', '%d.%m.%Y')

    week_offset = 1
    source_pdf = os.listdir(source_folder)[0]  # Nimm die erste (und einzige) PDF im Quellverzeichnis
    
    while start_of_week <= end_date:
        start_of_week, end_of_week = calculate_week_dates(start_of_week, week_offset)
        week_str = f"KW{start_of_week.isocalendar()[1]:02d}"
        new_file_name = f"{week_str} {start_of_week.strftime('%d.%m.%Y')} - {end_of_week.strftime('%d.%m.%Y')}.pdf"

        #shutil.copy(os.path.join(source_folder, source_pdf), os.path.join(destination_folder, new_file_name))
        update_pdf_dates(os.path.join(source_folder, source_pdf), os.path.join(destination_folder, new_file_name), start_of_week, end_of_week)

        #week_offset += 1
        start_of_week = end_of_week

# Funktion zum Anpassen der Daten im PDF
def update_pdf_dates(pdf_path, destination_path, start_of_week, end_of_week):
    reader = PyPDF2.PdfReader(pdf_path)
    
    writer = PyPDF2.PdfWriter()
    
    writer.add_page(reader.pages[0].clone(writer))

    
    #    text = text.replace("Ausbildungswoche vom:", f"Ausbildungswoche vom: {start_of_week.strftime('%d.%m.%Y')}")
    #    text = text.replace("bis:", f"bis: {end_of_week.strftime('%d.%m.%Y')}")

    
    writer.update_page_form_field_values(writer.pages[0], { "Ausbildungswoche vom": start_of_week.strftime('%d.%m.%Y'),
                                                           "bis": end_of_week.strftime('%d.%m.%Y'),
                                                          "Ausbildungsjahr": start_of_week.strftime('%Y')})
    #writer.remove_page(1)
    
    
    with open(destination_path, 'wb') as out_pdf:
        writer.write(out_pdf)
        
# Hauptfunktion ausführen
copy_and_rename_pdfs(1, 12)

