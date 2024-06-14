from pptx_to_qna import extract_text_from_pptx, generate_qna
from qna_to_apkg import qna_to_apkg


def pptx_to_apkg(pptx_file: str, apkg_file: str):
    extracted_text = extract_text_from_pptx(pptx_file)
    qna = generate_qna(extracted_text)
    print(qna)
    qna_to_apkg(qna, apkg_file)


def test():
    pptx_file = "OTP.pptx"
    apkg_file = "output/test.apkg"

    pptx_to_apkg(pptx_file, apkg_file)


if __name__ == "__main__":
    test()
