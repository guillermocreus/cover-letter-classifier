class Classifier:
    def classification_scores(
        self, cover_letter: str, labels: list[str]
    ) -> list[(str, float)]:
        """
        Given cover letter text and a list of labels, return list of label
        and score pairs.
        """
        pass

    def classification_interpret(
        self, cover_letter: str, label: str
    ) -> list[(str, float)]:
        """
        Given cover letter text and a label, return list of each cover 
        letter token and score pairs.
        """
        pass
