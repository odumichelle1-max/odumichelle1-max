# ==========================================
# MULTILINGUAL TRANSLATION SYSTEM - VERSION 2
# ==========================================

translations = {
    "sun": {
        "igbo": "anyanwụ",
        "hausa": "rana",
        "yoruba": "oòrùn",
        "idoma": "Ènɔ̀",
        "tiv": "yange (verify tone/orthography)"
    },

    "moon": {
        "igbo": "ọnwa",
        "hausa": "wata",
        "yoruba": "òṣùpá",
        "idoma": "Òyìchō / ɔɥá",
        "tiv": None
    },

    "star": {
        "igbo": "kpakpando",
        "hausa": "tauraro",
        "yoruba": "ìràwọ̀",
        "idoma": None,
        "tiv": None
    },

    "sky": {
        "igbo": "mbara igwe",
        "hausa": "sama",
        "yoruba": "sánmà / ojú ọ̀run",
        "idoma": None,
        "tiv": None
    },

    "rain": {
        "igbo": "mmiri ozuzo",
        "hausa": "ruwan sama",
        "yoruba": "òjò",
        "idoma": "ówó (verify tone/orthography)",
        "tiv": "ra / la (verify orthography)"
    },

    "fire": {
        "igbo": "ọkụ",
        "hausa": "wuta",
        "yoruba": "iná",
        "idoma": "Òlà",
        "tiv": "usu (verify orthography)"
    },

    "tree": {
        "igbo": "osisi",
        "hausa": "itace",
        "yoruba": "igi",
        "idoma": "Òchí",
        "tiv": None
    },

    "road": {
        "igbo": "ụzọ",
        "hausa": "hanya",
        "yoruba": "ọ̀nà",
        "idoma": "Òwè (path; verify road)",
        "tiv": None
    },

    "market": {
        "igbo": "ahịa",
        "hausa": "kasuwa",
        "yoruba": "ọjà",
        "idoma": None,
        "tiv": None
    },

    "money": {
        "igbo": "ego",
        "hausa": "kuɗi",
        "yoruba": "owó",
        "idoma": "Ìjè",
        "tiv": None
    },

    "watermelon": {
        "igbo": "elegede (verify regional usage)",
        "hausa": "kankana",
        "yoruba": "elegede / bàrà (verify regional usage)",
        "idoma": None,
        "tiv": None
    },

    "dog": {
        "igbo": "nkịta",
        "hausa": "kare",
        "yoruba": "ajá",
        "idoma": "Ewo (verify tone/orthography)",
        "tiv": "iwya"
    },

    "goat": {
        "igbo": "ewu",
        "hausa": "akuya",
        "yoruba": "ewúrẹ́",
        "idoma": "Èwū",
        "tiv": "ivo"
    },

    "chicken": {
        "igbo": "ọkụkọ",
        "hausa": "kaza",
        "yoruba": "adìyẹ",
        "idoma": "Ūgū (fowl; verify chicken)",
        "tiv": "ikyegh"
    },

    "river": {
        "igbo": "osimiri",
        "hausa": "kogi",
        "yoruba": "odò",
        "idoma": None,
        "tiv": None
    },

    "mountain": {
        "igbo": "ugwu",
        "hausa": "dutse",
        "yoruba": "òkè (hill/mountain)",
        "idoma": None,
        "tiv": None
    },

    "day": {
        "igbo": "ụbọchị",
        "hausa": "rana / yini",
        "yoruba": "ọjọ́",
        "idoma": None,
        "tiv": None
    },

    "night": {
        "igbo": "abalị",
        "hausa": "dare",
        "yoruba": "òru",
        "idoma": "Òtú",
        "tiv": "tuwu (verify orthography)"
    },

    "happiness": {
        "igbo": "ọṅụ",
        "hausa": "farin ciki",
        "yoruba": "ayọ̀ / ìdùnnú",
        "idoma": "Ngbede (verify usage)",
        "tiv": None
    },

    "peace": {
        "igbo": "udo",
        "hausa": "zaman lafiya / salama",
        "yoruba": "àlàáfíà",
        "idoma": None,
        "tiv": None
    }
}


# ==========================================
# WELCOME MESSAGE
# ==========================================

def welcome_message():

    print("\n========================================")
    print("   MULTILINGUAL TRANSLATION SYSTEM")
    print("             VERSION 2")
    print("========================================")
    print("English to Five Nigerian Languages")
    print("Total Words: 20")
    print("Available Languages: 5")
    print("========================================")


# ==========================================
# LANGUAGE SELECTION
# ==========================================

def select_language():

    languages = ["igbo", "hausa", "yoruba", "idoma", "tiv"]

    while True:

        print("\nSELECT YOUR LANGUAGE")

        for number, language in enumerate(languages, start=1):
            print(f"{number}. {language.title()}")

        choice = input("\nChoose a language (1-5): ").strip()

        if choice in ["1", "2", "3", "4", "5"]:

            selected_language = languages[int(choice) - 1]

            print(f"\nYou selected {selected_language.title()}")

            return selected_language

        else:

            print("Invalid selection! Choose between 1 and 5.")


# ==========================================
# DISPLAY AVAILABLE WORDS
# ==========================================

def display_words():

    print("\nAVAILABLE ENGLISH WORDS")

    for number, word in enumerate(translations.keys(), start=1):

        print(f"{number}. {word.title()}")


# ==========================================
# TRANSLATE ONE WORD
# ==========================================

def translate_word(language):

    word = input("\nEnter an English word: ").strip().lower()

    if word in translations:

        result = translations[word][language]

        print("\n========================================")
        print("          TRANSLATION RESULT")
        print("========================================")

        print(f"English: {word.title()}")

        if result is not None:

            print(f"{language.title()}: {result}")

        else:

            print(f"{language.title()}: Translation not available.")

        print("========================================")

    else:

        print("\nWord not found!")

        print("Please select a word from the available list.")


# ==========================================
# TRANSLATE ALL WORDS
# ==========================================

def translate_all(language):

    print("\n========================================")
    print(f"      ALL WORDS IN {language.upper()}")
    print("========================================")

    for number, (word, language_data) in enumerate(
        translations.items(), start=1
    ):

        result = language_data[language]

        if result is None:
            result = "Not available"

        print(f"{number}. {word.title()} = {result}")

    print("========================================")


# ==========================================
# DISPLAY ALL LANGUAGE TRANSLATIONS
# ==========================================

def display_all_languages():

    print("\n========================================")
    print("       COMPLETE TRANSLATION TABLE")
    print("========================================")

    for word, language_data in translations.items():

        print(f"\n{word.title()}")

        for language, translation in language_data.items():

            if translation is None:
                translation = "Not available"

            print(f"  {language.title()}: {translation}")

    print("\n========================================")


# ==========================================
# MAIN MENU
# ==========================================

def main_menu(language):

    while True:

        print("\n========================================")
        print("              MAIN MENU")
        print("========================================")

        print(f"Selected Language: {language.title()}")

        print("1. Translate a word")
        print("2. View available English words")
        print("3. Translate all 20 words")
        print("4. View all language translations")
        print("5. Change language")
        print("6. Exit")

        print("========================================")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":

            translate_word(language)

        elif choice == "2":

            display_words()

        elif choice == "3":

            translate_all(language)

        elif choice == "4":

            display_all_languages()

        elif choice == "5":

            language = select_language()

        elif choice == "6":

            print("\nThank you for using our system!")
            print("Goodbye!")

            break

        else:

            print("\nInvalid option! Please choose between 1 and 6.")


# ==========================================
# MAIN FUNCTION
# ==========================================

def main():

    welcome_message()

    language = select_language()

    main_menu(language)


# ==========================================
# EXECUTE PROGRAM
# ==========================================

if __name__ == "__main__":

    main()