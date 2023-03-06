from todoist_api_python.api import TodoistAPI

QURAN_SECTION_ID = "116699327"
KANJI_SECTION_ID = "116699528"
api = TodoistAPI("218789454eee0f5a21e3353580d2fd219228bff7")

def add_quran():
    for page in range(50, 61):
        for part in range(5):
            string = f"Page {page}, part {part+1}/5"
            print(string)

            api.add_task(
                content=string,
                section_id=QURAN_SECTION_ID
            )

    for page in range(28, 50):
        string = f"Murajaah page {page}"
        print(string)
        api.add_task(
            content=string,
            section_id=QURAN_SECTION_ID
        )

def add_kanji():
    for char in range(113, 201):
        string = f"Learn kanji no. {char}"
        print(string)

        api.add_task(
            content=string,
            section_id=KANJI_SECTION_ID
        )


def add_quran_maintain():
    for page in range(47, 61):
        for repeat in range(5):
            string = f"Page {page}, repeat #{repeat+1}"
            print(string)
            
            api.add_task(
                content=string,
                section_id=QURAN_SECTION_ID
            )


def main():
    add_quran_maintain()

if __name__ == "__main__":
    main()