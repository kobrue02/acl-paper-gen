from nlg import NLGModule


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

class ACLPaper:
    def __init__(self) -> None:
        self.content = self.__build()
    
    def __build(self):
        topic = ACLPaperTopic()
        abstract = ACLPaperAbstract(topic)
        return {
            "topic": repr(topic), 
            "abstract": repr(abstract)
        }
