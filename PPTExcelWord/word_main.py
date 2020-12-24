from docx import Document # 创建文档
from docx.oxml.ns import qn # 中文
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT # 段落
from docx.shared import Pt,RGBColor,Mm,Cm # 大小 磅数 字号

from openpyxl import load_workbook
# 我们要设置三个模板
# 模板
def template1(name):
    # 创建嘉宾模板 男士
    word_document = Document() # 创建word文档对象
    word_document.styles['Normal'].font.name = u'微软雅黑' # 正文/标题1/标题2 （英文)
    word_document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'微软雅黑') # 中文

    # -------段落创建P1--------
    p1 = word_document.add_paragraph() # 向word添加段落
    p1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER # 段落剧中对齐
    # -------添加文字----------
    run_text_1 = p1.add_run('万门大学客户大会')
    run_text_1.font.size = Pt(20)

    # --------段落创建P2--------
    p2 = word_document.add_paragraph() # 向word添加段落
    p2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER # 段落居中对齐
    # --------添加文字-----------
    run_text_2 = p2.add_run('邀请函')
    run_text_2.font.size = Pt(36)

    # ---------段落创建p customer-------
    p_customer = word_document.add_paragraph() # 向word添加段落
    p_customer.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT # 段落左对齐
    # ----------添加文字----------------
    run_text_c = p_customer.add_run('尊敬的 %s 先生' % name)
    run_text_c.font.size = Pt(20)

    # ----------创建段落p3--------------
    p3 = word_document.add_paragraph() # 向word添加段落
    # -----------添加文字---------------
    run_text_3 = p3.add_run('    诚邀您参加由万门大学组织的客户答谢会，请于2020年10月1日在万门大学总部准时出席，谢谢！')
    run_text_3.font.size = Pt(16)

    # ----------段落创建P4 公司logo图片----------
    p4 = word_document.add_paragraph() # 向word添加段落
    p4.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER # 段落居中对齐

    # ----------添加文字--------------------
    run_text_4 = p4.add_run()
    run_text_4.add_picture('wmlogo.jpg' , width=Mm(40))



