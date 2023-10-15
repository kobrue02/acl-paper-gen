from acl_text_gen import ACLPaper

from pylatex import Document, Section

class LaTeXDocument:

    def __init__(self, paper: ACLPaper) -> None:
        self.paper = paper
        self.doc = self.__build_doc()

    def __build_doc(self):
        doc = Document('paper')
        with doc.create(Section("Abstract")):
            doc.append(self.paper.content["abstract"])
        for section in self.paper.content["sections"].asdict():
            with doc.create(Section(section.title)):
                doc.append(section.content)

        return doc
    
    def save_pdf(self):
        self.doc.generate_pdf('paper', clean_tex=False)

