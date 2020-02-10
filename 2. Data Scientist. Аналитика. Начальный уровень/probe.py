draft_lines = (2, 2, 0, 2, 2, 2)

stores_lines = (200, 200, 200, 200, 200, 200)



# self.ui.countBtn.clicked.connect(self.calculate)


def validate_forms(draft_lines, stores_lines):
    draft_lines = [float(draft_line) for draft_line in draft_lines]
    for draft_line in draft_lines:
        if draft_line not in {2, 7.8}:
            print(draft_line, 'wrong!')
            print("Applicable draft values only: 2 - 7.8"
                  + "\n" +
                  "Applicable density values only: 0.1 - 2"
                  + "\n")
        # warn = QMessageBox.warning(self, 'Message',
        #                            "Applicable draft values only: 2 - 7.8"
        #                            + "\n" +
        #                            "Applicable density values only: 0.1 - 2"
        #                            + "\n", QMessageBox.Ok)

            return None


    draft_lines = [float(draft_line) for draft_line in draft_lines]
    for i in draft_lines:
        print(type(i))

validate_forms(draft_lines, stores_lines)
