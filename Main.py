from docxtpl import DocxTemplate
doc = DocxTemplate("template3.docx")
spaces_name = ' '*31
spaces_section = ' '*14
context = {'FIO': '{}Сингизину Игорю Ивановичу'.format(spaces_name),
           'SECTION': '{}5.1 Электротехнические комплексы и системы'.format(spaces_section)}
doc.render(context)
doc.save("шаблон-final2.docx")