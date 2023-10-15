from acl_text_gen import ACLPaper
from to_latex import LaTeXDocument

if __name__ == "__main__":
    paper = ACLPaper()
    print(paper.content["topic"])
    print(paper.content["abstract"])
    print(paper.content["section_titles"])
    for section in paper.content["sections"].asdict():
        print(section.title)
        print(section.content)
    latex_doc = LaTeXDocument(paper)
    latex_doc.save_pdf()