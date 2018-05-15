// C > Structs and Enums > Structuring the Document
//
//
// https://www.hackerrank.com/challenges/structuring-the-document/problem
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5

struct word {
    char* data;
};

struct sentence {
    struct word* data;
    int word_count;//denotes number of words in a sentence
};

struct paragraph {
    struct sentence* data  ;
    int sentence_count;//denotes number of sentences in a paragraph
};

struct document {
    struct paragraph* data;
    int paragraph_count;//denotes number of paragraphs in a document
};
// (skeliton_head) ----------------------------------------------------------------------

struct document get_document(char* text)
{
    struct document doc;
    struct paragraph *cur_paragraph = NULL;
    struct sentence *cur_sentence = NULL;
    char *new_word = NULL;

    doc.data = NULL;
    doc.paragraph_count = 0;

    for (char *s = text; *s; ++s)
    {
        if (*s == ' ' || *s == '.')
        {
            // nouveau paragraphe
            if (cur_paragraph == NULL)
            {
                doc.paragraph_count++;
                doc.data = (struct paragraph *) realloc(doc.data, sizeof(struct paragraph) * doc.paragraph_count);

                cur_paragraph = doc.data + doc.paragraph_count - 1;
                cur_paragraph->data = NULL;
                cur_paragraph->sentence_count = 0;

                cur_sentence = NULL;        // on recommence de facto une phrase
            }

            // nouvelle phrase
            if (cur_sentence == NULL)
            {
                cur_paragraph->sentence_count++;
                cur_paragraph->data = (struct sentence *) realloc(cur_paragraph->data, sizeof(struct sentence) * cur_paragraph->sentence_count);

                cur_sentence = cur_paragraph->data + cur_paragraph->sentence_count - 1;
                cur_sentence->data = NULL;
                cur_sentence->word_count = 0;
            }

            // nouveau mot
            cur_sentence->word_count++;
            cur_sentence->data = (struct word *) realloc(cur_sentence->data, sizeof(struct word) * cur_sentence->word_count);
            cur_sentence->data[cur_sentence->word_count - 1].data = new_word;
            new_word = NULL;

            if (*s == '.')
                cur_sentence = NULL;        // on recommencera une phrase
            *s = 0;
        }

        else if (*s == '\n')
        {
            cur_sentence = NULL;
            cur_paragraph = NULL;
        }
        else
        {
            if (new_word == NULL)
            {
                new_word = s;
            }
        }
    }

    return doc;
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n)
{
    return Doc.data[n - 1].data[m - 1].data[k - 1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m)
{
    return Doc.data[m - 1].data[k - 1];
}

struct paragraph kth_paragraph(struct document Doc, int k)
{
    return Doc.data[k - 1];
}

// (skeliton_tail) ----------------------------------------------------------------------
void print_word(struct word w) {
    printf("%s", w.data);
}

void print_sentence(struct sentence sen) {
    for(int i = 0; i < sen.word_count; i++) {
        print_word(sen.data[i]);
        if (i != sen.word_count - 1) {
            printf(" ");
        }
    }
}

void print_paragraph(struct paragraph para) {
    for(int i = 0; i < para.sentence_count; i++){
        print_sentence(para.data[i]);
        printf(".");
    }
}

void print_document(struct document doc) {
    for(int i = 0; i < doc.paragraph_count; i++) {
        print_paragraph(doc.data[i]);
        if (i != doc.paragraph_count - 1)
            printf("\n");
    }
}

char* get_input_text() {
    int paragraph_count;
    scanf("%d", &paragraph_count);

    char p[MAX_PARAGRAPHS][MAX_CHARACTERS], doc[MAX_CHARACTERS];
    memset(doc, 0, sizeof(doc));
    getchar();
    for (int i = 0; i < paragraph_count; i++) {
        scanf("%[^\n]%*c", p[i]);
        strcat(doc, p[i]);
        if (i != paragraph_count - 1)
            strcat(doc, "\n");
    }

    char* returnDoc = (char*)malloc((strlen (doc)+1) * (sizeof(char)));
    strcpy(returnDoc, doc);
    return returnDoc;
}

int main()
{
    //local debug
    //freopen("tests//structuring-the-document/input/input04.txt", "r", stdin);

    char* text = get_input_text();
    struct document Doc = get_document(text);

    int q;
    scanf("%d", &q);

    while (q--) {
        int type;
        scanf("%d", &type);

        if (type == 3){
            int k, m, n;
            scanf("%d %d %d", &k, &m, &n);
            struct word w = kth_word_in_mth_sentence_of_nth_paragraph(Doc, k, m, n);
            print_word(w);
        }

        else if (type == 2) {
            int k, m;
            scanf("%d %d", &k, &m);
            struct sentence sen= kth_sentence_in_mth_paragraph(Doc, k, m);
            print_sentence(sen);
        }

        else{
            int k;
            scanf("%d", &k);
            struct paragraph para = kth_paragraph(Doc, k);
            print_paragraph(para);
        }
        printf("\n");
    }
}
