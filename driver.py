import argparse
import speech_recognition as sr
from ASRDefault import ASRDefault
from NLUDefault import NLUDefault
from NLGDefault import NLGDefault
from T2SDefault import T2SDefault, FileCannotPlayError
from FrameDMSimple import FrameDMSimple


def main():
    parser = argparse.ArgumentParser("Homework 1 dialog manager system")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-s", "--system", choices=["FrameSimple"])
    parser.add_argument("-l", "--NLU", default="Default")
    parser.add_argument("-g", "--NLG", default="Default")
    parser.add_argument("-a", "--ASR", default="no ASR")
    parser.add_argument("-t", "--T2S", default="T2S")

    args = parser.parse_args()

    system = args.system
    NLU = args.NLU
    NLG = args.NLG
    ASR = args.ASR
    T2S = args.T2S

    print("NLU = {}, system = {}, NLG = {}".format(NLU, system, NLG))

    NLUModule = None
    DMModule = None
    NLGModule = None
    ASRModule = None
    T2SModule = None

    if NLU == "Default":
        NLUModule = NLUDefault()

    if NLG == "Default":
        NLGModule = NLGDefault()

    if ASR == "ASR":
        ASRModule = ASRDefault()

    if T2S == 'T2S':
        T2SModule = T2SDefault()

    if system == "FrameSimple":
        DMModule = FrameDMSimple(NLUModule, NLGModule)
    else:
        print("{} not implemented".format(system))
        return

    print("Welcome to the pizza ordering system. How can we help you?")
    if T2SModule:
        try:
            T2SModule.play("Welcome to the pizza ordering system. How can we help you?")
        except Exception as e:
            print(e)

    internet_at_work = True

    while True:
        if ASRModule:
            while True:
                try:
                    print('Please begin talking:')
                    inputStr = ASRModule.listen()
                    break
                except sr.UnknownValueError:
                    print('Unable to recognize speech, can you say it again?')
                except sr.WaitTimeoutError:
                    print('Unable to recognize speech in 10s, can you say it again?')
            print("> {}".format(inputStr))
        else:
            inputStr = input("> ")
        if inputStr.lower() == "quit":
            break

        try:
            outputStr = DMModule.execute(inputStr)
        except Exception as e:
            print(e)
            break

        print(outputStr)
        if T2SModule:
            try:
                if internet_at_work:
                    T2SModule.play(outputStr)
            except Exception as e:
                internet_at_work = False
                print(e)


if __name__ == "__main__":
    main()
