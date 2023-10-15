from nlg import NLGModule
from tqdm import tqdm

import ast

class ACLPaperTopic(NLGModule):

    def __init__(self) -> None:
        super().__init__()
        self._topic = self.__invent_topic()
        self._title = self.__generate_title()

    def __invent_topic(self):

        topic_prompt= [
            {"role": "system", "content": self._system},
            {"role": "user", "content": "Come up with a new interesting topic related to NLP."}
        ]
        topic = self._get_response(topic_prompt)
        return topic
    
    def __generate_title(self):
        title_prompt = [
                {"role": "system", "content": self._system},
                {"role": "user", "content": \
                 "Write an accurate and interesting title for a novel ACL style paper on the topic of {}".format(self._topic)}
            ]
        title = self._get_response(title_prompt)
        return title

    def __repr__(self):
        return self._title

class ACLPaperAbstract(NLGModule):

    def __init__(self, topic: str) -> None:
        super().__init__()
        self._topic = repr(topic)
        self._abstract = self.__generate_abstract()

    def __generate_abstract(self) -> str:
        abstract_prompt = [
                {"role": "system", "content": self._system},
                {"role": "user", "content": \
                 "Write an accurate and interesting abstract for a novel ACL style paper called {}".format(self._topic)}
            ]
        return self._get_response(abstract_prompt)
    
    def __repr__(self):
        return self._abstract

class ACLPaperSectionTitles(NLGModule):

    def __init__(self, topic: str, abstract: str) -> None:
        super().__init__()
        self._topic = repr(topic)
        self._abstract = repr(abstract)
        self._sections = self.__generate_sections()

    def __generate_sections(self) -> list:
        section_prompt = [
                {"role": "system", "content": self._system},
                {"role": "user", "content": \
                 f"""
                 You are writing a paper on {self._topic}. You have already written this abstract:\n{self._abstract}.
                 Come up with 6 useful sections that your paper will contain.
                 Return the titles of the sections in a python list. Do not enumerate the titles."""}
            ]
        sections = self._get_response(section_prompt)
        return ast.literal_eval(sections)
    
    def aslist(self):
        return self._sections

class ACLPaperSection(NLGModule):
    def __init__(self, topic: str, section: str) -> None:
        super().__init__()
        self._topic = repr(topic)
        self.title = section
        self.content = self.__write_section()

    def __write_section(self):
        section_prompt = [
                        {"role": "system", "content": self._system},
                        {"role": "user", "content": \
                        f"""
                        You are writing a paper on {self._topic}.
                        Currently, you are working on the section "{self.title}".
                        Write the content of this section. It should cover around half a page."""}
                    ]
        return self._get_response(section_prompt)
    
    def __repr__(self):
        return self.content

class ACLPaperSections(NLGModule):

    def __init__(self, topic: str, sections: ACLPaperSectionTitles) -> None:
        super().__init__()
        self._topic = repr(topic)
        self.section_titles = sections.aslist()

    def __write_section(self, section: str) -> ACLPaperSection:
        return ACLPaperSection(self._topic, section)
    
    def __write(self) -> dict:
        content = {}
        for section in tqdm(self.section_titles):
            section = self.__write_section(section)
            section_text = section.content
            content[section] = section_text
        return content
    
    def asdict(self):
        return self.__write()

class ACLPaper:

    def __init__(self) -> None:
        self.content = self.__build()
    
    def __build(self):
        topic = ACLPaperTopic()
        abstract = ACLPaperAbstract(topic)
        section_titles = ACLPaperSectionTitles(topic, abstract)
        sections = ACLPaperSections(topic, section_titles)
        paper = {
            "topic": repr(topic), 
            "abstract": repr(abstract),
            "section_titles": section_titles.aslist(),
            "sections": sections}
        return paper
