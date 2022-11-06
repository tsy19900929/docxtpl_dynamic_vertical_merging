from docxtpl import DocxTemplate
from docxtpldvm import DVM

tpl=DocxTemplate('test2_tpl__2.docx')
context = {
  'items':[
    {
      'gene':'CYP2D6',
      'level':'3',
      'detail':[
        {
          'rsid':'*3/rs35742686',
          'geno':'TT',
        },
        {
          'rsid':'*4/rs3892097',
          'geno':'CC',
        }
      ]
    },

    {
      'gene':'ADRB1',
      'level':'2A',
      'detail':[
        {
          'rsid':'rs1801253',
          'geno':'CC',
        }
      ]
    }
  ],
  'suggest':'warning',
  'd':DVM([(1,3)]),
}
tpl.render(context)
tpl.save('test2_out__2.docx')

