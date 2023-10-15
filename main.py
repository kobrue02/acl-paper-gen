from acl_text_gen import ACLPaper


if __name__ == "__main__":
    paper = ACLPaper()
    print(paper.content["topic"])
    print(paper.content["abstract"])