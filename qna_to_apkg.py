import genanki
import markdown
import random


def to_list(text: str):
    i = 1
    qna = []

    while len(text) > 0:
        question_index = text.find(str(i) + ". ") + 2 + i // 10
        if question_index == -1:
            break

        text = text[question_index:]
        new_line_index = text.find("\n")
        question = text[:new_line_index]
        text = text[new_line_index:]

        before_next_question_index = text.find(str(i + 1) + ". ")
        if before_next_question_index == -1:
            answer = text
            answer = markdown.markdown(answer.strip())
            qna.append([question, answer])
            break
        else:
            answer = text[:before_next_question_index]
            answer = markdown.markdown(answer.strip())
            qna.append([question, answer])
            i += 1

    return qna


def add_notes(deck: genanki.Deck, text: str):
    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),
        "Simple Model",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )

    questions = to_list(text)

    for question, answer in questions:
        note = genanki.Note(model=model, fields=[question, answer])

        deck.add_note(note)


def qna_to_apkg(text, filepath):
    my_deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), "New Deck")

    add_notes(my_deck, text)

    genanki.Package(my_deck).write_to_file(filepath)


def test_to_apkg():

    text = """1. What is a one-time password?

    A one-time password (OTP) is a password that only has one use, also known as dynamic password. It is usually used as a second authentication factor, in addition to the username and password commonly used.

    2. How do one-time passwords work?

    One-time passwords are generated through cryptographic algorithms that produce unique sequences. They are then delivered to the user via a variety of methods, such as SMS, email, or push notifications. The user must enter the OTP within a specified timeframe, usually a few minutes, in order to complete the authentication process.

    3. What are the different types of one-time passwords?

    There are three main types of one-time passwords:

    * Time-based OTPs: These passwords change over time, usually every 30 seconds or so.
    * Event-based OTPs: These passwords change every time a specific event takes place, such as logging in to a website or making a payment.
    * Disposable single-use OTPs: These passwords are used only once and are valid only for a short period of time.

    4. What are the advantages of using one-time passwords?

    One-time passwords offer several advantages over traditional static passwords, including:

    * **Reuse prevention:** OTPs cannot be reused, which makes them more resistant to brute-force attacks.
    * **Protection against keyloggers:** OTPs are not stored on the user's device, so they cannot be intercepted by keyloggers.
    * **Multifactor authentication:** OTPs can be used in conjunction with other authentication factors, such as a username and password, to provide stronger security.
    * **Phishing reduction:** OTPs are not sent over email or in text messages, which reduces the risk of phishing attacks.  

    5. What are the disadvantages of using one-time passwords?

    One-time passwords can have some disadvantages, including:

    * **Convenience:** OTPs can be inconvenient to use, especially if they are delivered via SMS or email.
    * **Cost:** OTPs can be costly to implement, especially if they are delivered via SMS.
    * **Complexity:** OTPs can be complex to implement and manage, especially in large organizations.

    6. What are the security risks associated with one-time passwords?

    One-time passwords can be subject to a number of security risks, including:

    * **Phishing:** OTPs can be phished by attackers who send fake emails or text messages that appear to be from a legitimate source.
    * **Compromised devices:** OTPs can be compromised if the user's device is infected with malware.
    * **Man-in-the-middle (MitM) attacks:** OTPs can be intercepted by attackers who are able to eavesdrop on the communication channel between the user and the authentication server.
    * **SMS reception:** OTPs that are delivered via SMS can be intercepted by attackers who are able to access the user's SMS inbox.

    7. What are the additional security measures that can be used to protect one-time passwords?

    There are a number of additional security measures that can be used to protect one-time passwords, including:

    * **Using secure hardware:** One-time passwords can be generated and stored on a hardware security module (HSM), which is a physical device that is designed to protect sensitive data.
    * **Using secure messaging:** OTPs can be delivered via secure messaging protocols, such as HTTPS or SRTP.
    * **Limiting authentication attempts:** The number of authentication attempts that can be made with a single OTP can be limited, which can help to prevent brute-force attacks.

    8. What are some common use cases for one-time passwords?

    One-time passwords are used in a variety of applications, including:

    * **Systems and apps:** Users are given a unique password each time they attempt to log in to a system or app.
    * **Two-step verification:** After entering the traditional static password, the user receives a password that must be entered to complete the authentication process.
    * **Online transactions:** When performing financial transactions, users can receive an OTP that validates the transaction.

    9. What is the future of one-time passwords?

    One-time passwords are an important security measure that can help to protect against a variety of threats. As the number of threats to online security continues to grow, the use of one-time passwords is likely to increase.
    """

    qna_to_apkg(text, "output/temp.apkg")


def test_qna_to_list():

    text = """1. What is a one-time password?

    A one-time password (OTP) is a password that only has one use, also known as dynamic password. It is usually used as a second authentication factor, in addition to the username and password commonly used.

    2. How do one-time passwords work?

    One-time passwords are generated through cryptographic algorithms that produce unique sequences. They are then delivered to the user via a variety of methods, such as SMS, email, or push notifications. The user must enter the OTP within a specified timeframe, usually a few minutes, in order to complete the authentication process.

    3. What are the different types of one-time passwords?

    There are three main types of one-time passwords:

    * Time-based OTPs: These passwords change over time, usually every 30 seconds or so.
    * Event-based OTPs: These passwords change every time a specific event takes place, such as logging in to a website or making a payment.
    * Disposable single-use OTPs: These passwords are used only once and are valid only for a short period of time.

    4. What are the advantages of using one-time passwords?

    One-time passwords offer several advantages over traditional static passwords, including:

    * **Reuse prevention:** OTPs cannot be reused, which makes them more resistant to brute-force attacks.
    * **Protection against keyloggers:** OTPs are not stored on the user's device, so they cannot be intercepted by keyloggers.
    * **Multifactor authentication:** OTPs can be used in conjunction with other authentication factors, such as a username and password, to provide stronger security.
    * **Phishing reduction:** OTPs are not sent over email or in text messages, which reduces the risk of phishing attacks.  

    5. What are the disadvantages of using one-time passwords?

    One-time passwords can have some disadvantages, including:

    * **Convenience:** OTPs can be inconvenient to use, especially if they are delivered via SMS or email.
    * **Cost:** OTPs can be costly to implement, especially if they are delivered via SMS.
    * **Complexity:** OTPs can be complex to implement and manage, especially in large organizations.

    6. What are the security risks associated with one-time passwords?

    One-time passwords can be subject to a number of security risks, including:

    * **Phishing:** OTPs can be phished by attackers who send fake emails or text messages that appear to be from a legitimate source.
    * **Compromised devices:** OTPs can be compromised if the user's device is infected with malware.
    * **Man-in-the-middle (MitM) attacks:** OTPs can be intercepted by attackers who are able to eavesdrop on the communication channel between the user and the authentication server.
    * **SMS reception:** OTPs that are delivered via SMS can be intercepted by attackers who are able to access the user's SMS inbox.

    7. What are the additional security measures that can be used to protect one-time passwords?

    There are a number of additional security measures 
    8. What are some common use cases for one-time passwords?

    One-time passwords are used in a variety of

    9. What is the future of one-time passwords?

    One-time passwords are an important security measure that can help to protect against a variety of threats. As the number of threats to online security continues to grow, the use of one-time passwords is likely to increase.
    """

    print(to_list(text))


if __name__ == "__main__":
    test_to_apkg()
