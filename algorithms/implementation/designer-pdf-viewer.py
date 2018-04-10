# Designer PDF Viewer
# Help finding selection area in PDF Viewer.
#
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#

def designerPdfViewer(h, word):
    # Complete this function
    return max(h[ord(c) - ord('a')] for c in word) * len(word)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
